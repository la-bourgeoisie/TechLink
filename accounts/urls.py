from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import(
    LoginView,
    RegisterView,
    UserProfileView,
)
from accounts.models import CustomUser

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('registrar/', RegisterView.as_view(), name='register'),
    path('usuario/me', UserProfileView.as_view(), name='user_profile'),
    path('usuario/<int:pk>', UserProfileView.as_view(), name='user_profile'),
]