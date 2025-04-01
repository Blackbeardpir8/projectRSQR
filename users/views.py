from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated


# User Registration View (Django Template-Based)
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print("\n--- Registration Attempt ---")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}")

        if password != confirm_password:
            print("❌ Error: Passwords do not match!")
            messages.error(request, "Passwords do not match!")
            return render(request, 'users/register.html')

        if CustomUser.objects.filter(email=email).exists():
            print("❌ Error: Email already registered!")
            messages.error(request, "Email is already registered!")
            return render(request, 'users/register.html')

        try:
            user = CustomUser.objects.create_user(
                email=email, password=password, phone=phone,
                first_name=first_name, last_name=last_name
            )
            user.save()
            print("✅ Registration Successful for:", email)

            messages.success(request, "Registration successful! Please log in.")
            return render(request, 'users/login.html')
        
        except Exception as e:
            print(f"❌ Database Error: {e}")
            messages.error(request, "Something went wrong! Try again.")
            return render(request, 'users/register.html')
    return render(request, 'users/register.html')


# ✅ User Login View (Template-Based)
def login_view(request):
    # If user is already authenticated, redirect to 'profile' page
    if request.user.is_authenticated:
        print("\n✅ User Already Logged In:", request.user.email)
        return redirect('userprofile/profile')  # Redirect to the profile page in userprofile app

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("\n--- Login Attempt ---")
        print(f"Email: {email}")
        print(f"Password: {password}")

        # Authenticate user using email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            print(f"✅ Login Successful for: {email}")

            # Set success message
            messages.success(request, "Login successful!")

            # Always redirect to 'profile' page after successful login
            return render(request,'userprofile/profile.html')  # Redirect to the profile view after login

        else:
            print("❌ Error: Invalid email or password!")
            messages.error(request, "Invalid email or password!")
            return render(request , 'users/login.html')  # Redirect to login page on failure

    return render(request, 'users/login.html')


from django.contrib.auth import logout
from django.contrib import messages

def logout_view(request):
    if request.user.is_authenticated:
        print(f"\n✅ Logging out user: {request.user.email}")
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    else:
        print("\n⚠️ Logout Attempt: No user is currently logged in.")

    return render(request, 'users/login.html')


def about_view(request):
    return render(request, 'users/about.html')

def faq_view(request):
    return render(request, 'users/faq.html')

def privacy_policy_view(request):
    return render(request, 'users/privacy_policy.html')

def terms_of_service_view(request):
    return render(request, 'users/terms_of_service.html')

def how_it_works_view(request):
    return render(request, 'users/how_it_works.html')


# API User Registration View
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "True", 
                "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "status": "False", 
            "message": "User registration failed", 
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# API User Login View
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is None or not user.is_active:
            return Response({
                "status": "False", 
                "message": "Login failed", 
                "error": "Invalid email or password"
            }, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            "status": "True",
            "message": "Login successful",
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
                "phone": user.phone,
                "role": user.role
            }
        }, status=status.HTTP_200_OK)



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "phone": user.phone,
            "first_name": user.first_name,
            "last_name": user.last_name
        })



########################

# to get all data through API

#########################

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserCompleteDataSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(["GET"])
def get_user_complete_data(request):
    """Fetch all user-related data in one API response (Open for testing)."""
    
    if request.user.is_authenticated:
        user = request.user
    else:
        # ✅ Get any test user (Change ID if needed)
        user = User.objects.filter().first()  

    if not user:
        return Response({"error": "No users found in the database."}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserCompleteDataSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


##################################





from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer
from medical.models import MedicalDetail
from medical.serializers import MedicalDetailSerializer
from emergency.models import EmergencyContact
from emergency.serializers import EmergencyContactSerializer

User = get_user_model()

@api_view(["GET"])
def get_user_complete_data(request, user_id=None):
    """Fetch complete user data including medical details and emergency contacts."""
    
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({
                "status": "False",
                "message": "User not found.",
                "error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    else:
        user = request.user if request.user.is_authenticated else None

    if not user:
        return Response({
            "status": "False",
            "message": "Authentication required or user not found.",
            "error": "Authentication required or user not found."
        }, status=status.HTTP_401_UNAUTHORIZED)

    # Fetch related data
    user_profile = UserProfile.objects.filter(user=user).first()
    medical_details = MedicalDetail.objects.filter(user=user)
    emergency_contacts = EmergencyContact.objects.filter(user=user)

    # Serialize data
    user_data = {
        "user": {
            "id": user.id,
            "email": user.email,
            "phone": user.phone,
            "first_name": user.first_name,
            "middle_name": user.middle_name,
            "last_name": user.last_name,
            "role": user.role,
        },
        "profile": UserProfileSerializer(user_profile).data if user_profile else None,
        "medical_details": MedicalDetailSerializer(medical_details, many=True).data,
        "emergency_contacts": EmergencyContactSerializer(emergency_contacts, many=True).data,
    }

    return Response({
        "status": "True",
        "message": "User data fetched successfully.",
        "data":user_data      
    }, status=status.HTTP_200_OK)

