# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'

    def save(self, *args, **kwargs):

        bad_words = ['ablah', 'befarosat', 'onasini_emsin']
        if any(bad_word in self.content.lower() for bad_word in bad_words):
            self.is_visible = False
        super().save(*args, **kwargs)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user.username} for {self.product.name}'
