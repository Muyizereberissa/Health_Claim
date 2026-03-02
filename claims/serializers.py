from rest_framework import serializers
from .models import Claim

class ClaimCreateSerializer(serializers.Serializer):
    member_id = serializers.CharField()
    provider_id = serializers.CharField()
    procedure_code = serializers.CharField()
    diagnosis_code = serializers.CharField()
    claim_amount = serializers.DecimalField(max_digits=12, decimal_places=2)

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