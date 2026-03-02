from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Member, Provider, Procedure, Diagnosis, Claim

class ClaimAPITestCase(APITestCase):

    def setUp(self):
        self.member = Member.objects.create(
            member_id="M001",
            full_name="Joseph Habineza",
            is_active=True,
            benefit_limit=50000
        )
        self.provider = Provider.objects.create(
            provider_id="P001",
            name="Legacy Hospital"
        )
        self.procedure = Procedure.objects.create(
            procedure_code="PRO001",
            description="Blood tes",
            average_cost=20000
        )
        self.diagnosis = Diagnosis.objects.create(
            diagnosis_code="D001",
            description="Malaria"
        )

        self.url = reverse("claim-list") 

    def test_create_claim(self):
        """Test POST /claims/ creates a claim successfully"""
        data = {
            "member_id": self.member.member_id,
            "provider_id": self.provider.provider_id,
            "procedure_code": self.procedure.procedure_code,
            "diagnosis_code": self.diagnosis.diagnosis_code,
            "claim_amount": 40000
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["member"], self.member.member_id)
        self.assertEqual(response.data["provider"], self.provider.provider_id)
        self.assertEqual(response.data["procedure"], self.procedure.procedure_code)
        self.assertEqual(response.data["diagnosis"], self.diagnosis.diagnosis_code)

        self.assertEqual(response.data["claim_amount"], "40000.00")
        self.assertIn(response.data["status"], ["APPROVED", "PARTIAL", "REJECTED"])
        self.assertIn("fraud_flag", response.data)
        self.assertIn("approved_amount", response.data)
        self.assertIn("created_at", response.data)

    def test_claim_fraud_flag(self):
        """Test that fraud_flag is True if claim_amount > 2x procedure average_cost"""
        data = {
            "member_id": self.member.member_id,
            "provider_id": self.provider.provider_id,
            "procedure_code": self.procedure.procedure_code,
            "diagnosis_code": self.diagnosis.diagnosis_code,
            "claim_amount": 50000  
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["fraud_flag"])

    def test_inactive_member_rejected(self):
        """Test that an inactive member results in REJECTED claim"""
        self.member.is_active = False
        self.member.save()

        data = {
            "member_id": self.member.member_id,
            "provider_id": self.provider.provider_id,
            "procedure_code": self.procedure.procedure_code,
            "diagnosis_code": self.diagnosis.diagnosis_code,
            "claim_amount": 10000
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "REJECTED")
        self.assertEqual(response.data["approved_amount"], "0.00")