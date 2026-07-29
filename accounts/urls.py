from django.urls import path
from .views import RegisterView, MeView
from .views import ProfileView, ChangePasswordView


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
    path('profile/', ProfileView.as_view()),
    
]

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg0OTk4MjQ3LCJpYXQiOjE3ODQ5OTQ2NDcsImp0aSI6IjgzY2U1YjU4MzYwYzQzZjM4YmJiMTY1YmYzNjlmMzE5IiwidXNlcl9pZCI6IjEifQ.SxVhrYYyhgJ-fWY42ieTMWbfQp6zWSn4OxbenqUPdhEcd backend