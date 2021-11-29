from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('controllers/', views.controller, name='controllers'),
    path('items/', views.items, name='items'),
    path('add_controller/', views.add_controller, name='add_controller'),
    path('add_items/', views.add_items, name='add_item'),
    path('controllers/<int:pk>', views.ControllerDetailsView.as_view(), name='controller_detail'),
    path('items/<int:pk>', views.ItemsDetailsView.as_view(), name='item_detail'),
    path('controllers/<int:pk>/update', views.ControllerUpdateView.as_view(), name='controller_update'),
    path('items/<int:pk>/update', views.ItemsUpdateView.as_view(), name='item_update'),
    path('controllers/<int:pk>/delete', views.ControllerDeleteView.as_view(), name='controller_delete'),
    path('items/<int:pk>/delete', views.ItemsDeleteView.as_view(), name='item_delete'),
    path('registration/', views.register_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]