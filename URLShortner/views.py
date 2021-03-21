from django.shortcuts import render, redirect
from .models import URLLink
from .serializers import URLSerializer
from django.views import View
from django.conf import settings
from rest_framework.generics import ListAPIView,CreateAPIView

# Create your views here.

class Shortener(ListAPIView):
    queryset = URLLink.objects.all()
    serializer_class = URLSerializer

class ShortenerCreate(CreateAPIView):
    
    serializer_class = URLSerializer
    print(serializer_class)

# To redirect the original page with new url
class Redirector(View):
    def get(self,request,shortener_url,*args, **kwargs):
        shortener_url=settings.HOST_URL+'/'+ self.kwargs['shortener_url']
        redirect_link=URLLink.objects.filter(shortened_url=shortener_url).first().original_url
        return redirect(redirect_link)