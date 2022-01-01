import random
import string
from django.utils.text import slugify
   

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
    return res



def Event_slug_generate(text):
    from .models import AdminTouristEvent
    new_slug = slugify(text)
    if AdminTouristEvent.objects.filter(slug=new_slug).first():
        return Event_slug_generate(text+generate_random_string(5))
    return new_slug


def User_Event_slug_generate(text):
    from .models import UserTouristEvent
    new_slug = slugify(text)
    if UserTouristEvent.objects.filter(slug=new_slug).first():
        return Event_slug_generate(text+generate_random_string(5))
    return new_slug
