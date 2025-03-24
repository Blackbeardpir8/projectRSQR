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
            return redirect('register-page')

        if CustomUser.objects.filter(email=email).exists():
            print("❌ Error: Email already registered!")
            messages.error(request, "Email is already registered!")
            return redirect('register-page')

        try:
            user = CustomUser.objects.create_user(
                email=email, password=password, phone=phone,
                first_name=first_name, last_name=last_name
            )
            user.save()
            print("✅ Registration Successful for:", email)

            messages.success(request, "Registration successful! Please log in.")
            return redirect('login-page')
        
        except Exception as e:
            print(f"❌ Database Error: {e}")
            messages.error(request, "Something went wrong! Try again.")
            return redirect('register-page')

    return render(request, 'register.html')


# ✅ User Login View (Template-Based)
def login_view(request):
    if request.user.is_authenticated:
        print("\n✅ User Already Logged In:", request.user.email)
        return redirect('about')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("\n--- Login Attempt ---")
        print(f"Email: {email}")
        print(f"Password: {password}")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            print(f"✅ Login Successful for: {email}")

            messages.success(request, "Login successful!")
            next_url = request.GET.get('next', 'about')
            return redirect(next_url)

        else:
            print("❌ Error: Invalid email or password!")
            messages.error(request, "Invalid email or password!")
            return redirect('login-page')

    return render(request, 'login.html')


# ✅ About View (Login Required)
@login_required
def about_view(request):
    return render(request, 'about.html')






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
