from django.db import models

# Create your models here.
class Product_category(models.Model):
    Pcid=models.IntegerField(primary_key=True)
    Pcname=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Pcname
    
class Product(models.Model):
    Pcname=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdate=models.DateField()
    Pcolour=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.Pname