from django.urls import path
from .views import UserListView, UserDetailView, UserUpdateView, UserCreateView
urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'), # auth need
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'), #auth need and admin permissions needed
    path('create/', UserCreateView.as_view(), name='user-create'),  # auth need and admin permissions needed
]
