
from django.urls import path
from .views import Index

urlpatterns = [
    path('1/', Index.as_view(), name="text" ),
    
]
