from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmergencyContact
from .forms import EmergencyContactForm  # Ensure this form is created

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from .serializers import EmergencyContactSerializer


class EmergencyContactListCreateView(generics.ListCreateAPIView):
    """
    API to list all emergency contacts for the authenticated user and create new ones.
    """
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EmergencyContact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set user automatically

    def create(self, request, *args, **kwargs):
        """
        Custom error handling for creating contacts.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "status": "True",
                "message": "Emergency contact created successfully.",
                "data": serializer.data,
            },status=status.HTTP_201_CREATED)
        
        return Response({
            "status": "False",
            "message": "Failed to create emergency contact.",
            "error": "Invalid data provided",
            "details": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class EmergencyContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API to retrieve, update, or delete an emergency contact.
    Ensures that a user can only modify their own contacts.
    """
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EmergencyContact.objects.filter(user=self.request.user)

    def get_object(self):
        """
        Ensures users can only access their own emergency contacts.
        Raises a NotFound or PermissionDenied error if unauthorized.
        """
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this contact.")
        return obj

    def update(self, request, *args, **kwargs):
        """
        Custom error handling for updating emergency contacts.
        """
        partial = kwargs.pop('partial', False)  # Allows PATCH requests
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "status": "True",
                "message": "Emergency contact updated successfully.",
                "data": serializer.data,
            }, status=status.HTTP_200_OK)
        
        return Response({
            "status": "False",
            "message": "Failed to update emergency contact.",
            "error": "Invalid data provided",
            "details": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Custom error handling for deleting contacts.
        """
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "status": "True",
                "message": "Emergency contact deleted successfully."
            }, status=status.HTTP_204_NO_CONTENT)
        
        except NotFound:
            return Response({
                "status": "False",
                "message": "Failed to delete emergency contact.",
                "error": "Emergency contact not found."
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "status": "False",
                "message": "Failed to delete emergency contact.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



@login_required
def add_contact_view(request):
    """
    View to add a new emergency contact.
    """
    if request.method == "POST":
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user  # Assign the current user
            contact.save()
            messages.success(request, "Emergency contact added successfully!")
            return redirect("emergency:list_contacts")  # Redirect to contacts list
        else:
            messages.error(request, "Error: Please correct the form errors.")
    else:
        form = EmergencyContactForm()

    return render(request, "emergency/add_contact.html", {"form": form})


@login_required
def list_contacts_view(request):
    """
    View to display all emergency contacts of the authenticated user.
    Allows deletion and updating of contacts.
    """
    contacts = EmergencyContact.objects.filter(user=request.user)

    return render(request, "emergency/list_contacts.html", {"contacts": contacts})


@login_required
def delete_contact_view(request, contact_id):
    """
    Deletes an emergency contact if it belongs to the logged-in user.
    """
    contact = get_object_or_404(EmergencyContact, id=contact_id, user=request.user)
    contact.delete()
    messages.success(request, "Contact deleted successfully.")
    return redirect("emergency:list_contacts")


@login_required
def update_contact_view(request, contact_id):
    """
    View to update an emergency contact.
    """
    contact = get_object_or_404(EmergencyContact, id=contact_id, user=request.user)

    if request.method == "POST":
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully!")
            return redirect("emergency:list_contacts")
        else:
            messages.error(request, "Error updating contact.")

    else:
        form = EmergencyContactForm(instance=contact)

    return render(request, "emergency/update_contact.html", {"form": form, "contact": contact})
