from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ValidationError
from .models import RequestingOrder,CustomUser,Ordershistory
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
import time
from django.http import HttpResponseRedirect





# Create your views here.

def register(request):
    if request.method == 'POST':
        try:
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # user_id = request.POST['user_id']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if not all([username, email, password, confirm_password]):
                raise ValidationError('Please fill in all required fields')

            if password != confirm_password:
                raise ValidationError('Passwords do not match')

            if CustomUser.objects.filter(username=username).exists():
                raise ValidationError('Username is already taken')

            if CustomUser.objects.filter(email=email).exists():
                raise ValidationError('Email is already registered')

            user = CustomUser.objects.create_user(
                # user_id=user_id,
                username=username,
                password=password,
                email=email,
            )
            user.set_password(password)
            user.save()

            messages.success(request, 'Account created successfully')
            return redirect('login_user')

        except ValidationError as e:
            messages.error(request, e.message)

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index.html')
        else:
            messages.info(request, 'Invalid name or password')

    return render(request, 'register.html')

def logout_user(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('index')

def index(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def services(request):
    
    return render(request, 'service-1.html')

def fuelDelivery(request):
    
    return render(request, 'fuel-delivery.html')

def enginOil(request):
    
    return render(request, 'engin-oil-service.html')

def carWash(request):
    
    return render(request, 'car-wash.html')

def battery(request):
    
    return render(request, 'battery-service.html')

def tyre(request):
    
    return render(request, 'tyre-service.html')

def towTruck(request):
    
    return render(request, 'tow-truck-service.html')


def reservation_form(request):
    if request.method == 'POST':
            brand_model = request.POST['brand_model']
            check_username = request.POST['check_username']
            arrival_date = request.POST['arrival_date']
            arrival_time = request.POST['arrival_time']
            car_id = request.POST['car_id']
            note = request.POST['note']
            the_service = request.POST['the_service']

            car = RequestingOrder(brand_model=brand_model, arrival_date=arrival_date, arrival_time=arrival_time, car_id=car_id, note=note, the_service=the_service,check_username=check_username)
            car.save()
            
            Ordershistory.objects.create(car=car, user=request.user)
            messages.success(request, 'Reservation created successfully')
            time.sleep(4)
            return redirect('orders_history')
    else:
        pass    
    return render(request, 'reservation-form.html')

def visa(request):
    return render(request, 'visa-payment.html')

def dashboard(request):
    return render(request, 'dashboard.html', {'orders':RequestingOrder.objects.all()})

def profile(request):
    if request.method == 'POST':        
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        adress = request.POST.get('adress')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postal_code = request.POST.get('postal_code')
        image = request.FILES.get('image')
        nation = request.POST.get('nation')
        about_the_user = request.POST.get('about_the_user')
        user = request.user

        if username and CustomUser.objects.filter(username=username).exclude(pk=user.pk).exists():
            messages.error(request, 'Username is already taken')
            return redirect('profile')
        
        if email and CustomUser.objects.filter(email=email).exclude(pk=user.pk).exists():
            messages.error(request, 'Email is already taken')
            return redirect('profile')
        
        if image:
            # Save the image to the default storage location
            image_path = default_storage.save('photos/{}.jpg'.format(user.pk), image)
            # Update the user's image field to point to the new image path
            user.image = image_path
        
        if username:
            user.username = username
            
        if about_the_user:
            user.about_the_user = about_the_user
        
        if email:
            user.email = email
        
        if nation:
            user.nation = nation
        
        if first_name:
            user.first_name = first_name
        
        if last_name:
            user.last_name = last_name
        
        if adress:
            user.adress = adress
        
        if city:
            user.city = city
        
        if country:
            user.country = country
        
        if postal_code:
            user.postal_code = postal_code
            
        if image:
            user.image = image
            

        
        user.save()
        messages.success(request, 'Your info updated successfully')
        return redirect('profile')

    return render(request, 'profile.html')

def orders_history(request):
    orders = Ordershistory.objects.all() 

    try:
        user = request.user
        orders = user.orders.all()
        context = {'orders': orders}
    except Exception as e:
        messages.error(request, f"Error: {e}")
        context = {'orders': orders} 

    return render(request, 'orders_history.html', context=context)













