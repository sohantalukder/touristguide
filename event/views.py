from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render,redirect

from account.models import User
from .models import EventInfo, UserTouristEvent,AdminTouristEvent
from .form import AdminTouristEventForm, ProfileForm
from .models import PaymentDetails,EventOrder
import requests
import socket
from django.urls import reverse
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
# Create your views here
from tourist.models import Feedback
def TouristEventView(request):
    if request.user.is_authenticated:
        template_name = 'event/Create-Event.html'
        context ={}
        
        if request.method=='POST':
            form = AdminTouristEventForm(request.POST or None, request.FILES)
            if form.is_valid():
                event_creator = request.user
                event_title  = form.cleaned_data['event_title']
                event_description  = form.cleaned_data['event_description']
                traveling_dates  = form.cleaned_data['traveling_dates']
                # total_traveling_person  = form.cleaned_data['total_traveling_person']
                traveling_location = form.cleaned_data['traveling_location']
                event_price = form.cleaned_data['event_price']
                # traveller_destination = form.cleaned_data['traveller_destination']
                guider_confirmation = form.cleaned_data['guider_confirmation']
                transport_service = form.cleaned_data['transport_service']
                event_image = request.FILES['event_image']
                data  = AdminTouristEvent(event_creator=event_creator,event_title=event_title,event_description=event_description,traveling_dates=traveling_dates,traveling_location=traveling_location,event_price=event_price,guider_confirmation=guider_confirmation,transport_service=transport_service,event_image=event_image)
                data.save()
                return redirect('profile')
        else:
            form = AdminTouristEventForm()
            context={
                'form': form
            }
        return render(request,template_name,context)
    else:
        return redirect('signin')


def event_profile_view(request):
    if request.user.is_authenticated:
        template_name = 'event\profile-event.html'
        events = AdminTouristEvent.objects.filter(event_creator=request.user)
        my_post=Feedback.objects.filter(name=request.user)
        context = {
            'events':events,
            'my_post':my_post,
            } 
        return render(request, template_name,context)
    else:
        return redirect('signin')

def edit_profile_view(request):
    if request.user.is_authenticated:
        template_name = 'event\edit-profile.html'
        user=User.objects.get(username=request.user)
        if request.method=="POST":
            form=ProfileForm(request.POST or None,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile Updated",extra_tags='profile_update')
                return redirect(request.POST['next'])
        else:
            form=ProfileForm(instance=user)

        return render(request, template_name,{'user':user,'form':form})
    else:
        return redirect('signin')

def event_requriement(request,id):
    if request.user.is_authenticated:
        template_name = 'event/event_requirement.html'
        context = {}
        event=AdminTouristEvent.objects.get(id=id)
        eveent=EventOrder.objects.create(
            event=event,user=request.user,ammount=event.event_price
        )
        eveent.save()
        data = EventInfo.objects.create(
            username=request.user.username,
            email= request.user.email,
            )
        return redirect(eveent.get_absolute_url())
    else:
        return redirect('signin')



def payment(request,id):
    if request.user.is_authenticated:
        user=EventOrder.objects.get(id=id)
        store_id = 'pecel616d784f482e9'
        store_password = 'pecel616d784f482e9@ssl'
        payment_status_url = request.build_absolute_uri(reverse("payment_complete"))

        print(payment_status_url)
        mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)

        mypayment.set_urls(success_url=payment_status_url, fail_url=payment_status_url, cancel_url=payment_status_url, ipn_url=payment_status_url)

        mypayment.set_product_integration(total_amount=Decimal(user.ammount), currency='BDT', product_category='Mixed ', product_name='doctor', num_of_item=1,
        shipping_method='YES', product_profile='None')

        mypayment.set_customer_info(name=user.user.name, email=user.user.email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

        mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')

        response_data = mypayment.init_payment()
        user.transaction_id = response_data.get('sessionkey')
        user.save()
        return redirect(response_data['GatewayPageURL'])
    return redirect('signin')

@csrf_exempt
def payment_complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,"Your Payment Completed Successfully! Page will be redirected!")
            return redirect(reverse("completepurchase", kwargs={'val_id':val_id, 'tran_id':tran_id},))
        elif status == 'FAILED':
            messages.warning(request, "Your Payment Failed! Please Try Again! Page will be redirected!")

    return render(request, "payment/complete.html", context={})

def get_eighty_percentage(val):
    return val*0.8
def completepurchase(request,val_id, tran_id):
    my_ord=EventOrder.objects.filter(user=request.user,ordered=False).order_by("-id")
    print (my_ord)
    my_ord=my_ord[0]
    my_ord.transaction_id=tran_id
    my_ord.ordered=True
    my_ord.save()
    event_user=User.objects.get(username=my_ord.event.event_creator)
    event_user.balance=event_user.balance+get_eighty_percentage(my_ord.event.event_price)
    event_user.save()
    return redirect('payment_status')


@csrf_exempt
def payment_status(request):
    return render(request,'payment/succes.html')

def event_status(request,id):
    event=AdminTouristEvent.objects.get(id=id)
    orders=EventOrder.objects.filter(event=event)
    context={
        'f':event,
        'orders':orders,
    }
    return render(request,'eventstatus.html',context)