from django.urls import path
from .views import LoginPage, DoctorsPage, ModerationPage, ServicesPage, VisitsPage, HelpPage

urlpatterns = [
    path('panel/login', LoginPage.as_view(), name='login'),
    path('panel/doctors', DoctorsPage.as_view(), name='doctors'),
    path('panel/moderation', ModerationPage.as_view(), name='mod'),
    path('panel/services', ServicesPage.as_view(), name='services'),
    path('panel/visits', VisitsPage.as_view(), name='visits'),
    path('panel/help', HelpPage.as_view(), name='help'),
]