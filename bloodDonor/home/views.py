from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Contact, UserProfile, DonorStory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    #user = User.objects.all()
    profile = UserProfile.objects.all()
    story = DonorStory.objects.all()

    return render(request, 'home/home.html', {
        'profile': profile,
        'story':story,

    })

def about(request):
    return render(request, 'home/about.html')

def users(request):
    users = UserProfile.objects.all()
    paginator = Paginator(users, 3)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    pagerange = paginator.num_pages
   


    return render(request, 'home/users.html',{
        'users':page_obj,
        'page_obj':page_obj,
        'range': range(1,pagerange),
        'pageRange': paginator
    })

def contact(request):
    username = User.objects.all()
    
    if request.method == "POST":
        name = request.POST['txtName']
        email = request.POST['txtEmail']
        phn = request.POST['txtPhone']
        msg = request.POST['txtMsg']

        contact = Contact(name=name, email=email, phn=phn, msg=msg)
        contact.save()
        messages.success(request, "Your Message has been Sent")
        return redirect('/')




    return render(request, 'home/contact.html',{
        'userProfile':userProfile
    })

def signup(request):
    return render(request, 'home/signup.html')

def handleSignup(request):
    
    if request.method == 'POST':
        user = User.objects.all()
        
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phn1=request.POST['phn1']
        phn2=request.POST['phn2']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        add1=request.POST['add1']
        add2=request.POST['add2']
        fblink=request.POST['fblink']
        age=request.POST['age']
        bg=request.POST['bg']
        #img=request.POST['file']

        profile = request.FILES['file']
        uploaded_file_url = ''
        if profile=='':
            uploaded_file_url = uploaded_file_url+'media/user.jpeg'
        else:

            fs = FileSystemStorage()
            filename = fs.save(profile.name, profile)
            uploaded_file_url = uploaded_file_url+ fs.url(filename)
            print(uploaded_file_url)

         # check for errorneous input
        if len(username)>12:
            messages.error(request, " Your user name must be under 12 characters")
            return redirect('/signup')
        if User.objects.filter(username = username).first() :
            messages.error(request, "This username is already taken")
            return redirect('/signup')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/signup')

       
        
        #Create Users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
    
        messages.success(request, " Your Donor Account has been successfully created")
        profile = UserProfile(username=username,fname=fname, lname=lname, email=email, phn1=phn1,phn2=phn2,add1=add1,add2=add2,fblink=fblink ,age=age,bg=bg,img=filename)
        profile.save()

        user=authenticate(username= username, password= pass1)
        login(request,user)
        
        return redirect('/')
    else:
        return HttpResponse("404 - Not found")

def loginpage(request):
    return render(request, 'home/login.html')

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("/login")

    return HttpResponse("404- Not found")
   

    return HttpResponse("/login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def userProfile(request, user):
    profile = UserProfile.objects.filter(username=user)
   
    return render(request, 'home/user-profile.html', {
        'profile':profile,
    })

def editProfile(request):
    profile = UserProfile.objects.filter(username=request.user)

    if (len(profile)==0):
        messages.warning(request, "Please login to your account")
        return redirect('/')
    else:
        if(request.method == "POST"):
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phn1 = request.POST['phn1']
            phn2 = request.POST['phn2']
            add1 = request.POST['add1']
            add2 = request.POST['add2']
            bg = request.POST['bg']
            age = request.POST['age']
            fblink = request.POST['fblink']
            

            UserProfile.objects.update_or_create(username=username,
            defaults={
                'fname':fname,
                'lname':lname,
                'email':email,
                'phn1':phn1,
                'phn2':phn2,
                'add1':add1,
                'add2':add2,
                'bg':bg,
                'age':age,
                'fblink':fblink,
                

            })

            messages.success(request, 'Your Personal Information has been Updated!')
            return redirect(f'/users/{request.user}')
            
    


        return render(request, 'home/editProfile.html',{
                'profiles': profile
            })
    


def uploadPic(request):

    if(request.method == "POST"):
        img = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_url = fs.url(filename)

        UserProfile.objects.update_or_create(username=request.user,
            defaults={
                'img':filename,
            })
        messages.success(request, 'Your Profile Picture has been Updated!')
        return redirect(f'/users/{request.user}')

    return HttpResponse("ERROR")
   
def DltProfile(request):

    try:
        UserProfile.objects.filter(username=request.user).delete()
        u = User.objects.get(username = request.user)
        u.delete()
        messages.success(request, 'Your Profile Has been Deleted')
        return redirect('/')          

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('/')

    except Exception as e: 
        return HttpResponse(f'{e}')

    


    



def search(request):
    query = request.GET.get('Search')

    
    result = UserProfile.objects.filter(bg__icontains=query)|UserProfile.objects.filter(add1__icontains=query)|UserProfile.objects.filter(fname__icontains=query)|UserProfile.objects.filter(lname__icontains=query)|UserProfile.objects.filter(add2__icontains=query)

    params={'result': result, 'query':query}
    return render(request, 'home/search.html', params)



def donorStory(request,user):
    profile = UserProfile.objects.filter(username=user).first()

    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        phn = request.POST['Phone']
        msg = request.POST['Msg']
        img = request.POST['img']

        if len(msg)<16:
            messages.warning(request, "Sorry, your message is too brief to be shared. Please provide a message with at least 16 words.")
        else:
            story = DonorStory(name=name, email=email, phn=phn, msg=msg, imgname=img )
            story.save()
            messages.success(request, "Your Message has been Sent")
            return redirect('/')

    return render(request, 'home/story.html',{
        'profile':profile,
    })