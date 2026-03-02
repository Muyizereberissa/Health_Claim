from rest_framework import serializers
from .models import Claim, Member, Provider, Procedure, Diagnosis

class ClaimCreateSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())
    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all())
    procedure = serializers.PrimaryKeyRelatedField(queryset=Procedure.objects.all())
    diagnosis = serializers.PrimaryKeyRelatedField(queryset=Diagnosis.objects.all())

    class Meta:
        model = Claim
        fields = ["member", "provider", "procedure", "diagnosis", "claim_amount"]

class ClaimResponseSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField()
    provider = serializers.StringRelatedField()
    procedure = serializers.StringRelatedField()
    diagnosis = serializers.StringRelatedField()

    class Meta:
        model = Claim
        fields = [
            "id",
            "member",
            "provider",
            "procedure",
            "diagnosis",
            "claim_amount",
            "status",
            "fraud_flag",
            "approved_amount",
            "created_at",
        ]