from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : "this is sent"
    }
    return render(request, 'index.html' , context)

def logos(request):
    return render(request, 'logos.html' )

def brandinglogos(request):
    return render(request, 'brandinglogos.html' )

def banners(request):
    return render(request, 'banners.html' )

def overlays(request):
    return render(request, 'overlays.html' )

def animations(request):
    return render(request, 'animations.html' )

def pricing(request):
    return render(request, 'pricing.html' )



def contactus(request):
    if request.method == "POST":
        # Get the form data
        name = request.POST.get('name')  
        country_code = request.POST.get('country_code')  # Get the selected country code
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        users_need = request.POST.get('users_need')

        # Combine country code with phone number
        full_phone_number = f"{country_code}{phone_number}"

        # Create and save the Contact instance
        contact = Contact(
            name=name,
            phone_number=full_phone_number,
            email=email,
            users_need=users_need,
        )
        contact.save()

        # Display success message
        messages.success(request, "Your details have been saved")

    return render(request, 'contactus.html')
