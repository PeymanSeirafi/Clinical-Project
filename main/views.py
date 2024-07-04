from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

# Admin Pages

# class PanelViewSet(ViewSet):

class LoginPage(APIView):
    def get(self, request):
        return Response(template_name='admin-panel/admin-login.html')

class DoctorsPage(APIView):
    def get(self, request):
        return Response(template_name='admin-panel/admin-doctors.html')

class ModerationPage(APIView):
    def get(self, request):
        return Response(template_name='admin-panel/admin-moderation.html')

class ServicesPage(APIView):
    def get(self, request):
        return Response(template_name='admin-panel/admin-services.html')

class VisitsPage(APIView):
    def get(self, request):
        return Response(template_name='admin-panel/admin-visits.html')

class HelpPage(APIView):
    def get(self, request):
        return Response(template_name='admin-panel/help.html')