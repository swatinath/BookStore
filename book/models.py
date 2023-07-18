from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Categories"
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="book_images")
    
    # def __str__(self):
        # return self.title   #used to display only title of the book
