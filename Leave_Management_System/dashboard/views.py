from django.shortcuts import render

from .models import ProfileDetails

 

# Create your views here.

def dashboard(request):
    return render(request,"dashboard/index.html")

# def profile(request):
#     # Retrieve all profiles from the database
#     profiles = ProfileDetails.objects.all()

#     fields = ProfileDetails._meta.fields  # Pass fields explicitly
#     return render(request, 'dashboard/profile.html', {'profiles': profiles, 'fields': fields})


# dashboard/views.py
from django.shortcuts import render
from .models import ProfileDetails

# def profile(request):
#     # Retrieve all profiles from the database
#     profiles = ProfileDetails.objects.all()

#     # Extract field names and verbose names
#     fields = [
#         {'name': field.name, 'verbose_name': field.verbose_name}
#         for field in ProfileDetails._meta.fields
#     ]
#     return render(request, 'dashboard/profile.html', {'profiles': profiles, 'fields': fields})



def profile(request):
    # Assuming profiles is a queryset of Profile objects
    profiles = ProfileDetails.objects.all()  # Adjust to your logic for fetching profiles
    
    processed_profiles = []
    for profile in profiles:
        fields = []
        for field in profile._meta.fields:
            field_value = getattr(profile, field.name, 'N/A')
            fields.append({
                'name': field.name,
                'verbose_name': field.verbose_name,
                'value': field_value,
                'type': 'email' if field.name == 'email' else 'text',
            })
        processed_profiles.append(fields)

    return render(request, 'dashboard/profile.html', {'profiles': processed_profiles})






    # return render(request, 'dashboard/profile.html', {'profiles': profiles})    
    # return render(request,"dashboard/profile.html") 

def organization(request):    
    return render(request,"dashboard/organization.html") 

def monthly_ctc(request):    
    return render(request,"dashboard/monthly_ctc.html")

def yearly_ctc(request):    
    return render(request,"dashboard/yearly_ctc.html")


def qualification(request):    
    return render(request,"dashboard/Qualification.html") 


def previous_experience(request):    
    return render(request,"dashboard/previous_experience.html") 


def leave(request):    
    return render(request,"dashboard/leave.html")


def special_application(request):    
    return render(request,"dashboard/special_application.html")



def Compensatory_off_Request(request):    
    return render(request,"dashboard/Compensatory_off_Request.html")


def daily_attendence(request):    
    return render(request,"dashboard/daily_attendence2.html")
