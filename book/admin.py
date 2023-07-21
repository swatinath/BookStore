from django.contrib import admin

from book.models import Category, Book, Order

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'is_available')   #used to display all the elements of the tuple
    search_fields = ('title',)
    list_editable = ('is_available',)    #used to change is_available outside
    list_filter = ('is_available','category',)
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'quantity', 'status',)   
    search_fields = ('user', 'book',)
    list_editable = ('status',)    
    list_filter = ('status',)    
    
admin.site.register(Category)
admin.site.register(Book, BookAdmin)  #output as defined by BookAdmin
admin.site.register(Order, OrderAdmin)  