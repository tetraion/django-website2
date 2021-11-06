from django.urls import path, include


from .views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('text_edit/', include("text_edit.urls")),
]
