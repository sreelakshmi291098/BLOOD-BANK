from django.db import models



from django.contrib.auth.models import User

class Donor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=500)
    blood_group=models.CharField(max_length=500)
    profile_photo=models.ImageField(upload_to ='images/')
    status=models.CharField(max_length=10)
    last_donate_date=models.DateField(max_length=264,unique=True)
    role=models.CharField(max_length=20)

class Reg_user(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=500)
    blood_group=models.CharField(max_length=500)
    disease=models.CharField(max_length=500)
    profile_photo=models.ImageField(upload_to ='images/')
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=20)

class Request(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    donor_id=models.IntegerField()
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    blood_group=models.CharField(max_length=500)
    last_donate_date=models.DateField(max_length=264,unique=True)
    disease=models.CharField(max_length=500)
    quantity=models.CharField(max_length=500)
    status=models.CharField(max_length=10)

class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    comment=models.CharField(max_length=100)

