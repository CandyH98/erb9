from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        doctor_email = request.POST['doctor_email'] 

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an inquiry for this clinic")
                return redirect("listings:listing", listing_id=listing_id)
        contact = Contact(
            listing = listing,
            listing_id = listing_id,
            name = name,
            email = email,
            message = message,
            phone = phone,
            user_id = user_id,
            )
        contact.save()
        '''# send mail
        send_mail(
            "Clinic Inquiry",
            "There has been an inquiry for " + listing + ". Sign into the admin panel for more info",
            os.getenv('EMAIL_HOST_USER'),
            [doctor_email],
            fail_silently=False,
            )'''
        messages.success(request,"Your request has been submitted, a representative will" "get back to you soon")
        return redirect("listings:listing", listing_id=listing_id)
    
def delete_contact(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    contact.delete()
    return redirect("accounts:dashboard")

def edit_contact(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    if request.method =="POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/edit_contact.html", {"form":form, "contact":contact})