from django.urls import path

from pets import views

app_name = 'pets'

urlpatterns = [
    path('', views.home, name='home'),
    # cart urls segment
    path('product_list/', views.product_list, name='product_list'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.view_cart, name='view_cart'),

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # payment urls
    path('payment/<int:amount>/', views.payment, name='payment'),
    # user urls segment
    path('profile/', views.client_profile, name='client_profile'),
    path('<int:pk>/', views.client_details, name='client_details'),
    path('<int:pk>/edit/', views.edit_profile, name='edit_profile'),
    path('<int:pk>/delete/', views.delete_profile, name='delete_profile'),

]
