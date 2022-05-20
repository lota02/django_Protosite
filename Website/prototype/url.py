from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("about us/",views.about,name="about"),
    path("feedback/",views.feedback,name="feedback"),
    path("contact/",views.contact,name="contact"),
]