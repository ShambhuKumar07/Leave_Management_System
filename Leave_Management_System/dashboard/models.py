#dashboard/models.py

from django.db import models

# Create your models here.
from django.db import models

class ProfileDetails(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Employee Code")
    name = models.CharField(max_length=100, verbose_name="Full Name")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], verbose_name="Gender")
    mobile = models.CharField(max_length=15, verbose_name="Mobile Number")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    father_name = models.CharField(max_length=100, verbose_name="Father's Name")
    spouse_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Spouse's Name")
    present_address = models.TextField(verbose_name="Present Address")
    permanent_address = models.TextField(verbose_name="Permanent Address")
    dob = models.DateField(verbose_name="Date of Birth")
    blood_group = models.CharField(max_length=5, blank=True, null=True, verbose_name="Blood Group")
    emergency_contact = models.CharField(max_length=15, verbose_name="Emergency Contact Number")
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True, verbose_name="Profile Image")

    def __str__(self):
        return f"{self.name} ({self.code})"
