from django.urls import path
from My_Admin import views
app_name='App_Admin'
urlpatterns = [

    path('ajax/load-districts/', views.load_district, name='ajax_load_district'),
    path('ajax/load-sub-districts/', views.load_sub_district, name='ajax_load_sub_district'),
    path('', views.Dashboard, name='dashboard'),
    path('superadmin-login', views.SuperadminLogin, name="superadmin_login"),
    path('superadmin-logout', views.SuperadminLogout, name="superadmin_logout"),

    path('division-page',views.Divisionmanagement,name='division_page'),
    path('division-delete',views.DivisionDelete,name='division_delete'),
    path('division-update/<int:id>',views.DivisionUpdate,name='division_update'),

    path('district-page',views.Districtmanagement,name='district_page'),
    path('district-delete',views.DistrictDelete,name='district_delete'),
    path('district-update/<int:id>',views.DistrictUpdate,name='district_update'),

    path('sub_district-page', views.Sub_Districtmanagement, name='sub_district_page'),
    path('sub_district-delete', views.Sub_DistrictDelete, name='sub_district_delete'),
    path('sub_district-update/<int:id>', views.Sub_DistrictUpdate, name='sub_district_update'),

    path('tourist-place', views.TouristPlacesview, name='tourist_place'),
    path('add-place', views.Add_Touristplaceview, name='add_place'),
    path('delete-place', views.Delete_Touristplaceview, name='delete_place'),
    path('update-place/<int:id>', views.Touristplaceupdate, name='update_tourist'),

    path('top-rated-place', views.TopratedPlacesview, name='top_rated_place'),
    path('add-top-rated-place', views.Add_Topratedplace, name='add_top_rated_place'),
    path('delete-top-rated-place', views.Delete_Topratedplace, name='delete_top_rated_place'),
    path('update-top-rated-place/<int:id>', views.Topratedplaceupdate, name='update_toprated_place'),

    path('place-order', views.Placeorderview, name='place_order_view'),
    path('delete-place-order', views.Delete_placeorder, name='delete_place_order'),
    path('update-place-order/<int:id>', views.Update_placeorder, name='update_place_order'),

    path('toprated-place-order', views.Topratedplaceorderview, name='top_rated_place_order_view'),
    path('toprated-delete-place-order', views.Delete_topratedplaceorder, name='delete_toprated_place_order'),
    path('toprated-update-place-order/<int:id>', views.Update_topratedplaceorder, name='update_toprated_place_order'),


    path('hotel-manage', views.Hotelmanage, name='manage_hotel'),
    path('delete-hotel', views.Delete_Hotel, name='delete_hotel'),
    path('update-hotel/<int:id>', views.Update_Hotel, name='update_hotel'),

    path('food-manage', views.Foodmanage, name='manage_food'),
    path('delete-food', views.Delete_Food, name='delete_food'),
    path('update-food/<int:id>', views.Update_Food, name='update_food'),

    path('nearest-place-manage', views.Nearestplacemanage, name='manage_nearest_place'),
    path('delete-nearest-place', views.Delete_Nearest_place, name='delete_nearest_place'),
    path('update-nearest-place/<int:id>', views.Update_Nearest_place, name='update_nearest_place'),

    path('view-guider', views.Guiderview, name='view_guider'),
    path('add-guider', views.Add_Guider, name='add_guider'),
    path('delete-guider', views.Delete_Guider, name='delete_guider'),
    path('update-guider/<int:id>', views.Update_Guider, name='update_guider'),

    path('view-hireguider', views.Hireguiderview, name='view_hireguider'),
    path('delete-hireguider', views.Delete_Hireguider, name='delete_hireguider'),
    path('update-hireguider/<int:id>', views.Update_Hireguider, name='update_hireguider'),

    path('user-profile/<int:id>',views.Userprofile,name='user_profile'),

]
