from django.contrib import admin
from .models import Books,Members,Carts,Orders

# Register your models here.

class MembersAdmin(admin.ModelAdmin):
    list_display=['MemberAccount','MemberPassword','MemberName','MemberAddress','MemberPhone']
    list_per_page=10

admin.site.register(Members,MembersAdmin)

class BooksAdmin(admin.ModelAdmin):
    list_display=['ISBN','BookName','BookAuthor','BookPrice','BookPress','BookRemainNum','BookCategory']
    list_per_page=10

admin.site.register(Books,BooksAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display=['OrderID','ISBN','MemberAccount','OrderNum','OrderTime','OrderState']
    list_per_page=10

admin.site.register(Orders,OrdersAdmin)

class CartsAdmin(admin.ModelAdmin):
    list_display=['MemberAccount','ISBN','CartNum']
    list_per_page=10

admin.site.register(Carts,CartsAdmin)