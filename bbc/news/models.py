from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cat_name


class News(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='news', blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return self.title


class CompanySetting(models.Model):
    c_name = models.CharField(max_length=255)
    c_email = models.CharField(max_length=255, blank=True, null=True)
    c_address = models.CharField(max_length=255, blank=True, null=True)
    c_phone = models.CharField(max_length=255, blank=True, null=True)
    c_logo = models.ImageField(upload_to='logo', blank=True, null=True)

    def __str__(self):
        return self.c_name


class Contact(models.Model):
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email
