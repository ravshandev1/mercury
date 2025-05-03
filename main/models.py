from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.text


class AboutImage(models.Model):
    about = models.ForeignKey(About, models.CASCADE, 'images')
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.about.text


class Carousel(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, models.CASCADE)
    description = RichTextField()
    scope = RichTextField()

    def __str__(self):
        return self.name


class Table(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'tables')
    size = models.CharField(max_length=500)
    color = models.CharField(max_length=500)
    in_package = models.CharField(max_length=500)
    code = models.CharField(max_length=500)

    def __str__(self):
        return self.size


class Character(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'characters')
    key = models.CharField(max_length=500)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.key


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=500)
    address = models.TextField()
    telegram = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    whatsapp = models.CharField(max_length=500)
    iframe = models.TextField()

    def __str__(self):
        return self.email


class Phone(models.Model):
    phone = models.CharField(max_length=500)
    contact = models.ForeignKey(Contact, models.CASCADE, 'phones')

    def __str__(self):
        return self.phone


class Certificate(models.Model):
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.image.name


class Client(models.Model):
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.image.name
