from django.db import models

# Create your models here.


'''class 书籍类别表(models.Model):
    名称 = models.CharField(max_length=50,unique=True)
    描述 = models.TextField(blank=True)
    图片 = models.ImageField(upload_to='category',blank=True)

    class Meta:
        verbose_name_plural='书籍类别表'
        db_table='书籍类别表'

    def __str__(self):
        return self.名称'''

class Books(models.Model):
    ISBN = models.CharField(max_length=15,unique=True)
    BookName = models.CharField(max_length=30)
    BookAuthor = models.CharField(max_length=30)
    BookPrice = models.DecimalField(max_digits=10,decimal_places=2)
    BookRemainNum = models.IntegerField(default=0)
    BookPress = models.CharField(max_length=30,blank=True)
    BookCategory = models.CharField(max_length=30,blank=True)
    Photo = models.ImageField(upload_to='category',blank=True)

    class Meta:
        verbose_name_plural='Books'
        db_table='Books'
        ordering = ('ISBN',)

    def __str__(self):
        return self.ISBN

class Members(models.Model):
    MemberAccount = models.CharField(max_length=10, unique=True)
    MemberPassword = models.CharField(max_length=10)
    MemberName = models.CharField(max_length=30)
    MemberAddress = models.CharField(max_length=30)
    MemberPhone = models.CharField(max_length=11)

    def __str__(self):
        return self.MemberAccount

    class Meta:
        ordering = ["MemberAccount"]
        verbose_name = "Member"
        verbose_name_plural = "Members"
        db_table='Members'

class Orders(models.Model):
    OrderID = models.CharField(max_length=20, unique=True)
    ISBN = models.ForeignKey(Books,on_delete=models.CASCADE)
    MemberAccount = models.ForeignKey(Members,on_delete=models.CASCADE)
    OrderNum = models.IntegerField(default=1)
    OrderTime = models.DateTimeField(auto_now_add=True)
    OrderState = models.CharField(max_length=10)

    def __str__(self):
        return self.OrderID

    class Meta:
        ordering = ["OrderTime"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table='Orders'

class Carts(models.Model):
    CartID = models.CharField(max_length=20,unique=True,default=0)
    MemberAccount = models.ForeignKey(Members,on_delete=models.CASCADE)
    ISBN = models.ForeignKey(Books,on_delete=models.CASCADE)
    CartNum = models.IntegerField(default=1)

    def __str__(self):
        return self.CartID

    class Meta:
        ordering = ["MemberAccount"]
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        db_table='Carts'