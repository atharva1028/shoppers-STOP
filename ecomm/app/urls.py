from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('', views.home),
    # path('product-detail/', views.product_detail, name='product-detail'),
    # path('cart/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('', views.ProductView.as_view(), name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
