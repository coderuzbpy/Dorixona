from django.urls import path
from .views import \
    home, contact_form, DoriList, DoriDetail, DoriCreate, DoriUpdate, DoriDelete

urlpatterns = [
    path('', home, name='home'),
    path('dori-list/', DoriList.as_view(), name='dori-list'),
    path('dori/<int:pk>', DoriDetail.as_view(), name='dori-detail'),
    path('dori-create/', DoriCreate.as_view(), name='dori-create'),
    path('dori-update/<int:pk>/', DoriUpdate.as_view(), name='dori-update'),
    path('dori-delete/<int:pk>/', DoriDelete.as_view(), name='dori-delete'),
    path('contact/', contact_form, name='contact'),  # Add this line to your urls.py file.
]