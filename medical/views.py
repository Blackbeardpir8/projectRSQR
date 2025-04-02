from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import MedicalDetail
from .serializers import MedicalDetailSerializer
from .forms import MedicalDetailForm  # Only keep this if using Django Forms in HTML templates


class MedicalDetailAPIView(APIView):
    """
    API to get and update medical details.
    """
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        try:
            medical_detail, created = MedicalDetail.objects.get_or_create(user=request.user)
            serializer = MedicalDetailSerializer(medical_detail)
            return Response({
                "status": "True",
                "message": "Medical details retrieved successfully.",
                "data": serializer.data,    
            },status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "False",
                "message": "Failed to retrieve medical details.",
                "error": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

    def put(self, request):
        try:
            medical_detail, _ = MedicalDetail.objects.get_or_create(user=request.user)
            serializer = MedicalDetailSerializer(medical_detail, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "True",
                    "message": "Medical details updated successfully.",
                    "data": serializer.data,
                }, status=status.HTTP_200_OK)

            return Response({
                "status": "False",
                "message": "Failed to update medical details.",
                "error": "Invalid data provided",
                "details": serializer.errors,
                "error": "Invalid data provided"
            }, status=status.HTTP_400_BAD_REQUEST)

        except MedicalDetail.DoesNotExist:
            return Response({
                "status": "False",
                "message": "Failed to update medical details.",
                "error": "Medical record not found."
            }, status=status.HTTP_404_NOT_FOUND)    

        except Exception as e:
            return Response({
                "status": "False",
                "message": "Failed to update medical details.", 
                "error": "An unexpected error occurred.", "details": str(e)
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR,)

# Create this form

@login_required
def medical_detail_view(request):
    medical_detail = MedicalDetail.objects.filter(user=request.user).first()

    if not medical_detail:
        return render(request, "medical/no_details.html")  # Create this template
    
    return render(request, "medical/medical_detail.html", {"medical_detail": medical_detail})

@login_required
def update_medical_details(request):
    medical_detail, created = MedicalDetail.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = MedicalDetailForm(request.POST, request.FILES, instance=medical_detail)
        if form.is_valid():
            form.save()
            return redirect("medical/medical-details")  # Redirect to details page

    else:
        form = MedicalDetailForm(instance=medical_detail)

    return render(request, "medical/update_medical_details.html", {"form": form})
