from django.db import models
from . constain import CATEGORY 
    
class BookModel(models.Model):
    isbn = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=10 , choices=CATEGORY)
    count = models.IntegerField()
    avialable = models.BooleanField()
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
