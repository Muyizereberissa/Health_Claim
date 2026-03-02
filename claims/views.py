from rest_framework import viewsets
from .models import Claim
from .serializers import ClaimCreateSerializer, ClaimResponseSerializer
from .services import ClaimService

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ClaimCreateSerializer
        return ClaimResponseSerializer

    def perform_create(self, serializer):
        result = ClaimService.process_claim(serializer.validated_data)
        serializer.save(
            member=result["member"],
            provider=result["provider"],
            procedure=result["procedure"],
            diagnosis=result["diagnosis"],
            status=result["status"],
            fraud_flag=result["fraud_flag"],
            approved_amount=result["approved_amount"],
        )