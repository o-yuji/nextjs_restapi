from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskListView,TaskRetrieveView,TaskViewSet,PostListView,PostRetrieveView,CreateUserView

router = DefaultRouter()
router.register('tasks',TaskViewSet,basename='tasks')

urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/',TaskRetrieveView.as_view(),name='detail-task'),
    path('register/',CreateUserView.as_view(),name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('',include(router.urls)),
]