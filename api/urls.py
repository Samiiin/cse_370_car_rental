from django.urls import path, include 
from . import views 

urlpatterns = [
    # Customer Dashboard
    path("free_cars/", views.free_cars, name="free_cars"), #get

    # Admin Dashboard
    path("all_cars/", views.all_cars, name="all_cars"), #get
    path("all_customers/", views.all_customers, name="all_customers"), #get 

    # Other Endpoints (authentication) 
    path("accounts/", include("django.contrib.auth.urls")),  # User Authentication URLs #get
    path("accounts/register/", views.register, name="register"),  # Custom registration URL 
    path("accounts/change_password/", views.change_password, name="change_password"),  # Custom change password URL
    path("accounts/reset_password/", views.reset_password, name="reset_password"),  # Custom reset password URL

    # Car Operations
    path("car/<int:car_id>/", views.view_car_details, name="view_car_details"), #get
    path("car/<int:car_id>/reserve/", views.reserve_car, name="reserve_car"), #post
    path("reservation/<int:reservation_id>/cancel/", views.cancel_reservation, name="cancel_reservation"), #post

    # Payment Operations
    path("reservation/<int:reservation_id>/make_payment/", views.make_payment, name="make_payment"), #post
    path("payments/", views.view_payment_history, name="view_payment_history"), #get
    path("payment/<int:payment_id>/", views.view_payment_details, name="view_payment_details"), #get

    # User Profile
    path("profile/", views.view_profile, name="view_profile"), 
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    # Reservation Management
    path("reservations/", views.view_reservations, name="view_reservations"), #get
    path("reservation/<int:reservation_id>/edit/", views.modify_reservation, name="modify_reservation"), #post 
    path("reservation/<int:reservation_id>/cancel/", views.cancel_reservation, name="cancel_reservation"), #post

    # Admin Operations
    path("admin/add_car/", views.add_car, name="add_car"), #post
    path("admin/edit_car/<int:car_id>/", views.edit_car_details, name="edit_car_details"), #post
    path("admin/delete_car/<int:car_id>/", views.delete_car, name="delete_car"), #post
    path("admin/all_reservations/", views.all_reservations_admin, name="all_reservations_admin"), #get
    path("admin/reservation/<int:reservation_id>/", views.view_reservation_admin, name="view_reservation_admin"), #get
    path("admin/all_payments/", views.all_payments_admin, name="all_payments_admin"), #get
    path("admin/payment/<int:payment_id>/", views.view_payment_admin, name="view_payment_admin"), #get
    path("admin/customer/<int:customer_id>/", views.view_customer_admin, name="view_customer_admin"), #get
]
