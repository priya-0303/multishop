from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('detail/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/', views.carts,name='cart'),
    path('add-cart/<int:pid>', views.add_cart,name='add_cart'),
    path('plus-cart/<int:cid>',views.plus_cart,name='plus_cart'),
    path('minus-cart/<int:cid>',views.minus_cart,name='minus_cart'),
    path('confirmorder/<int:oid>', views.confirmorder,name='confirmorder'),
    path('myorders/', views.myorders,name='myorders'),
    path('delete-cart/<int:cid>', views.delete_cart,name='delete_cart'),
    path('contact/',views.contact_us,name='contact.html'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('catagory/<int:id>', views.cat_prod,name='cat_prod'),
    path('search/', views.search,name='search'),

    # for forgot password ##

    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    
   
   
]

