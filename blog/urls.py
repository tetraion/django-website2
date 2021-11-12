from django.urls import path

from . import views
from .admin import mypage_site

urlpatterns = [
    path('', views.Index.as_view(), name="blog"),
    
    # <pk>にPostのIDを渡すと表示される。
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>/', views.Update.as_view(), name="update"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),
    
    path('mypage/', mypage_site.urls),

]
