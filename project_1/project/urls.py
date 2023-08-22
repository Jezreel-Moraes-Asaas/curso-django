from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def dashboard(request):
    return HttpResponse("dashboard")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard),
]
