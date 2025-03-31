from django.urls import path
from .views import *



app_name = 'emergency'

urlpatterns = [
    

    path("add/", add_contact_view, name="add_contact"),
    path("list/", list_contacts_view, name="list_contacts"),
    path("delete/<int:contact_id>/", delete_contact_view, name="delete_contact"),
    path("update/<int:contact_id>/", update_contact_view, name="update_contact"),
]