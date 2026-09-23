from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        subject = request.POST.get("subject", "").strip()
        msg = request.POST.get("message", "").strip()

        try:
            Contact.objects.create(name=name, email=email, subject=subject, message=msg)
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            print("Error:", e)
            messages.error(request, "Message could not be sent!")

        return redirect("contact")  # PRG pattern

    return render(request, "contact/contact.html")
