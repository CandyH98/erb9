from django.db import models
from doctors.models import Doctor

# Create your models here.
class Listing(models.Model):
    doctors=models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    choices=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    services=models.CharField(max_length=200)
    services=models.IntegerField()
    room_type=models.CharField(max_length=50)
    rooms=models.IntegerField()
    photos_main=models.ImageField(upload_to='photo/%Y/%m/%d')
    photos_1=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    photos_2=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    photos_3=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    photos_4=models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-list_date']
        indexes=[models.Index(fields=['list_date'])]

    def __str__(self):
        return self.title 