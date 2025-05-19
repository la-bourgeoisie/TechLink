from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', 'accounts.views.login', name='login'),
    path('logout/', 'accounts.views.logout', name='logout'),
    path('register/', 'accounts.views.register', name='register'),
    path('profile/', 'accounts.views.profile', name='profile'),
    path('password_change/', 'accounts.views.password_change', name='password_change'),
    path('password_reset/', 'accounts.views.password_reset', name='password_reset'),
]