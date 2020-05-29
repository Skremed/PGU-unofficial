import sys
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import views, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# Create your views here.
class LoginTemplateView(TemplateView):
    template_name = 'login/login.html'


class UserView(views.APIView):
    """View for login"""

    def get(self, request):
        user = request.query_params.get("user")
        password = request.query_params.get("password")
        resp = Response()
        if not user or not password:
            resp.status_code = 400
            return resp

        from scraper import scrape
        status = scrape.loginSite([user, password])

        if status:
            resp.status_code = 200
        else:
            resp.status_code = 400
        resp.data = [user, password]
        return resp
