from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Warranty(models.Model):
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.duration


class Seller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_short_note = models.TextField(max_length=200)
    profileimg = models.ImageField(upload_to='media/images', default='media/images/blank_profile_pic.jpg')

    def __str__(self):
        return self.name

    @classmethod
    def filter_by_price(cls, min_price=None, max_price=None):
        products = cls.objects.all()
        
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        
        if max_price is not None:
            products = products.filter(price__lte=max_price)
        
        return products
