from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import PersonInfoView, TokenView

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('person/', PersonInfoView.as_view()),
    path('token/', TokenView.as_view())
]

# hello/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NzEyOTU3LCJpYXQiOjE2ODU3MTI2NTcsImp0aSI6ImJiZGE4ODhiNzIwMTRlMjViZTUzMWEwY2I0NTUyNTRjIiwidXNlcl9pZCI6MX0.6ocC_2X_tyYG-XrYkCkUetoQWbdznNfyD1r1eLz2-hE"