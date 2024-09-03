
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/',views.Hpage,name='home_page'),
    path('',views.Index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('cart/cartsave/',views.Cartsave,name='cartsave'),

    
    #add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    #contact page
    path('contact_us/',views.Contact_page, name="contact_page"),
    
    # checkout page
    # path('checkout/',views.Checkout,name='checkout'),
    
    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
