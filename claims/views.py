from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ClaimCreateSerializer, ClaimResponseSerializer
from .models import Claim
from .services import ClaimService

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ClaimCreateSerializer
        return ClaimResponseSerializer

    def create(self, request, *args, **kwargs):
        serializer = ClaimCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

    
        result = ClaimService.process_claim(serializer.validated_data)
        claim = Claim.objects.create(
            member=result["member"],
            provider=result["provider"],
            procedure=result["procedure"],
            diagnosis=result["diagnosis"],
            claim_amount=serializer.validated_data["claim_amount"],
            status=result["status"],
            fraud_flag=result["fraud_flag"],
            approved_amount=result["approved_amount"],
        )

        response_serializer = ClaimResponseSerializer(claim)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)