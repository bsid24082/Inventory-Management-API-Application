from django.contrib import admin
from django.urls import path
from inventory_api.views import ItemDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/<str:name>/', ItemDetails.as_view(), name='item_details'),
]

