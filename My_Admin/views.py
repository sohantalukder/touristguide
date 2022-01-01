from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect , HttpResponse
from My_Admin.forms import *
from tourist.models import guider,hireguider

@login_required(login_url='App_Admin:superadmin_login')
def Dashboard(request):
    if request.user.is_superuser:
        all_user=User.objects.all()
        all_guider=guider.objects.all()
        all_place_order=Placeorder.objects.filter(ordered=True)
        all_top_place_order=TopPlaceorder.objects.filter(ordered=True)
        all_guider_order=hireguider.objects.filter(ordered=True)
        context={
            'all_user':all_user,
            'all_guider':all_guider,
            'all_place_order':all_place_order,
            'all_top_place_order':all_top_place_order,
            'all_guider_order':all_guider_order,
        }
        return render(request, 'App_Admin/index.html',context)
    else:
        return redirect('home')


def SuperadminLogin(request):
    if request.user.is_authenticated:
        return redirect('App_Admin:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('App_Admin:dashboard')
            else:
                messages.info(request, "Enter correct username and password", extra_tags="login")
                return redirect('App_Admin:superadmin_login')

        else:
            return render(request, 'App_Admin/login.html')


def SuperadminLogout(request):
    logout(request)
    return redirect('App_Admin:superadmin_login')


def Divisionmanagement(request):
    division_data=Division.objects.all().order_by("-id")
    if request.user.is_superuser:
        if request.method=="POST":
            form=DivisionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Division Saved successfully",extra_tags="division_add")
                return redirect(request.POST['next'])
        else:
            form=DivisionForm()
        context={
            'form':form,
            'division_data':division_data,
        }
        return render(request,'App_Admin/division.html',context)
    else:
        return redirect('home')


def DivisionDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['division_delc']
            single_data = Division.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Division Deleted Successfully", extra_tags="division_delete")
            return redirect('App_Admin:division_page')
        except:
            return redirect('App_Admin:division_page')
    else:
        return redirect('home')


def DivisionUpdate(request,id):
    if request.user.is_superuser:
        try:

            single_division = Division.objects.get(id=id)
            if request.method == "POST":
                form = DivisionForm(request.POST or None, instance=single_division)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Division Update successfully',
                                     extra_tags='division_update')
                    return redirect('App_Admin:division_page')
            else:
                form = DivisionForm(instance=single_division)
        except:
            return redirect('App_Admin:division_page')

        context = {
            'form': form,
            'division_id': single_division,
            'division_data': Division.objects.all().order_by('-id'),
        }
        return render(request,'App_Admin/divisionupdate.html',context)
    else:
        return redirect('home')


def Districtmanagement(request):
    district_data = District.objects.all().order_by("-id")
    if request.user.is_superuser:
        if request.method == "POST":
            form = DistrictForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "District Saved successfully", extra_tags="district_add")
                return redirect(request.POST['next'])
        else:
            form = DistrictForm()
        context = {
            'form': form,
            'district_data': district_data,
        }
        return render(request, 'App_Admin/district.html', context)
    else:
        return redirect('home')

def DistrictDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['district_delc']
            single_data = District.objects.get(id=id)
            single_data.delete()
            messages.success(request, "District Deleted Successfully", extra_tags="district_delete")
            return redirect('App_Admin:district_page')
        except:
            return redirect('App_Admin:district_page')
    else:
        return redirect('home')


def DistrictUpdate(request,id):
    if request.user.is_superuser:
        try:

            single_district = District.objects.get(id=id)
            if request.method == "POST":
                form = DistrictForm(request.POST or None, instance=single_district)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'District Update successfully',
                                     extra_tags='district_update')
                    return redirect('App_Admin:district_page')
            else:
                form = DistrictForm(instance=single_district)
        except:
            return redirect('App_Admin:district_page')

        context = {
            'form': form,
            'division_id': single_district,
            'district_data': District.objects.all().order_by('-id'),
        }
        return render(request,'App_Admin/districtupdate.html',context)
    else:
        return redirect('home')

def Sub_Districtmanagement(request):
    subdistrict_data = Sub_District.objects.all().order_by("-id")
    if request.user.is_superuser:
        if request.method == "POST":
            form = Sub_DistrictForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Sub District Saved successfully", extra_tags="sub_district_add")
                return redirect(request.POST['next'])
        else:
            form = Sub_DistrictForm()
        context = {
            'form': form,
            'sub_district_data': subdistrict_data,
        }
        return render(request, 'App_Admin/sub_district.html', context)
    else:
        return redirect('home')


def Sub_DistrictDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['sub_district_delc']
            single_data = Sub_District.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Sub District Deleted Successfully", extra_tags="sub_district_delete")
            return redirect('App_Admin:sub_district_page')
        except:
            return redirect('App_Admin:sub_district_page')
    else:
        return redirect('home')


def Sub_DistrictUpdate(request,id):
    if request.user.is_superuser:
        try:

            single_sub_district = Sub_District.objects.get(id=id)
            if request.method == "POST":
                form = Sub_DistrictForm(request.POST or None, instance=single_sub_district)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Sub District Update successfully',
                                     extra_tags='sub_district_update')
                    return redirect('App_Admin:sub_district_page')
            else:
                form = Sub_DistrictForm(instance=single_sub_district)
        except:
            return redirect('App_Admin:sub_district_page')

        context = {
            'form': form,
            'division_id': single_sub_district,
            'sub_district_data': Sub_District.objects.all().order_by('-id'),
        }
        return render(request,'App_Admin/sub_districtupdate.html',context)
    else:
        return redirect('home')

def TouristPlacesview(request):
    if request.user.is_superuser:
        all_place=TouristPlaces.objects.all().order_by("-id")
        context = {
            'all_place': all_place,
        }
        return render(request, 'App_Admin/touristplace.html', context)
    else:
        return redirect('home')

def Add_Touristplaceview(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form=TouristPlaceForm(request.POST or None,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Tourist Place saved success",extra_tags="add_place")
                return redirect(request.POST['next'])
        else:
            form=TouristPlaceForm()
        context={
            'form':form,
        }
        return render(request, 'App_Admin/add_touristplace.html', context)
    else:
        return redirect('home')


def Touristplaceupdate(request,id):
    if request.user.is_superuser:
        single_place=TouristPlaces.objects.get(id=id)
        if request.method=="POST":
            form=TouristPlaceForm(request.POST or None,request.FILES,instance=single_place)
            if form.is_valid():
                form.save()
                messages.success(request,"Tourist Place update success",extra_tags="update_place")
                return redirect(request.POST['next'])
        else:
            form=TouristPlaceForm(instance=single_place)
        context={
            'form':form,
            'single_place':single_place,
        }
        return render(request, 'App_Admin/update_touristplace.html', context)
    else:
        return redirect('home')

def Delete_Touristplaceview(request):
    if request.user.is_superuser:
        try:
            id = request.POST['touristplace']
            single_data = TouristPlaces.objects.get(id=id)
            single_data.delete()
            print (single_data)
            messages.success(request, "Tourist Place Deleted Successfully", extra_tags="delete_place")
            return redirect('App_Admin:tourist_place')
        except:
            return redirect('App_Admin:tourist_place')
    else:
        return redirect('home')


def load_district(request):
    division_id = request.GET.get('division')
    districs = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'App_Admin/city_dropdown_list_options.html', {'districs': districs})

def load_sub_district(request):
    district_id = request.GET.get('district')
    sub_districs = Sub_District.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'App_Admin/sub_city_dropdown_list_option.html', {'sub_districs': sub_districs})


def TopratedPlacesview(request):
    if request.user.is_superuser:
        all_place=Topratedplace.objects.all().order_by("-id")
        context = {
            'all_place': all_place,
        }
        return render(request,'App_Admin/topratedplace.html',context)
    else:
        return redirect('home')



def Add_Topratedplace(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = TopratedplaceForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Top Rated Place saved success", extra_tags="add_place")
                return redirect(request.POST['next'])
        else:
            form = TopratedplaceForm()
        context = {
            'form': form,
        }
        return render(request, 'App_Admin/add_topratedplace.html', context)
    else:
        return redirect('home')


def Delete_Topratedplace(request):
    if request.user.is_superuser:
        try:
            id = request.POST['topratedplace']
            single_data = Topratedplace.objects.get(id=id)
            single_data.delete()
            print (single_data)
            messages.success(request, "Top rated Place Deleted Successfully", extra_tags="delete_place")
            return redirect('App_Admin:top_rated_place')
        except:
            return redirect('App_Admin:top_rated_place')
    else:
        return redirect('home')


def Topratedplaceupdate(request,id):
    if request.user.is_superuser:
        single_place=Topratedplace.objects.get(id=id)
        if request.method == "POST":
            form = TopratedplaceForm(request.POST or None, request.FILES,instance=single_place)
            if form.is_valid():
                form.save()
                messages.success(request, "Top Rated Place update success", extra_tags="update_place")
                return redirect(request.POST['next'])
        else:
            form = TopratedplaceForm(instance=single_place)
        context = {
            'form': form,
        }
        return render(request, 'App_Admin/update_topratedplace.html', context)
    else:
        return redirect('home')


def Placeorderview(request):
    if request.user.is_superuser:
        all_place=Placeorder.objects.all().order_by("-id")
        context = {
            'all_place': all_place,
        }
        return render(request,'App_Admin/manage_placeorder.html',context)
    else:
        return redirect('home')

def Delete_placeorder(request):
    if request.user.is_superuser:
        try:
            id = request.POST['order_id']
            single_data = Placeorder.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Order Deleted Successfully", extra_tags="delete_order")
            return redirect('App_Admin:place_order_view')
        except:
            return redirect('App_Admin:place_order_view')
    else:
        return redirect('home')


def Update_placeorder(request,id):
    if request.user.is_superuser:
        single_place=Placeorder.objects.get(id=id)
        if request.method == "POST":
            form = PlaceorderForm(request.POST or None,instance=single_place)
            if form.is_valid():
                form.save()
                messages.success(request, "Order update success", extra_tags="update_place_order")
                return redirect(request.POST['next'])
        else:
            form = PlaceorderForm(instance=single_place)
        context = {
            'form': form,
            'single_place':single_place,
        }
        return render(request, 'App_Admin/update_placeorder.html', context)
    else:
        return redirect('home')



def Topratedplaceorderview(request):
    if request.user.is_superuser:
        all_place=TopPlaceorder.objects.all().order_by("-id")
        context = {
            'all_place': all_place,
        }
        return render(request,'App_Admin/manage_toprated_placeorder.html',context)
    else:
        return redirect('home')

def Delete_topratedplaceorder(request):
    if request.user.is_superuser:
        try:
            id = request.POST['topplace_order_id']
            single_data = TopPlaceorder.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Order Deleted Successfully", extra_tags="delete_order")
            return redirect('App_Admin:top_rated_place_order_view')
        except:
            return redirect('App_Admin:top_rated_place_order_view')
    else:
        return redirect('home')


def Update_topratedplaceorder(request,id):
    if request.user.is_superuser:
        single_place = TopPlaceorder.objects.get(id=id)
        if request.method == "POST":
            form = TopratedPlaceorderForm(request.POST or None, instance=single_place)
            if form.is_valid():
                form.save()
                messages.success(request, "Order update success", extra_tags="update_place_order")
                return redirect(request.POST['next'])
        else:
            form = TopratedPlaceorderForm(instance=single_place)
        context = {
            'form': form,
            'single_place': single_place,
        }
        return render(request, 'App_Admin/update_topratedplaceorder.html', context)
    else:
        return redirect('home')



def Hotelmanage(request):
    if request.user.is_superuser:
        all_hotel=Hotels.objects.all().order_by("-name")
        if request.method=="POST":
            form=HotelForms(request.POST or None,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Hotel saved success",extra_tags="add_hotel")
                return redirect(request.POST['next'])
        else:
            form=HotelForms()
        context = {
            'all_hotel': all_hotel,
            'form':form,
        }
        return render(request,'App_Admin/manage_hotel.html',context)
    else:
        return redirect('home')

def Update_Hotel(request,id):
    if request.user.is_superuser:
        single_hotel = Hotels.objects.get(id=id)
        if request.method == "POST":
            form = HotelForms(request.POST or None, instance=single_hotel)
            if form.is_valid():
                form.save()
                messages.success(request, "Hotel update success", extra_tags="update_hotel")
                return redirect(request.POST['next'])
        else:
            form = HotelForms(instance=single_hotel)
        context = {
            'form': form,
            'single_hotel': single_hotel,
        }
        return render(request, 'App_Admin/update_hotel.html', context)
    else:
        return redirect('home')


def Delete_Hotel(request):
    if request.user.is_superuser:
        try:
            id = request.POST['hotel_id']
            single_data = Hotels.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Hotel Deleted Successfully", extra_tags="delete_hotel")
            return redirect('App_Admin:manage_hotel')
        except:
            return redirect('App_Admin:manage_hotel')
    else:
        return redirect('home')


def Foodmanage(request):
    if request.user.is_superuser:
        all_food=FamousFood.objects.all().order_by("-name")
        if request.method=="POST":
            form=FamousFoodForms(request.POST or None,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Food saved success",extra_tags="add_food")
                return redirect(request.POST['next'])
        else:
            form=FamousFoodForms()
        context = {
            'all_food': all_food,
            'form':form,
        }
        return render(request,'App_Admin/manage_famousfood.html',context)
    else:
        return redirect('home')


def Delete_Food(request):
    if request.user.is_superuser:
        try:
            id = request.POST['food_id']
            single_data = FamousFood.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Food Deleted Successfully", extra_tags="delete_food")
            return redirect('App_Admin:manage_food')
        except:
            return redirect('App_Admin:manage_food')
    else:
        return redirect('home')


def Update_Food(request,id):
    if request.user.is_superuser:
        single_food = FamousFood.objects.get(id=id)
        if request.method == "POST":
            form = FamousFoodForms(request.POST or None, instance=single_food)
            if form.is_valid():
                form.save()
                messages.success(request, "Food update success", extra_tags="update_food")
                return redirect(request.POST['next'])
        else:
            form = FamousFoodForms(instance=single_food)
        context = {
            'form': form,
            'single_food': single_food,
        }
        return render(request, 'App_Admin/update_food.html', context)
    else:
        return redirect('home')


def Nearestplacemanage(request):
    if request.user.is_superuser:
        all_place = NearestPlace.objects.all().order_by("-name")
        if request.method == "POST":
            form = NearestPlaceForms(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Nearest Place saved success", extra_tags="add_nearest_place")
                return redirect(request.POST['next'])
        else:
            form = NearestPlaceForms()
        context = {
            'all_place': all_place,
            'form': form,
        }
        return render(request, 'App_Admin/manage_nearestplace.html', context)
    else:
        return redirect('home')


def Delete_Nearest_place(request):
    if request.user.is_superuser:
        try:
            id = request.POST['nearest_place_id']
            single_data = NearestPlace.objects.get(id=id)
            single_data.delete()
            messages.success(request, "Place Deleted Successfully", extra_tags="delete_nearest_place")
            return redirect('App_Admin:manage_nearest_place')
        except:
            return redirect('App_Admin:manage_nearest_place')
    else:
        return redirect('home')


def Update_Nearest_place(request,id):
    if request.user.is_superuser:
        single_place = NearestPlace.objects.get(id=id)
        if request.method == "POST":
            form = NearestPlaceForms(request.POST or None, instance=single_place)
            if form.is_valid():
                form.save()
                messages.success(request, "Place update success", extra_tags="update_nearest_place")
                return redirect(request.POST['next'])
        else:
            form = NearestPlaceForms(instance=single_place)
        context = {
            'form': form,
            'single_place': single_place,
        }
        return render(request, 'App_Admin/update_nearest_place.html', context)
    else:
        return redirect('home')


def Guiderview(request):
    if request.user.is_superuser:
        all_guider=guider.objects.all().order_by("-name")
        context = {
            'all_guider': all_guider,
        }
        return render(request,'App_Admin/guiderview.html',context)
    else:
        return redirect('home')


def Add_Guider(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = guiderForm(request.POST or None,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "guider add successfully", extra_tags="add_guider")
                return redirect(request.POST['next'])
        else:
            form = guiderForm()
        context = {
            'form': form,
        }
        return render(request, 'App_Admin/add_guider.html', context)
    else:
        return redirect('home')


def Update_Guider(request,id):
    if request.user.is_superuser:
        single_guider=guider.objects.get(id=id)
        if request.method == "POST":
            form = guiderForm(request.POST or None,request.FILES,instance=single_guider)
            if form.is_valid():
                form.save()
                messages.success(request, "guider update successfully", extra_tags="update_guider")
                return redirect(request.POST['next'])
        else:
            form = guiderForm(instance=single_guider)
        context = {
            'form': form,
        }
        return render(request, 'App_Admin/update_guider.html', context)
    else:
        return redirect('home')


def Delete_Guider(request):
    if request.user.is_superuser:
        try:
            id = request.POST['guider_id']
            single_data = guider.objects.get(id=id)
            single_data.delete()
            messages.success(request, "guider Deleted Successfully", extra_tags="delete_guider")
            return redirect('App_Admin:view_guider')
        except:
            return redirect('App_Admin:view_guider')
    else:
        return redirect('home')


def Hireguiderview(request):
    if request.user.is_superuser:
        all_hireguider=hireguider.objects.all().order_by("-id")
        context = {
            'all_hireguider': all_hireguider,
        }
        return render(request,'App_Admin/hireguiderview.html',context)
    else:
        return redirect('home')


def Update_Hireguider(request,id):
    if request.user.is_superuser:
        single_guider = hireguider.objects.get(id=id)
        if request.method == "POST":
            form = hireguiderForm(request.POST or None,instance=single_guider)
            if form.is_valid():
                form.save()
                messages.success(request, "guider update successfully", extra_tags="update_hireguider")
                return redirect(request.POST['next'])
        else:
            form = hireguiderForm(instance=single_guider)
        context = {
            'form': form,
        }
        return render(request, 'App_Admin/update_hireguider.html', context)
    else:
        return redirect('home')


def Delete_Hireguider(request):
    if request.user.is_superuser:
        try:
            id = request.POST['hireguider_id']
            single_data = hireguider.objects.get(id=id)
            single_data.delete()
            messages.success(request, "hireguider Deleted Successfully", extra_tags="delete_hireguider")
            return redirect('App_Admin:view_hireguider')
        except:
            return redirect('App_Admin:view_hireguider')
    else:
        return redirect('home')


def Userprofile(request,id):
    user=User.objects.get(id=id)
    context={
        'user':user
    }
    return render(request,'App_Admin/userprofile.html',context)
