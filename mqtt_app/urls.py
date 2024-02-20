from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publish/', views.publish_message, name='publish'),
    path('get-all-topics/', views.get_all_topics, name='get-all-topics'),
    path('data/<str:topic>/<str:qos>/<str:content_hex>/', views.show_data)
]