from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from app22.models import Donor,Reg_user,Request,feedback
from.import models
from django.contrib.auth.models import User
from app22.forms import loginForm
from django.contrib import messages
# Create your views here.
def adminpage(request):
    return render(request,'admin.html')

def user(request):
    return render(request,'user.html')

def donator(request):
    return render(request,'donator.html')

def index(request):
    return render(request,'index.html')
role=""
roles=""
def login(request):
    global role
    global roles
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            id=i['id']
            u_name=i['username']
            print(".............",id,u_name)
 
            da=Donor.objects.filter(user_id=id).values()
            print("donnordata==>",da)
            for i in da:
                roles=i['role']
                statuss=i['status']
                print(roles)

            d=Reg_user.objects.filter(user_id=id).values()
            print("userdata==>",d)
            for i in d:
                roles=i['role']
                status=i['status']
                print(roles)

            user=authenticate(username=username,password=password)

            if user is not None and roles=='user' and username==u_name and status=="1":
                auth_login(request,user)
                return redirect("user")

            elif roles=='donor' and username==u_name and statuss=="1":
                auth_login(request,user)
                return redirect("donator")

            elif username=="sreelakshmi" and password=="sree123":
                return redirect("adminpage")
            else:pass
        else:
            messages.info(request,'Invalid credentials')
            return redirect("login")
    else:
        return render(request,'login.html')
    

def register(request):
    return render(request,'registration.html')

def userrequest(request):
    return render(request,'userrequest.html')

def donorrequest(request):
    return render(request,'donorrequest.html')

def blooddonate(request):
    return render(request,'blooddonate.html')

def viewuserreq(request):
    return render(request,'viewuserreq.html')

def viewdonorreq(request):
    return render(request,'viewdonorreq.html')

def viewuser(request):
    return render(request,'viewuser.html')

def viewdonor(request):
    return render(request,'viewdonor.html')

def donorreg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('conformpassword')
        address=request.POST.get('address')
        phonenumber=request.POST.get('number')
        blood_group=request.POST.get('bloodgroup')
        disease=request.POST.get('disease')
        last_donate_date=request.POST.get('date')
        profile=request.FILES['profile']
        status="0"
        role="donor"

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("donorreg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect("donorreg")
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                userDetail=models.Donor(user=user,name=name,email=email,address=address,phone_number=phonenumber,blood_group=blood_group,last_donate_date=last_donate_date,profile_photo=profile,status=status,role=role)
                userDetail.save()

                print('user created')
        else:
            messages.info(request,"password is not matching")
            return redirect("donorreg")
        return redirect("login")
    else:
        return render(request,'donorreg.html')

def userreg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('conformpassword')
        address=request.POST.get('address')
        phonenumber=request.POST.get('phonenumber')
        blood_group=request.POST.get('bloodgroup')
        disease=request.POST.get('disease')
        profile=request.FILES['profile']
        status="0"
        role="user"

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("userreg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect("userreg")
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                userDetail=models.Reg_user(user=user,name=name,email=email,address=address,phone_number=phonenumber,blood_group=blood_group,disease=disease,profile_photo=profile,status=status,role=role)
                userDetail.save()

                print('user created')
        else:
            messages.info(request,"password is not matching")
            return redirect("userreg")
        return redirect("login")
    else:
        return render(request,'userreg.html')


def userpending(request):
    data=Reg_user.objects.all()
    return render(request,'viewuserpending.html',{'data':data})

def donorpending(request):
    data=Donor.objects.all()
    return render(request,'viewdonorpending.html',{'data':data})

def user_approve(request,reg_id):
    reg=Reg_user.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("userpending")

def user_reject(request,reg_id):
    item=Reg_user.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("userpending")

def approveduser(request):
    data=Reg_user.objects.all()
    return render(request,'approveduser.html',{'data':data})

def donor_approve(request,reg_id):
    reg=Donor.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("donorpending")

def donor_reject(request,reg_id):
    item=Donor.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("donorpending")

def approveddonor(request):
    data=Donor.objects.all()
    return render(request,'approveddonor.html',{'data':data})

def user_delete(request,reg_id):
    add=Reg_user.objects.get(id=reg_id)
    add.delete()
    return redirect('approveduser')

def donor_delete(request,reg_id):
    dele=Donor.objects.get(id=reg_id)
    dele.delete()
    return redirect('approveddonor')

def viewuserprofile(request):
    data=Reg_user.objects.all()
    return render(request,'viewuserprofile.html',{'data':data})

def viewdonorprofile(request):
    data=Donor.objects.all()
    return render(request,'viewdonorprofile.html',{'data':data})

def userdelete(request,id):
    if request.method=="POST":
        add=Reg_user.objects.get(id=id)
        add.delete()
        return redirect('viewuserprofile')
    else:
        Data=Reg_user.objects.all()
        return render(request, 'viewuserprofile.html',{'Data':Data})

def formupdate(request,id):
    if request.method=="POST":
        add=Reg_user.objects.get(id=id)
        add.name=request.POST['name']
        add.address=request.POST['address']
        add.email=request.POST['email']
        add.phone_number=request.POST['phonenumber']
        add.blood_group=request.POST['bloodgroup']
        add.profile_photo=request.POST['profile']
        add.save()
        return redirect("viewuserprofile")
    else:
        Data=Reg_user.objects.all()
        return render(request, 'userupdate.html',{'Data':Data})

def userupdate(request):
    return render(request,'userupdate.html')

def edit(request,id):
    Data=Reg_user.objects.get(id=id)
    return render(request,'userupdate.html',{'Data':Data})

def donordelete(request,id):
    if request.method=="POST":
        add=Donor.objects.get(id=id)
        add.delete()
        return redirect('donator')
    else:
        Data=Donor.objects.all()
        return render(request, 'viewdonorprofile.html',{'Data':Data})

def donatorupdate(request,id):
    if request.method=="POST":
        add=Donor.objects.get(id=id)
        add.name=request.POST['name']
        add.address=request.POST['address']
        add.email=request.POST['email']
        add.phone_number=request.POST['phonenumber']
        add.blood_group=request.POST['bloodgroup']
        add.last_donate_date=request.POST['donatedate']
        add.profile_photo=request.POST['profile']
        add.save()
        return redirect("viewdonorprofile")
    else:
        Data=Donor.objects.all()
        return render(request, 'donorupdate.html',{'Data':Data})

def donorupdate(request):
    return render(request,'donorupdate.html')

def donoredit(request,id):
    Data=Donor.objects.get(id=id)
    return render(request,'donorupdate.html',{'Data':Data})

def donorlist(request):
    data=Donor.objects.all()
    print(data)
    return render(request,'donorlist.html',{'data':data})

def requestform(request,id):
    Data=Donor.objects.get(id=id)
    return render(request,'requestform.html',{'Data':Data})


def requestapply(request):
    if request.user:
        user=request.user
        if request.method=='POST':
            donor_id=request.POST.get('id')
            name=request.POST.get('name')
            phonenumber=request.POST.get('phonenumber')
            blood_group=request.POST.get('bloodgroup')
            disease=request.POST.get('disease')
            last_donate_date=request.POST.get('date')
            quantity=request.POST.get('quantity')
            status="0"

            userDetail=models.Request(user=user,donor_id=donor_id,name=name,phone_number=phonenumber,blood_group=blood_group,disease=disease,last_donate_date=last_donate_date,quantity=quantity,status=status)
            userDetail.save()
            return redirect("requestlist")
        else:
            return render(request,'donorlist.html')
    else:    
        return render(request,'donorlist.html')


def requestedit(request,id):
    Data=Donor.objects.get(id=id)
    return render(request,'requestform.html',{'Data':Data})


def requestlist(request):
    data=Request.objects.all()
    return render(request,'requestlist.html',{'data':data})

def adminapproved(request):
    data=Request.objects.all()
    return render(request,'adminapproved.html',{'data':data})

def admin_approve(request,reg_id):
    reg=Request.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("donator")

def donor_request_approved(request):
    data=Request.objects.all()
    return render(request,'donor_request_approved.html',{'data':data})

def request_delete(request,reg_id):
    add=Request.objects.get(id=reg_id)
    add.delete()
    return redirect('adminpage')

def donator_approve(request,reg_id):
    reg=Request.objects.get(id=reg_id)
    reg.status=2
    reg.save()
    return redirect("user")

def donatorapproved(request):
    data=Request.objects.all()
    return render(request,'donatorapproved.html',{'data':data})

def feed_back(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')

        userDetail=models.feedback(name=name,email=email,comment=comment)
        userDetail.save()
        return redirect("adminpage")
    else:
        return render(request,'feedback.html')

def viewfeedback(request):
    data=feedback.objects.all()
    return render(request,'viewfeedback.html',{'data':data})



