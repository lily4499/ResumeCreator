import io 

from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Contact
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django.views import View
import csv
import os
from django.views.generic import View
from django.forms.models import model_to_dict
from .forms import ResumeForm 
from django.template.loader import get_template
from django.conf import settings
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string, get_template
from weasyprint import HTML
from xhtml2pdf import pisa
from .models import Profile  # Assuming Profile model is imported correctly


# Create your views here.

def index(request):

    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phoneno=request.POST.get("phoneno")
        msg=request.POST.get("msg")
        
        myquery = Contact(name=name, email=email, phoneno=phoneno, msg=msg)
        myquery.save()

#Sending Email
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f'Email From {name}', f'User Email : {email}\n User Phone Number:{phoneno}\n Message from User: {msg}', from_email, ['ayuresumebuilder@gmail.com'], connection=connection)

        email_message_user = mail.EmailMessage(f'ResumeBuilder Response', f'Hey {name}\n\n Thanks for reaching us.\n We will get back to you soon.', from_email, [email], connection=connection)

        connection.send_messages([email_message, email_message_user])
        connection.close()
        
        messages.info(request, "Your response has been recorded. Thanks for reaching us.")
        return redirect('/#home')


    return render(request, 'index.html')


def signupPage(request):

    if request.method == "POST":
        uname=request.POST.get("Username")
        fname=request.POST.get("Fname")
        lname=request.POST.get("Lname")
        email=request.POST.get("Emailid")
        pass1=request.POST.get("Password")
        pass2=request.POST.get("confirmPassword")

        if pass1 != pass2:
            messages.error(request, "Password doesn't match!")
            return redirect('/signup')

        try:
            if User.objects.get(username = uname):
                messages.warning(request, "Username is already taken!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email = email):
                messages.warning(request, "Email ID is already registered!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(uname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "SignUp Successful!")
        return redirect('/login')

    return render(request, 'signup.html')

def loginPage(request):

    if request.method == "POST":
        uname=request.POST.get("Username")
        password=request.POST.get("Password")

        myuser = authenticate(username=uname, password=password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful!")
            return redirect('/')

        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('/login')

    return render(request, 'login.html')
    


def addddResume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Save form data and associate with the current user
            profile = form.save(commit=False)
            profile.userid = request.user.username  # Assuming user is authenticated
            profile.save()
            messages.success(request, "Your resume has been successfully added!")
            return redirect('add_resume')
    else:
        form = ResumeForm()

    return render(request, 'addResume.html', {'form': form})


def addResume(request):
    user_profile = Profile.objects.filter(userid=request.user.username).first()

    if user_profile:
        # User already has a resume, provide option to edit it
        return redirect('listResume')

    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Save form data and associate with the current user
            profile = form.save(commit=False)
            profile.userid = request.user.username
            profile.save()
            messages.success(request, "Your resume has been successfully added!")
            return redirect('addResume')
    else:
        form = ResumeForm()

    return render(request, 'addResume.html', {'form': form})


def viewResume(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, "viewResume.html", {'user_profile':user_profile})
   

def listResume(request):
    current_user = request.user.username
    userid = Profile.userid

    if Profile.objects.filter(userid = current_user).exists():
        profile=Profile.objects.filter(userid = current_user)
        return render(request, "listResume.html", {'profile':profile})
        
    return render(request, "listResume.html")


def logoutPage(request):
    logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('/login')




def generate_pdf_resume(request):
    # Retrieve profile data for the current user
    user_profile = Profile.objects.filter(userid=request.user.username).first()
    template_path = 'viewResume.html'  # Define the path to your template

    if user_profile:
        # Populate the context with the user's profile data
        context = {'user_profile': user_profile}

        # Load template
        template = get_template(template_path)
        html = template.render(context)

        # Create a PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        # Create a PDF file
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response
    else:
        return HttpResponse("Profile not found for the current user", status=404)


def download(request):
    # Retrieve profile data for the current user
    user_profile = Profile.objects.filter(userid=request.user.username).first()
    template_path = 'download.html'  # Define the path to your template

    if user_profile:
        # Populate the context with the user's profile data
        context = {'user_profile': user_profile}

        # Load template
        template = get_template(template_path)
        html = template.render(context)

        # Create a PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        # Create a PDF file
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response
    else:
        return HttpResponse("Profile not found for the current user", status=404)





def deleteResume(request):
    # Retrieve the user's profile (resume)
    user_profile = Profile.objects.filter(userid=request.user.username).first()

    if request.method == "POST":
        # Delete the user's profile (resume)
        user_profile.delete()
        messages.success(request, "Your resume has been successfully deleted!")
        return redirect('addResume')  # Redirect to a relevant page after deletion

    return render(request, 'confirmDelete.html', {'user_profile': user_profile})