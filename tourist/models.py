from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.
from django.core.mail import send_mail, EmailMessage
from django.dispatch import receiver
from account.models import User

class guider(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    details=models.TextField(max_length=500)
    photo=models.ImageField(upload_to="guider/",blank=False)
    hourly_rate=models.IntegerField(default=50)

    def __str__(self):
        return self.name

    def review_count(self):
        return Ratting.objects.filter(name=self).count()
    def get_ratting(self):
        val=Ratting.objects.filter(name=self)
        count=0
        for i in val:
            count=count+i.score
        if count>0:
            return format(count/(val.count()),".1f")
            # return count/(val.count())
        return count
    def get_ratting_float(self):
        val=Ratting.objects.filter(name=self)
        count=0
        for i in val:
            count=count+i.score
        if count>0:
            # return format(count/(val.count()),".1f")
            return count/(val.count())
        return count

@receiver(post_save, sender=guider)
def create_profile(sender, instance, created, **kwargs):
    if created:
        all_email=Subscriber.objects.all()
        all=[]
        for i in all_email:
            all.append(i.email)

        mail_subject ='New Guider Created'
        message="Please check our new guider that are now available in our website"
        email = EmailMessage(
            mail_subject, message, to=all
        )
        email.send()

class Ratting(models.Model):
    name=models.ForeignKey(guider,on_delete=models.CASCADE,related_name='guider_name')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    score=models.IntegerField(default=0)

    def __str__(self):
        return '{}-{}-{}'.format(self.name,self.user,self.score)


class hireguider(models.Model):
    guider_name = models.ForeignKey(guider, on_delete=models.DO_NOTHING)
    hour = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=500, default="")
    ammount = models.FloatField(max_length=100, default=0.0)

    def get_absolute_url(self):
        return reverse('guider_payment', kwargs={'id': self.id})


class Feedback(models.Model):
    name =models.ForeignKey(User,on_delete=models.CASCADE)
    experience=models.TextField(default="your experience here")
    category = models.CharField(max_length=30,blank=False)
    privacy=models.CharField(max_length=30,blank=False)
    image=models.ImageField(upload_to="feedback/",blank=True)
    love = models.ManyToManyField(User, related_name="scope_love", blank=True)
    status=models.BooleanField(default=False)

    def total_love(self):
        return self.love.count()

    def __str__(self):
        return str(self.name)


class Contactus(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=30,blank=False)
    message=models.TextField(blank=False)
    status=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

class Subscriber(models.Model):
    email=models.EmailField(max_length=30,blank=False)

    def __str__(self):
        return str(self.email)
