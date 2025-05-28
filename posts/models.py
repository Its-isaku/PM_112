
#? Library imports
from django.db import models
from django.urls import reverse

#? Class for the Post model
class Post(models.Model):
    title = models.CharField(max_length=128)                 #* Inheritance | Title of the post
    subtitle = models.CharField(max_length=256)              #* Composition | Subtitle of the post
    body = models.TextField()                                #* Composition | Body of the post
    created_on = models.DateTimeField(auto_now_add=True)     #* Composition | Date of creation

    def __str__(self):
        return self.title  #* Returns the title of the post when the object is printed
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
    