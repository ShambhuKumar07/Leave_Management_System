# dashboard/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import dashboard,profile,organization,monthly_ctc,yearly_ctc,qualification,previous_experience,leave,special_application,Compensatory_off_Request,daily_attendence
 

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('organization/', organization, name='organization'),
    path('monthly_ctc/', monthly_ctc, name='monthly_ctc'),
    path('yearly_ctc/', yearly_ctc, name='yearly_ctc'),
    path('qualification/', qualification, name='qualification'),
    path('previous_experience/', previous_experience, name='previous_experience'),
    path('leave/', leave, name='leave'),
    path('special_application/', special_application, name='special_application'),
    path('Compensatory_off_Request/', Compensatory_off_Request, name='Compensatory_off_Request'),

    path('daily_attendence/', daily_attendence, name='daily_attendence'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)