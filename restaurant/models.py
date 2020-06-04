from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=32)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=120)
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=20)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
class BookTable(models.Model):
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.product_name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    amount=models.IntegerField(default=0)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name
class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."