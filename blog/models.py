
from typing import Any
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField




class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True, db_index=True, editable=False)

    def __str__(self):
       return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    name = models.CharField(max_length=250)
    resim = models.ImageField(upload_to="blogs")
    description = RichTextField()
    post_time = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, unique=True, db_index=True, editable=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Education(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to="education")
    slug = models.SlugField(null=False, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category)
 
    
    def __str__(self):
       return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)