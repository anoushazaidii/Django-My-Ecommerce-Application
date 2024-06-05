from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name =  models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    product_category = models.CharField(max_length=50,default="")
    product_sub_category = models.CharField(max_length=50,default="")
    product_pub_date = models.DateField
    image= models.ImageField(upload_to="shop/images",default="")
    product_price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500,default="")
 
    def __str__(self):
        return self.name    
    
 
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)    
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,default="")