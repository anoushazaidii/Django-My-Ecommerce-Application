from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField
    product_name =  models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    product_category = models.CharField(max_length=50,default="")
    product_sub_category = models.CharField(max_length=50,default="")
    product_pub_date = models.DateField
    image= models.ImageField(upload_to="shop/images",default="")
    product_price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product_name