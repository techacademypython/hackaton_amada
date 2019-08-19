from django.urls import path
from core.views import index, cordinates, notfication

urlpatterns = [
    path("", index, name="index"),
    path("cordinates/", cordinates, name="cordinates"),
    path("notfication/", notfication, name="notfication")
]
