from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

User = get_user_model()


def signup_view(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name").strip()
        last_name = request.POST.get("last_name").strip()
        email = request.POST.get("email").strip().lower()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
        )

        # otp = user.generate_otp()

        # send_otp_email(user.email, otp)

        messages.success(request, "Account craeted successfully")

        return redirect("login")

    return render(request, "accounts/signup.html")


def login_view(request):

    if request.method == "POST":

        email = (request.POST.get("email") or "").strip().lower()
        password = request.POST.get("password") or ""

        user = authenticate(request, username=email, password=password)

        if user is None:
            messages.error(request, "Invalid Email or Password.")
            return redirect("login")

        login(request, user)

        return redirect("home")

    return render(request, "accounts/login.html")


from django.contrib.auth import logout


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successfully.")
    return redirect("login")


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def update_profile(request):

    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.phone = request.POST.get("phone")
        user.age = request.POST.get("age")
        user.gender = request.POST.get("gender")
        user.address = request.POST.get("address")
        user.city = request.POST.get("city")
        user.state = request.POST.get("state")
        user.country = request.POST.get("country")
        user.zip_code = request.POST.get("zip_code")

        if request.FILES.get("avatar"):
            user.avatar = request.FILES["avatar"]

        user.save()

        messages.success(request, "Profile Updated Successfully.")

        return redirect("profile")

    return render(request, "accounts/update_profile.html")


from django.contrib.auth import update_session_auth_hash


@login_required
def change_password(request):

    if request.method == "POST":

        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
            return redirect("change_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("change_password")

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, "Password Changed Successfully.")

        return redirect("profile")

    return render(request, "accounts/change_password.html")
