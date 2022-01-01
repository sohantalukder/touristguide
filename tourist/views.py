import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from event.models import AdminTouristEvent, UserTouristEvent, PaymentDetails
from places.forms import OrderForm, TOpOrderForm
from places.models import *
import json
from tourist.models import guider,hireguider,Feedback
from tourist.models import Ratting as Rat,Contactus,Subscriber
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def get_ratting_order(guider_list):
    dict={}
    all=[]
    for g in guider_list:
        if g.get_ratting_float != 0:
            dict[g.id] = g.get_ratting_float()
    x=sorted(dict.items(), key=lambda item: item[1],reverse=True)
    x=list(x)
    for i in x:
        all.append(i[0])
    return all
def homePage(request):
    template_name = 'index.html'
    context ={}
    events = AdminTouristEvent.objects.all().filter(publish='Accept')
    # user_events = UserTouristEvent.objects.all()
    latest_event = AdminTouristEvent.objects.filter(publish='Accept').order_by('-id')[:1]
    last_ten_in_ascending_order = reversed(latest_event)
    all_district=District.objects.all().order_by("name")
    top_rated_place=Topratedplace.objects.all().order_by("-id")
    guider_list = guider.objects.all().order_by("-id")
    contact_msg = Contactus.objects.filter(status=True).order_by("-id")
    print (contact_msg)
    all=get_ratting_order(guider_list)
    guider_=[]
    for i in all:
        guider_.append(guider.objects.get(id=i))
    context = {
        'events':events,
        # 'user_events':user_events,
        'latest_event':last_ten_in_ascending_order,
        'all_district':all_district,
        'top_rated_place':top_rated_place,
        'districts':District.objects.all().order_by("name"),
        'guiders':guider_,
        'contact_msg':contact_msg,
    }
    return render(request, template_name,context)


def is_valid_queryparam(param):
    return param != '' and param is not None

def search_view(request):
    map_def="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3746984.585555884!2d88.09996593838902!3d23.490578837072032!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30adaaed80e18ba7%3A0xf2d28e0c4e1fc6b!2sBangladesh!5e0!3m2!1sen!2sbd!4v1639504662575!5m2!1sen!2sbd"
    query=request.GET.get('query').capitalize()
    min_price=request.GET.get('min_price')
    max_price=request.GET.get('max_price')
    rated=request.GET.get('rated')
    hotel=request.GET.get('hotel')
    places = TouristPlaces.objects.all()
    places = places.filter(
        Q(district__name__exact=query)|
        Q(division__name__exact=query)
    )
    if is_valid_queryparam(min_price):
        places = places.filter(price__gte=min_price)
    if is_valid_queryparam(max_price):
        places = places.filter(price__lte=max_price)
    if rated:
        qq=[]
        for q in places:
            if q.count_total_ratting()>0:
                qq.append(q.id)
        places=places.filter(pk__in=qq)

    try:
        get_map=District.objects.get(name__exact=query)
        get_map=get_map.map_url
    except:
        get_map=map_def
    context={
        'places':places,
        'map_loc':get_map,
    }
    # return render(request,'place/Destination.html',context)
    return render(request,'search_places.html',context)

@login_required(login_url='signin')
def place_details(request,id):
    try:
        my_place=TouristPlaces.objects.get(id=id)
        print (my_place)
        my_hotel=Hotels.objects.filter(sub_district=my_place.sub_district)
        my_nearest=NearestPlace.objects.filter(sub_district=my_place.sub_district)
        my_food=FamousFood.objects.filter(sub_district=my_place.sub_district)
        related=TouristPlaces.objects.filter(district=my_place.district).exclude(place_name=my_place.place_name)
    except:
        return redirect('home')

    if Ratting.objects.filter(place=my_place, user=request.user).exists():
        my_ratting = Ratting.objects.get(place=my_place, user=request.user)
    else:
        my_ratting={'score':0}

    if request.method=="POST":
        form=OrderForm(request.POST or None)
        if form.is_valid():
            ord=form.save(commit=False)
            user=request.user
            place=TouristPlaces.objects.get(id=id)
            ord.user=user
            ord.place=place
            ord.save()
            print (ord)
            return redirect(ord.get_absolute_url())
    else:
        form=OrderForm()
    context={
        'my_place':my_place,
        'my_hotel':my_hotel,
        'my_nearest':my_nearest,
        'my_food':my_food,
        'related':related,
        'my_ratting':my_ratting,
        'form':form,
    }
    return render(request,'full-view-guiders.html',context)

@login_required(login_url='signin')
def AddRating(request):
    body = json.loads(request.body)
    print('BODY', body)
    rating_value=body['rating']
    print (rating_value)
    id=body['placeId']
    print (id)
    my_place=TouristPlaces.objects.get(id=id)
    if Ratting.objects.filter(place=my_place, user=request.user).exists():
        my_ratting = Ratting.objects.get(place=my_place, user=request.user)
        my_ratting.score=rating_value
        my_ratting.save()
        print("old user")
    else:
        new_user=Ratting.objects.create(
            place=my_place,user=request.user,score=rating_value
        )
        new_user.save()
        print ("new user")
    return HttpResponse("done")


def single_place(request,id):
    places=TouristPlaces.objects.filter(district_id=id)
    min_price=request.GET.get('min_price')
    max_price=request.GET.get('max_price')
    rated=request.GET.get('rated')
    if is_valid_queryparam(min_price):
        places = places.filter(price__gte=min_price)
    if is_valid_queryparam(max_price):
        places = places.filter(price__lte=max_price)
    if rated:
        qq=[]
        for q in places:
            if q.count_total_ratting()>0:
                qq.append(q.id)
        places=places.filter(pk__in=qq)

    context={
        'all_place':places,
    }
    return render(request,'desintaion-full.html',context)


@login_required(login_url='signin')
def place_requriement(request,id):
    store_id = 'pecel616d784f482e9'
    store_password = 'pecel616d784f482e9@ssl'
    payment_status_url = request.build_absolute_uri(reverse("place_payment_status"))
    my_order=Placeorder.objects.get(id=id)
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)
    mypayment.set_urls(success_url=payment_status_url, fail_url='http://127.0.0.1:8000/place-failed/',
                       cancel_url='http://127.0.0.1:8000/place-cancel/', ipn_url=payment_status_url)
    mypayment.set_product_integration(total_amount=Decimal(my_order.place.price), currency='BDT',
                                      product_category='Mixed ', product_name='doctor', num_of_item=1,
                                      shipping_method='YES', product_profile='None')
    mypayment.set_customer_info(name="TUtul", email="user@email", address1='demo address',
                                address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh',
                                phone='01711111111')
    mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209',
                                country='Bangladesh')
    response_data = mypayment.init_payment()
    my_order.transaction_id = response_data.get('sessionkey')
    my_order.ammount = my_order.place.price
    my_order.save()
    return redirect(response_data['GatewayPageURL'])

@csrf_exempt
def place_payment_status(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request, "Your Payment Completed Successfully! Page will be redirected!")
            return HttpResponseRedirect(reverse("completepurchase_place", kwargs={'val_id': val_id, 'tran_id': tran_id}, ))
        elif status == 'FAILED':
            messages.warning(request, "Your Payment Failed! Please Try Again! Page will be redirected!")

    return render(request, "payment/complete.html", context={})

@login_required
def completepurchase(request, val_id, tran_id):
    my_ord=Placeorder.objects.filter(user=request.user,ordered=False).order_by("-id")
    my_ord=my_ord[0]
    my_ord.transaction_id=tran_id
    my_ord.ordered=True
    my_ord.save()
    return redirect('place_success')

@csrf_exempt
def place_success(request):
    print("yes")
    return render(request,'payment/succes.html')

@csrf_exempt
def place_failed(request):
    return render(request,'payment/unsecces.html')

@csrf_exempt
def place_cancel(request):
    return render(request,'payment/cancel.html')

@login_required(login_url='signin')
def topdatedplacedetails(request,id):
    try:
        my_place=Topratedplace.objects.get(id=id)
        related = Topratedplace.objects.all().exclude(id=id).order_by("-id")
        my_hotel = Hotels.objects.filter(sub_district=my_place.sub_district)
        my_nearest = NearestPlace.objects.filter(sub_district=my_place.sub_district)
        my_food = FamousFood.objects.filter(sub_district=my_place.sub_district)
    except:
        return redirect('home')
    if request.method=="POST":
        form=TOpOrderForm(request.POST or None)
        if form.is_valid():
            ord=form.save(commit=False)
            user=request.user
            place=Topratedplace.objects.get(id=id)
            ord.user=user
            ord.place=place
            ord.save()
            print (ord)
            return redirect(ord.get_absolute_url())
    else:
        form=TOpOrderForm()
    context={
        'my_place':my_place,
        'related':related[:4],
        'my_hotel': my_hotel,
        'my_nearest': my_nearest,
        'my_food': my_food,
        'form':form,
    }
    return render(request,'topratedplace_details.html',context)


def payment(request,id):
    store_id = 'pecel616d784f482e9'
    store_password = 'pecel616d784f482e9@ssl'
    my_ord=TopPlaceorder.objects.get(id=id)
    payment_status_url = request.build_absolute_uri(reverse("complete"))
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)
    mypayment.set_urls(success_url=payment_status_url, fail_url='http://127.0.0.1:8000/place-failed/',
                       cancel_url='http://127.0.0.1:8000/place-cancel/', ipn_url=payment_status_url)
    mypayment.set_product_integration(total_amount=Decimal(my_ord.place.price), currency='BDT',
                                      product_category='Mixed ', product_name='doctor', num_of_item=1,
                                      shipping_method='YES', product_profile='None')
    mypayment.set_customer_info(name="TUtul", email="user@email", address1='demo address',
                                address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh',
                                phone='01711111111')
    mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209',
                                country='Bangladesh')
    response_data = mypayment.init_payment()
    my_ord.transaction_id = response_data.get('sessionkey')
    my_ord.ammount=my_ord.place.price
    my_ord.save()
    return redirect(response_data['GatewayPageURL'])

@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,"Your Payment Completed Successfully! Page will be redirected!")
            return HttpResponseRedirect(reverse("purchase", kwargs={'val_id':val_id, 'tran_id':tran_id},))
        elif status == 'FAILED':
            messages.warning(request, "Your Payment Failed! Please Try Again! Page will be redirected!")

    return render(request, "payment/complete.html", context={})

@login_required
def purchase(request, val_id, tran_id):
    my_ord=TopPlaceorder.objects.filter(user=request.user,ordered=False).order_by("-id")
    my_ord=my_ord[0]
    my_ord.transaction_id=tran_id
    my_ord.ordered=True
    my_ord.save()
    return redirect('place_success')




def guider_view(request):
    try:
        guider_list=guider.objects.all().order_by("-id")
        query = request.GET.get('q')
        print (query)
        if query:
            guider_list = guider_list.filter(
                Q(name__icontains=query)|
                Q(details__icontains=query) |
                Q(designation__icontains=query)
            ).distinct()
        page = request.GET.get('page', 1)

        paginator = Paginator(guider_list, 6)
        try:
            guider_list = paginator.page(page)
        except PageNotAnInteger:
            guider_list = paginator.page(1)
        except EmptyPage:
            guider_list = paginator.page(paginator.num_pages)
    except:
        return HttpResponse("Something went wrong")
    context={
        'guiders':guider_list,
    }
    return render(request,'guider-hirer.html',context)


@login_required(login_url='signin')
def guider_details(request,id):
    try:
        single_guider=guider.objects.get(id=id)
        if Rat.objects.filter(user=request.user,name=single_guider).exists():
            my_ratting=Rat.objects.filter(user=request.user,name=single_guider).order_by("-id")
            my_ratting=my_ratting[0]
        else:
            my_ratting=None
    except:
        return redirect('home')
    if request.method == 'POST':
        time = request.POST['hour_select']
        guid = hireguider.objects.create(
            guider_name=single_guider, user=request.user, hour=time, ammount=int(time) * single_guider.hourly_rate
        )
        guid.save()
        return redirect(guid.get_absolute_url())
    context={
        'single_guider':single_guider,
        'my_ratting':my_ratting
    }
    return render(request,'guider-hire.html',context)

def guider_ratting(request):
    body = json.loads(request.body)
    rating_value = body['rating']
    id = body['placeId']

    print (rating_value)
    print (id)
    my_name = guider.objects.get(id=id)
    print (my_name)
    if Rat.objects.filter(name=my_name, user=request.user).exists():
        my_ratting = Rat.objects.get(name=my_name, user=request.user)
        my_ratting.score = rating_value
        my_ratting.save()
        print("old user")
    else:
        new_user = Rat.objects.create(
            name=my_name, user=request.user, score=rating_value
        )
        new_user.save()
        print ("new user")
    return HttpResponse("done")

def guider_payment(request,id):
    store_id = 'pecel616d784f482e9'
    store_password = 'pecel616d784f482e9@ssl'
    my_ord = hireguider.objects.get(id=id)
    payment_status_url = request.build_absolute_uri(reverse("guider_complete"))
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)
    mypayment.set_urls(success_url=payment_status_url, fail_url='http://127.0.0.1:8000/place-failed/',
                       cancel_url='http://127.0.0.1:8000/place-cancel/', ipn_url=payment_status_url)
    mypayment.set_product_integration(total_amount=Decimal(my_ord.ammount), currency='BDT',
                                      product_category='Mixed ', product_name='doctor', num_of_item=1,
                                      shipping_method='YES', product_profile='None')
    mypayment.set_customer_info(name="TUtul", email="user@email", address1='demo address',
                                address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh',
                                phone='01711111111')
    mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209',
                                country='Bangladesh')
    response_data = mypayment.init_payment()
    my_ord.transaction_id = response_data.get('sessionkey')
    my_ord.save()
    return redirect(response_data['GatewayPageURL'])

@csrf_exempt
def guider_complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,"Your Payment Completed Successfully! Page will be redirected!")
            return HttpResponseRedirect(reverse("guidercompletepurchase", kwargs={'val_id':val_id, 'tran_id':tran_id},))
        elif status == 'FAILED':
            messages.warning(request, "Your Payment Failed! Please Try Again! Page will be redirected!")

    return render(request, "payment/complete.html", context={})

def guidercompletepurchase(request,val_id, tran_id):
    my_ord=hireguider.objects.filter(user=request.user,ordered=False).order_by("-id")
    print (my_ord)
    my_ord=my_ord[0]
    my_ord.transaction_id=tran_id
    my_ord.ordered=True
    my_ord.save()
    return redirect('place_success')

@login_required(login_url='signin')
def feedbackview(request):
    if request.method=="POST":
        expi=request.POST.get('exp')
        cats=request.POST.get('gender')
        priv=request.POST.get('privacy')
        img=request.FILES['imagw_file']
        feed=Feedback.objects.create(
            name=request.user,
            category=cats,
            experience=expi,
            privacy=priv,
            image=img
        )
        feed.save()
        if priv=="Share Experience":
            feed.status=True
            feed.save()
        messages.success(request,"Feedback saved successfully",extra_tags='feedback')
        return redirect('feedback')
    return render(request,'feedback.html')


@login_required(login_url='signin')
def galleryview(request):
    all_feedback=Feedback.objects.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(all_feedback, 8)
    try:
        all_feedback = paginator.page(page)
    except PageNotAnInteger:
        all_feedback = paginator.page(1)
    except EmptyPage:
        all_feedback = paginator.page(paginator.num_pages)
    context={
        'all_feedback':all_feedback,
    }
    return render(request, 'Gallery.html',context)


def love_view(request,id):
    scope = get_object_or_404(Feedback, id=id)
    if scope.love.filter(id=request.user.id).exists():
        scope.love.remove(request.user)
    else:
        scope.love.add(request.user)
    return redirect('gallery')

def love_view_event(request,id):
    scope = get_object_or_404(Feedback, id=id)
    if scope.love.filter(id=request.user.id).exists():
        scope.love.remove(request.user)
    else:
        scope.love.add(request.user)
    return redirect('profile')


def Faq_view(request):
    return render(request,'FAQ.html')
def Aboutus_view(request):
    return render(request,'About-us.html')
def Conditions_view(request):
    return render(request,'Trems-conditions.html')

def Howtouse_view(request):
    return render(request,'howtouse.html')
def Contractus_view(request):
    if request.method=="POST":
        name=request.POST.get('your_name')
        email=request.POST.get('your_email')
        msg=request.POST.get('your_message')
        mg=Contactus.objects.create(
            name=name,email=email,message=msg
        )
        mg.save()
        messages.success(request,'your message is send',extra_tags='contact')
        return redirect('contact')
    return render(request,'contact-us.html')



def join_email_view(request):
    if request.method=="POST":
        ema=request.POST.get('emal')
        sub=Subscriber.objects.create(
            email=ema
        )
        sub.save()
        return redirect('home')
    return redirect('home')


def destination_view(request):
    places = TouristPlaces.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    rated = request.GET.get('rated')
    if is_valid_queryparam(min_price):
        places = places.filter(price__gte=min_price)
    if is_valid_queryparam(max_price):
        places = places.filter(price__lte=max_price)
    if rated:
        qq = []
        for q in places:
            if q.count_total_ratting() > 0:
                qq.append(q.id)
        places = places.filter(pk__in=qq)
    page = request.GET.get('page', 1)
    paginator = Paginator(places, 6)
    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages)
    context = {
        'all_place': places,
    }
    return render(request, 'desintaion-full.html', context)