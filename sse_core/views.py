from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.http import HttpResponse
# Create your views here.

# The default home page
def index(request):
    return render(request, 'index.html')

# The signup page and actions
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #pass
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, "Username already taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()

                # Log user in and redirect to settings page

                # Create a profile object for the new user
                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user = user_model, id_user = user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

# The Account settings page
def setting(request):
    return render(request, 'setting.html')

# The Account settings page
def dashboard(request):
    return render(request, 'dashboard.html')

# The signin page
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('python_1')
        
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('signin')


    else:
        return render(request, 'signin.html')



# The profile page
def profile(request):
    return render(request, 'profile.html')




# Python views. This has links to all the Python pages
def python_1_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_1_1.html')

def python_1_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_1_2.html')


def python_1_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_1_3.html')

def python_1_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_1_4.html')

def python_2_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_2_1.html')

def python_2_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_2_2.html')

def python_2_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_2_3.html')

def python_2_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_2_4.html')

def python_3_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_3_1.html')

def python_3_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_3_2.html')

def python_3_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_3_3.html')

def python_3_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_3_4.html')

def python_4_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_1.html')

def python_4_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_2.html')

def python_4_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_3.html')

def python_4_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_4.html')

def python_5_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_5_1.html')

def python_5_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_5_2.html')

def python_5_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_5_3.html')

def python_5_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_5_4.html')

def python_6_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_6_1.html')

def python_6_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_6_2.html')

def python_6_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_6_3.html')

def python_6_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_6_4.html')

def python_7_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_7_1.html')

def python_7_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_7_2.html')

def python_7_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_7_3.html')

def python_7_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_7_4.html')

def python_8_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_8_1.html')

def python_8_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_8_2.html')

def python_8_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_8_3.html')

def python_8_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_8_4.html')

def python_9_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_9_1.html')

def python_9_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_9_2.html')

def python_9_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_9_3.html')

def python_9_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_9_4.html')

def python_10_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_10_1.html')

def python_10_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_10_2.html')

def python_10_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_10_3.html')

def python_10_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_10_4.html')

def python_11_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_11_1.html')

def python_11_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_11_2.html')

def python_11_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_11_3.html')

def python_11_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_11_4.html')

def python_12_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_12_1.html')

def python_12_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_12_2.html')

def python_12_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_12_3.html')

def python_12_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_12_4.html')

def python_13_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_13_1.html')

def python_13_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_13_2.html')

def python_13_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_13_3.html')

def python_13_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_13_4.html')

def python_14_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_14_1.html')

def python_14_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_14_2.html')

def python_14_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_14_3.html')

def python_14_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_14_4.html')

def python_15_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_15_1.html')

def python_15_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_15_2.html')

def python_15_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_15_3.html')

def python_15_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_15_4.html')

def python_16_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_16_1.html')

def python_16_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_16_2.html')

def python_16_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_16_3.html')

def python_16_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_16_4.html')

def python_17_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_17_1.html')

def python_17_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_17_2.html')

def python_17_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_17_3.html')

def python_17_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_17_4.html')

def python_18_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_18_1.html')

def python_18_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_18_2.html')

def python_18_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_18_3.html')

def python_18_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_18_4.html')

def python_19_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_19_1.html')

def python_19_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_19_2.html')

def python_19_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_19_3.html')

def python_19_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_19_4.html')

def python_20_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_20_1.html')

def python_20_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_20_2.html')

def python_20_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_20_3.html')

def python_20_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_20_4.html')

def python_21_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_21_1.html')

def python_21_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_21_2.html')

def python_21_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_21_3.html')

def python_21_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_21_4.html')

def python_22_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_22_1.html')

def python_22_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_22_2.html')

def python_22_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_22_3.html')

def python_22_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_22_4.html')

def python_23_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_23_1.html')

def python_23_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_23_2.html')

def python_23_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_23_3.html')

def python_23_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_23_4.html')

def python_24_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_1.html')

def python_24_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_2.html')

def python_24_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_3.html')

def python_24_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_4_4.html')

def python_25_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_25_1.html')

def python_25_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_25_2.html')

def python_25_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_25_3.html')

def python_25_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_25_4.html')

def python_26_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_26_1.html')

def python_26_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_26_2.html')

def python_26_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_26_3.html')

def python_26_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_26_4.html')

def python_27_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_27_1.html')

def python_27_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_27_2.html')

def python_27_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_27_3.html')

def python_27_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_27_4.html')

def python_28_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_28_1.html')

def python_28_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_28_2.html')

def python_28_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_28_3.html')

def python_28_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_28_4.html')

def python_29_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_29_1.html')

def python_29_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_29_2.html')

def python_29_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_29_3.html')

def python_29_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_29_4.html')

def python_30_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_30_1.html')

def python_30_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_30_2.html')

def python_30_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_30_3.html')

def python_30_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_30_4.html')

def python_31_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_31_1.html')

def python_31_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_31_2.html')

def python_31_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_31_3.html')

def python_31_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_31_4.html')

def python_32_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_32_1.html')

def python_32_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_32_2.html')

def python_32_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_32_3.html')

def python_32_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_32_4.html')

def python_33_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_33_1.html')

def python_33_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_33_2.html')

def python_33_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_33_3.html')

def python_33_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_33_4.html')

def python_34_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_34_1.html')

def python_34_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_34_2.html')

def python_34_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_34_3.html')

def python_34_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_34_4.html')

def python_35_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_35_1.html')

def python_35_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_35_2.html')

def python_35_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_35_3.html')

def python_35_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_35_4.html')

def python_36_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_36_1.html')

def python_36_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_36_2.html')

def python_36_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_36_3.html')

def python_36_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_36_4.html')

def python_37_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_37_1.html')

def python_37_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_37_2.html')

def python_37_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_37_3.html')

def python_37_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_37_4.html')

def python_38_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_38_1.html')

def python_38_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_38_2.html')

def python_38_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_38_3.html')

def python_38_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_38_4.html')

def python_39_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_39_1.html')

def python_39_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_39_2.html')

def python_39_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_39_3.html')

def python_39_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_39_4.html')

def python_40_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_40_1.html')

def python_40_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_40_2.html')

def python_40_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_40_3.html')

def python_40_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_40_4.html')

def python_41_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_1.html')

def python_41_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_2.html')

def python_41_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_3.html')

def python_41_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_4.html')

def python_42_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_42_1.html')

def python_42_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_42_2.html')

def python_42_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_42_3.html')

def python_42_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_42_4.html')
 
def python_43_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_1.html')

def python_43_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_2.html')

def python_43_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_3.html')

def python_43_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_41_4.html')
 
def python_44_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_44_1.html')

def python_44_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_44_2.html')

def python_44_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_44_3.html')

def python_44_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_44_4.html')
 
def python_45_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_45_1.html')

def python_45_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_45_2.html')

def python_45_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_45_3.html')

def python_45_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_45_4.html')
 
def python_46_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_46_1.html')

def python_46_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_46_2.html')

def python_46_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_46_3.html')

def python_46_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_46_4.html')
 
def python_47_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_47_1.html')

def python_47_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_47_2.html')

def python_47_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_47_3.html')

def python_47_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_47_4.html')
 
def python_48_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_48_1.html')

def python_48_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_48_2.html')

def python_48_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_48_3.html')

def python_48_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_48_4.html')
 
def python_49_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_49_1.html')

def python_49_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_49_2.html')

def python_49_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_49_3.html')

def python_49_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_49_4.html')
 

def python_50_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_50_1.html')

def python_50_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_50_2.html')

def python_50_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_50_3.html')

def python_50_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_50_4.html')
 
def python_51_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_51_1.html')

def python_51_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_51_2.html')

def python_51_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_51_3.html')

def python_51_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_51_4.html')
 

def python_52_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_52_1.html')

def python_52_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_52_2.html')

def python_52_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_52_3.html')

def python_52_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_52_4.html')
 
def python_53_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_53_1.html')

def python_53_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_53_2.html')

def python_53_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_53_3.html')

def python_53_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_53_4.html')

def python_54_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_54_1.html')

def python_54_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_54_2.html')

def python_54_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_54_3.html')

def python_54_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_54_4.html')

def python_55_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_55_1.html')

def python_55_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_55_2.html')

def python_55_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_55_3.html')

def python_55_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_55_4.html')

def python_56_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_56_1.html')

def python_56_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_56_2.html')

def python_56_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_56_3.html')

def python_56_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_56_4.html')

def python_57_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_57_1.html')

def python_57_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_57_2.html')

def python_57_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_57_3.html')

def python_57_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_57_4.html')

def python_58_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_58_1.html')

def python_58_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_58_2.html')

def python_58_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_58_3.html')

def python_58_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_58_4.html')

def python_59_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_59_1.html')

def python_59_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_59_2.html')

def python_59_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_59_3.html')

def python_59_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_59_4.html')

def python_60_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_60_1.html')

def python_60_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_60_2.html')

def python_60_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_60_3.html')

def python_60_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_60_4.html')

def python_61_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_61_1.html')

def python_61_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_61_2.html')

def python_61_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_61_3.html')

def python_61_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_61_4.html')

def python_62_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_62_1.html')

def python_62_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_62_2.html')

def python_62_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_62_3.html')

def python_62_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_62_4.html')

def python_63_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_63_1.html')

def python_63_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_63_2.html')

def python_63_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_63_3.html')

def python_63_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_63_4.html')

def python_64_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_64_1.html')

def python_64_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_64_2.html')

def python_64_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_64_3.html')

def python_64_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_64_4.html')

def python_65_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_65_1.html')

def python_65_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_65_2.html')

def python_65_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_65_3.html')

def python_65_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_65_4.html')

def python_66_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_66_1.html')

def python_66_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_66_2.html')

def python_66_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_66_3.html')

def python_66_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_66_4.html')

def python_67_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_67_1.html')

def python_67_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_67_2.html')

def python_67_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_67_3.html')

def python_67_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_67_4.html')

def python_68_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_68_1.html')

def python_68_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_68_2.html')

def python_68_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_68_3.html')

def python_68_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_68_4.html')

def python_69_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_69_1.html')

def python_69_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_69_2.html')

def python_69_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_69_3.html')

def python_69_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_69_4.html')

def python_70_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_70_1.html')

def python_70_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_70_2.html')

def python_70_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_70_3.html')

def python_70_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_70_4.html')

def python_71_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_71_1.html')

def python_71_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_71_2.html')

def python_71_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_71_3.html')

def python_71_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_71_4.html')

def python_72_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_72_1.html')

def python_72_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_72_2.html')

def python_72_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_72_3.html')

def python_72_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_72_4.html')

def python_73_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_73_1.html')

def python_73_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_73_2.html')

def python_73_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_73_3.html')

def python_73_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_73_4.html')

def python_74_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_74_1.html')

def python_74_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_74_2.html')

def python_74_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_74_3.html')

def python_74_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_74_4.html')

def python_75_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_75_1.html')

def python_75_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_75_2.html')

def python_75_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_75_3.html')

def python_75_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_75_4.html')

def python_76_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_76_1.html')

def python_76_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_76_2.html')

def python_76_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_76_3.html')

def python_76_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_76_4.html')

def python_77_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_77_1.html')

def python_77_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_77_2.html')

def python_77_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_77_3.html')

def python_77_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_77_4.html')

def python_78_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_78_1.html')

def python_78_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_78_2.html')

def python_78_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_78_3.html')

def python_78_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_78_4.html')

def python_79_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_79_1.html')

def python_79_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_79_2.html')

def python_79_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_79_3.html')

def python_79_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_79_4.html')

def python_80_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_80_1.html')

def python_80_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_80_2.html')

def python_80_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_80_3.html')

def python_80_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_80_4.html')

def python_81_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_81_1.html')

def python_81_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_81_2.html')

def python_81_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_81_3.html')

def python_81_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_81_4.html')

def python_82_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_82_1.html')

def python_82_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_82_2.html')

def python_82_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_82_3.html')

def python_82_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_82_4.html')

def python_83_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_83_1.html')

def python_83_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_83_2.html')

def python_83_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_83_3.html')

def python_83_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_83_4.html')

def python_84_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_84_1.html')

def python_84_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_84_2.html')

def python_84_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_84_3.html')

def python_84_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_84_4.html')

def python_85_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_85_1.html')

def python_85_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_85_2.html')

def python_85_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_85_3.html')

def python_85_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_85_4.html')

def python_86_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_86_1.html')

def python_86_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_86_2.html')

def python_86_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_86_3.html')

def python_86_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_86_4.html')

def python_87_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_87_1.html')

def python_87_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_87_2.html')

def python_87_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_87_3.html')

def python_87_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_87_4.html')

def python_88_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_88_1.html')

def python_88_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_88_2.html')

def python_88_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_88_3.html')

def python_88_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_88_4.html')

def python_89_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_89_1.html')

def python_89_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_89_2.html')

def python_89_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_89_3.html')

def python_89_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_89_4.html')

def python_90_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_90_1.html')

def python_90_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_90_2.html')

def python_90_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_90_3.html')

def python_90_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'python_90_4.html')





# Cpp views. This has links to all the Cpp pages
def Cpp_1_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'Cpp_1_1.html')

def Cpp_2_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'Cpp_2_1.html')

def Cpp_3_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'Cpp_3_1.html')

def Cpp_4_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'Cpp_4_1.html')

def Cpp_5_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'Cpp_5_1.html')

def Cpp_6_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'Cpp_6_1.html')




# C views. This has links to all the Cpp pages
def C_1_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'C_1_1.html')

def C_2_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'C_2_1.html')

def C_3_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'C_3_1.html')

def C_4_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'C_4_1.html')

def C_5_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'C_5_1.html')

def C_6_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'C_6_1.html')





# Embedded C pages
def embedded_c(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'embedded_c.html')

def day_1(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'intro.html')

def day_2(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_2_var.html')

def day_3(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_3_address_var.html')

def day_4(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_4_func.html')

def day_5(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_5_microcontrollers.html')

def day_6(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_6_build_process.html')

def day_7(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_7_float.html')

def day_8(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_8_pointers.html')

def day_9(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_9_operators.html')

def day_10(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_10_decision_making.html')

def day_11(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_11_bitwise.html')

def day_12(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_12_blink.html')

def day_13(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_13_shift_operators.html')

def day_14(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_14_looping.html')

def day_15(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_15_type_qualifier.html')

def day_16(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_16_pinread.html')

def day_17(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_17_volatile.html')

def day_18(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_18_structures.html')

def day_19(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_19_usage_of_bitfield.html')

def day_20(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_20_keypad_interfacing.html')

def day_21(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_21_Arrays.html')

def day_22(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_22_strings.html')

def day_23(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_23_pre_processor.html')

def day_24(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_24_lcd_programming.html')

def day_25(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_25_uart.html')

def day_26(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_26_spi_tft.html')

def day_27(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_27_interview_questions.html')

def day_28(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_28_spi_adc.html')

def day_29(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_29_interview_questions.html')

def day_30(request):
    # write code to make sure this page is only returned after signin
    return render(request, 'day_30_graduation.html')