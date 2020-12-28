from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Services(models.Model):
    services=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.services
    class Meta:
        verbose_name_plural = "Services"

class HairCare(models.Model):
    hairCare = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.hairCare


class MakeUpServices(models.Model):
    makeUpServices = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.makeUpServices
    class Meta:
        verbose_name_plural = "Make Up Services"

class FacialTreatment(models.Model):
    facialTreatment = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.facialTreatment

class NailArts(models.Model):
    nailArts = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nailArts
    class Meta:
        verbose_name_plural = "Nail Arts"

class HairStyles(models.Model):
    hairStyles = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.hairStyles

class Pedicure(models.Model):
    pedicure = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.pedicure

class Manicure(models.Model):
    manicure = models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    hours=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.manicure



class Blog(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE, related_name="blogs",default=False)
    body=models.TextField()
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    status=models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Blogs"

class Comment(models.Model):
    post=models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment {} by {}'.format(self.body, self.name)

class BookingHaircare(models.Model):
    haircare=models.ForeignKey(HairCare, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

    # def __str__(self):
    #     return self.haircare


    

class BookingMakeUpServices(models.Model):
    makeupservices=models.ForeignKey(MakeUpServices, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

class BookingFacialTreatment(models.Model):
    facialtreatment=models.ForeignKey(FacialTreatment, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

class BookingNailArts(models.Model):
    nailarts=models.ForeignKey(NailArts, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

class BookingHairStyles(models.Model):
    hairstyles=models.ForeignKey(HairStyles, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

class BookingPedicure(models.Model):
    pedicure=models.ForeignKey(Pedicure, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

class BookingManicure(models.Model):
    manicure=models.ForeignKey(Manicure, on_delete=models.CASCADE)
    date=models.DateField(blank=True, null=True)

