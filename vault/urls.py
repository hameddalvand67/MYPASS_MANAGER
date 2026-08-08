from django.urls import path
from . import views

app_name = "vault"

urlpatterns = [
    path("", views.entry_list, name="entry_list"),
    path("item/<int:pk>/", views.entry_detail, name="entry_detail"),
]
