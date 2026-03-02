from decimal import Decimal
from rest_framework.exceptions import ValidationError
from .models import Member, Provider, Procedure, Diagnosis


class ClaimService:

    @staticmethod
    def process_claim(data):
        try:
            member = Member.objects.get(member_id=data["member_id"])
        except Member.DoesNotExist:
            raise ValidationError({"member_id": "Member not found."})

        try:
            provider = Provider.objects.get(provider_id=data["provider_id"])
        except Provider.DoesNotExist:
            raise ValidationError({"provider_id": "Provider not found."})

        try:
            procedure = Procedure.objects.get(procedure_code=data["procedure_code"])
        except Procedure.DoesNotExist:
            raise ValidationError({"procedure_code": "Procedure not found."})

        try:
            diagnosis = Diagnosis.objects.get(diagnosis_code=data["diagnosis_code"])
        except Diagnosis.DoesNotExist:
            raise ValidationError({"diagnosis_code": "Diagnosis not found."})

        claim_amount = data["claim_amount"]

        if not member.is_active:
            return {
                "status": "REJECTED",
                "fraud_flag": False,
                "approved_amount": Decimal("0"),
                "member": member,
                "provider": provider,
                "procedure": procedure,
                "diagnosis": diagnosis,
            }

        fraud_flag = claim_amount > (procedure.average_cost * 2)

        if claim_amount <= member.benefit_limit:
            status = "APPROVED"
            approved_amount = claim_amount
        else:
            status = "PARTIAL"
            approved_amount = member.benefit_limit

        return {
            "status": status,
            "fraud_flag": fraud_flag,
            "approved_amount": approved_amount,
            "member": member,
            "provider": provider,
            "procedure": procedure,
            "diagnosis": diagnosis,
        }