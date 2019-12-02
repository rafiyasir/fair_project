from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        claim_id = request.POST['claim_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id

        contact = Contact(location=claim_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('/claims/'+claim_id)


