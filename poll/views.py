from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse, request
#from .forms import RegistrationForm
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
#from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Candidate,ControlVote,Position
#from .forms import ChangeForm
from django.conf import settings
from django.core.mail import send_mail
import math, random
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
import datetime

def indexview(request):
    return render(request, "poll/index2.html")

def homeView(request):
    return render(request, "poll/home.html")

def generateOTP() : 
    digits = "0123456789"
    OTP=""
    for i in range(5) :
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP 
'''
def send_otp(request):
     email=request.GET.get("email")
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     
     send_mail('OTP request',o,'abhishekkanshetti@gmail.com',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)


def verifyEmail():
	
	if(theOTP == mOTP):
			cur = mysql.connection.cursor()
			ar = cur.execute('INSERT INTO users(name, email, password, user_type, user_image) values(%s,%s,%s,%s,%s)', (dbName, dbEmail, dbPassword, dbUser_type, dbImgdata))
			mysql.connection.commit()
			if ar > 0:
				flash("Thanks for registering! You are sucessfully verified!.")
				return  redirect(url_for('login'))
			else:
				flash("Error Occurred!")
				return  redirect(url_for('login')) 
			cur.close()
			session.clear()
		else:
			return render_template('register.html',error="OTP is incorrect.")
	return render_template('verifyEmail.html')
'''
def verifyemailvotingview(request):
    if request.method == "POST":
        passw = request.POST['otpelec']
        #print(passw)
        #print(o)
        if otpelec==passw:
            #obj = form.save(commit=False)
            #obj.save()
            #username=request.session.get['username']
            #useremail=request.session['email'] 
            #msg = 'your username is'+username
            #send_mail(subject='About UserName',message=msg,from_email='abhishekkanshetti@gmail.com',recipient_list=[useremail], fail_silently=False,)
            messages.success(request, 'Your mail is verified.')
            return redirect('position')
        else:
            messages.success(request, 'Invalid OTP! Enter Correct OTP to Vote in Election')
            return render(request, "poll/verifyemailvoting.html")
    else:
        return render(request, "poll/verifyemailvoting.html")

def emailvotingview(request):
    if request.method == "POST":
        global otpelec
        otpelec=generateOTP()
        msg= 'Your OTP is'+' '+otpelec
        useremail = request.POST['emailvote']
        send_mail(subject='OTP request',message=msg,from_email='abhishekkanshetti@gmail.com',recipient_list=[useremail], fail_silently=False,)
        return redirect('verifyemailvoting')
        #print(passw)
        #print(o)
        '''
        if o==passw:
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'You have been registered.')
            return redirect('home')
        else:
            messages.success(request, 'Invalid OTP!')
            return render(request, "poll/verifyotp.html")
        '''
    else:
        return render(request, "poll/emailvoting.html")
    #return redirect('forgotemail')

# as django not supports anonoyms user so we cant use this.
@login_required
def changePasswordverifyforgotemail(request):
    if request.method == "POST":
        formp = PasswordChangeForm(user=request.user, data=request.POST)
        if formp.is_valid():
            formp.save()
            update_session_auth_hash(request,formp.user)
            messages.success(request, 'You Password has been reset.')
            return redirect('home')
    else:
        formp = PasswordChangeForm(user=request.user)

    return render(request, "poll/password.html", {'form':formp})

def verifyforgotemail(request):
    if request.method == "POST":
        passw = request.POST['otp']
        #print(passw)
        #print(o)
        if otp==passw:
            #obj = form.save(commit=False)
            #obj.save()
            #username=request.session.get['username']
            #useremail=request.session['email'] 
            #msg = 'your username is'+username
            #send_mail(subject='About UserName',message=msg,from_email='abhishekkanshetti@gmail.com',recipient_list=[useremail], fail_silently=False,)
            messages.success(request, 'Your mail is verified but for security reason you must Login to our web portal.')
            return redirect('changePasswordforgotemail')
        else:
            messages.success(request, 'Invalid OTP!')
            return render(request, "poll/forgotemailverifyotp.html")
    else:
        return render(request, "poll/forgotemailverifyotp.html")

def forgotemail(request):
    if request.method == "POST":
        global otp
        otp=generateOTP()
        msg= 'Your OTP is'+' '+otp
        useremail = request.POST['femail']
        send_mail(subject='OTP request',message=msg,from_email='abhishekkanshetti@gmail.com',recipient_list=[useremail], fail_silently=False,)
        return redirect('verifyforgotemail')
        #print(passw)
        #print(o)
        '''
        if o==passw:
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'You have been registered.')
            return redirect('home')
        else:
            messages.success(request, 'Invalid OTP!')
            return render(request, "poll/verifyotp.html")
        '''
    else:
        return render(request, "poll/forgotemail.html")
    #return redirect('forgotemail')

def verifyemail(request):
    if request.method == "POST":
        passw = request.POST['otp']
        #print(passw)
        #print(o)
        if o==passw:
            #useremail = form.cleaned_data.get('email')
            obj = form.save(commit=False)
            obj.save()
            id = obj.id
            useremail = obj.email
            msg = 'Congratulations you have Sucessfully Registered on Digi-vote.\n Your Voter ID is'+' '+'DGVOTE'+str(id)
            send_mail(subject='Voter ID',message=msg,from_email='abhishekkanshetti@gmail.com',recipient_list=[useremail], fail_silently=False,)
            messages.success(request, 'You have been registered and Your Voterid is sent on your mail.')
            return redirect('home')
        else:
            messages.success(request, 'Invalid OTP!')
            return render(request, "poll/verifyotp.html")
    else:
        return render(request, "poll/verifyotp.html")
    #return render(request,"poll/verifyotp.html")

def registrationView(request):
    if request.method == "POST":
        global form
        form = CustomUserCreationForm(request.POST)     #form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dateofbirth = cd['dob']
            userpass= cd['password1']
            userconfirm= cd['password2']
            #request.session['username'] = cd['username']
            #request.session['email'] = cd['email']
            #temp=0
            useremail= cd['email']
            global o
            o=generateOTP()
            #htmlgen = '<p>Your OTP is <strong>o</strong></p>'
            msg= 'Your OTP is'+' '+o
            if (datetime.date.today() - dateofbirth) >= datetime.timedelta(days=18*365):
                if userpass == userconfirm:
                    send_mail(subject='OTP request',message=msg,from_email='abhishekkanshetti@gmail.com',recipient_list=[useremail], fail_silently=False,)
                    #obj = form.save(commit=False)
                    #obj.set_password(obj.password)
    
                    #obj.save()
                    #messages.success(request, 'You have been registered.')
                    return redirect('verifyotp')
                else:
                    return render(request, "poll/registration.html", {'form':form,'note':'Password not matched During Registration.'})

            else:
                return render(request, "poll/registration.html", {'form':form,'note':'Your Age is not eligible for voter Registration.'})
    else:
        form = CustomUserCreationForm()               #form = RegistrationForm(request.POST)

    return render(request, "poll/registration.html", {'form':form})

from .backend import CustomUserBackend

def loginView(request):
    if request.method == "POST":
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request, username=usern, password=passw)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.success(request, 'Invalid username or password!')
            return render(request, "poll/login.html")
    else:
        return render(request, "poll/login.html")


@login_required
def logoutView(request):
    logout(request)
    return redirect('home')

@login_required
def dashboardView(request):
    return render(request, "poll/dashboard.html")

@login_required
def positionView(request):
    obj = Position.objects.all()
    cnt=0
    sbk=0
    for i in obj:
        if i.Election_on == True:
            sbk+=1
        cnt+=1
    if cnt==sbk:
        return render(request, "poll/position.html", {'obj':obj})
    else:
        messages.success(request, 'Election is not Available.')
        return redirect('home')
    

@login_required
def candidateView(request, pos):
    obj = get_object_or_404(Position, pk = pos)
    if request.method == "POST":

        temp = ControlVote.objects.get_or_create(user=request.user, position=obj)[0]

        if temp.status == False:
            temp2 = Candidate.objects.get(pk=request.POST.get(obj.title))
            temp2.total_vote += 1
            temp2.save()
            temp.status = True
            temp.save()
            return HttpResponseRedirect('/position/')
        else:
            messages.success(request, 'you have already been voted this position.')
            return render(request, 'poll/candidate.html', {'obj':obj})
    else:
        return render(request, 'poll/candidate.html', {'obj':obj})

@login_required
def resultView(request):
    pobj = Position.objects.all()
    cnt=0
    sbk=0
    for i in pobj:
        if i.show_result == True:
            sbk+=1
        cnt+=1

    if cnt==sbk:
        obj = Candidate.objects.all().order_by('position','-total_vote')
        return render(request, "poll/result.html", {'obj':obj})
    else:
        messages.success(request, 'You Cannot see the Result unless the Admin Publishes the Result.')
        return redirect('home')


@login_required
def candidateDetailView(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    return render(request, "poll/candidate_detail.html", {'obj':obj})


@login_required
def changePasswordView(request):
    if request.method == "POST":
        formc = PasswordChangeForm(user=request.user, data=request.POST)
        if formc.is_valid():
            formc.save()
            update_session_auth_hash(request,formc.user)
            return redirect('dashboard')
    else:
        formc = PasswordChangeForm(user=request.user)

    return render(request, "poll/password.html", {'form':formc})


@login_required
def editProfileView(request):
    if request.method == "POST":
        formp = CustomUserChangeForm(request.POST, instance=request.user)  #form = ChangeForm(request.POST, instance=request.user)
        if formp.is_valid():
            formp.save()
            return redirect('dashboard')
    else:
        formp = CustomUserChangeForm(instance=request.user)               #form = ChangeForm(instance=request.user)
    return render(request, "poll/edit_profile.html", {'form':formp})
