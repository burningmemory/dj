from django.urls import path

from .views import SignUpView, UsersListView

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', UsersListView.as_view(), name='ulist')
]