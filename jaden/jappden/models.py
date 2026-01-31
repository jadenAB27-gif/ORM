from django.db import models
from django.contrib import admin
class ZomatoDB(models.Model):
	OrderNo=models.IntegerField(primary_key=True);
	OrderName=models.CharField(max_length=10);
	Bill=models.FloatField();
	Mobile_no=models.IntegerField();
	Address=models.CharField(max_length=40);
	DeliveryName=models.CharField(max_length=10);
class ZomatoDBAdmin(admin.ModelAdmin):
	list_display=['OrderNo','OrderName','Bill','Mobile_no','Address','DeliveryName'];
