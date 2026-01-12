from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
#from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=120)
    contenuto= models.TextField( )
    data = models.DateTimeField(auto_now=False, auto_now_add=True) #(default=timezone.now)
    slug= models.SlugField()#crea URL humanfriendly
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    #best pracice per ottenere url
    def get_absolute_url(self):
        return reverse("singolo",kwargs={"id": self.id, "slug":self.slug})

# Create your models here.
