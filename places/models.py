from django.urls import reverse
from django.utils.datetime_safe import datetime
from tourist.models import Subscriber
from account.models import User
from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.core.mail import send_mail, EmailMessage
from django.dispatch import receiver


# Create your models here.

class Ratting(models.Model):
    place = models.ForeignKey(to="TouristPlaces", on_delete=models.CASCADE,related_name="place")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '{}-{}-{}'.format(self.place, self.user, self.score)


class Division(models.Model):
    name = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=30)
    map_url=models.TextField(default="",blank=True)

    def __str__(self):
        return self.name
    def get_place_count(self):
        return TouristPlaces.objects.filter(district=self).count()

class Sub_District(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.name


class TouristPlaces(models.Model):
    place_name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="places/", blank=False)
    ratting = models.ForeignKey(Ratting,null=True, blank=True,on_delete=models.CASCADE,related_name="ratting")
    price=models.IntegerField(default=200)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL, null=True)
    district=models.ForeignKey(District,on_delete=models.SET_NULL, null=True)
    sub_district=models.ForeignKey(Sub_District,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}-{}'.format(self.place_name,self.price)

    def count_total_ratting(self):
        return Ratting.objects.filter(place=self).count()

    def count_avg_ratting(self):
        n=Ratting.objects.filter(place=self)
        total_ratting=Ratting.objects.filter(place=self).count()
        avg=0.0
        if total_ratting>0:
            all_score=0
            for i in n:
                all_score=all_score+i.score
            print (all_score)
            avg=all_score/total_ratting
        return format(avg,".1f")

@receiver(post_save, sender=TouristPlaces)
def create_profile(sender, instance, created, **kwargs):
    if created:
        all_email=Subscriber.objects.all()
        all=[]
        for i in all_email:
            all.append(i.email)

        mail_subject ='New Place Added'
        message="Please check our new place that are now available in our website"
        email = EmailMessage(
            mail_subject, message, to=all
        )
        email.send()


class Hotels(models.Model):
    sub_district=models.ForeignKey(Sub_District,on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return '{}-{}'.format(self.name,self.sub_district)

class NearestPlace(models.Model):
    sub_district = models.ForeignKey(Sub_District, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return '{}-{}'.format(self.name,self.sub_district)

class FamousFood(models.Model):
    sub_district = models.ForeignKey(Sub_District, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return '{}-{}'.format(self.name,self.sub_district)

class Order(models.Model):
    place = models.ForeignKey(TouristPlaces, on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    person = models.IntegerField(default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=500,default="")
    ammount = models.FloatField(max_length=100,default=0.0)
    card_type = models.CharField(max_length=100,default="")
    payment_status = models.CharField(max_length=100,default="")
    transaction_date = models.CharField(max_length=100,default="")
    risk_title = models.CharField(max_length=100,default="")

    def __str__(self):
        return '{}'.format(self.user)

    def get_absolute_url(self):
        return reverse('place_requriementfile', kwargs={'id': self.id})

class Placeorder(models.Model):
    place = models.ForeignKey(TouristPlaces, on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    person = models.IntegerField(default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=500,default="")
    ammount = models.FloatField(max_length=100,default=0.0)
    card_type = models.CharField(max_length=100,default="",blank=True)
    payment_status = models.CharField(max_length=100,default="",blank=True)
    transaction_date = models.CharField(max_length=100,default="",blank=True)
    risk_title = models.CharField(max_length=100,default="",blank=True)


    def get_absolute_url(self):
        return reverse('place_requriementfile', kwargs={'id': self.id})


class Topratedplace(models.Model):
    title=models.CharField(max_length=120)
    slug=models.CharField(max_length=200)
    description=models.TextField(default="Description text will be added here")
    image=models.ImageField(upload_to="Top Rated/",blank=False)
    price = models.IntegerField(default=1500)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    sub_district = models.ForeignKey(Sub_District, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}-{}'.format(self.title,self.slug)


@receiver(post_save, sender=Topratedplace)
def create_profile(sender, instance, created, **kwargs):
    if created:
        all_email=Subscriber.objects.all()
        all=[]
        for i in all_email:
            all.append(i.email)

        mail_subject ='Top Rated Place Added'
        message="Please check our new top rated place that are now available in our website"
        email = EmailMessage(
            mail_subject, message, to=all
        )
        email.send()

class TopPlaceorder(models.Model):
    place = models.ForeignKey(Topratedplace, on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    person = models.IntegerField(default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=500,default="")
    ammount = models.FloatField(max_length=100,default=0.0)
    card_type = models.CharField(max_length=100, default="", blank=True)
    payment_status = models.CharField(max_length=100, default="", blank=True)
    transaction_date = models.CharField(max_length=100, default="", blank=True)
    risk_title = models.CharField(max_length=100, default="", blank=True)

    def get_absolute_url(self):
        return reverse('payment', kwargs={'id': self.id})