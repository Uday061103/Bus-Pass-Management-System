from django.shortcuts import render,redirect
from django.contrib import messages
from students.models import studentregistermodel

# Create your views here.
def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})


def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)

        # Hardcoded login check
        if usrid == 'admin' and pswd == 'admin':
            # Store user_name in session
            request.session['user_name'] = usrid
            print("Session stored with user_name:", request.session.get('user_name'))  # Debugging line
            return redirect(AdminHome)  # Redirect to Admin Home page
        else:
            messages.success(request, 'Please Check Your Login Details')

    return render(request, 'AdminLogin.html', {})

def AdminHome(request):
    user_name = request.session.get('user_name', None)
    return render(request, 'admins/AdminHome.html',{'user_name': user_name})

def RegisterUsersView(request):
    data = studentregistermodel.objects.all()
    user_name = request.session.get('user_name', None)
    return render(request,'admins/viewregisterusers.html',{'data':data,'user_name': user_name})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        user_name = request.session.get('user_name', None)
        status = 'activated'
        print("PID = ", id, status)
        studentregistermodel.objects.filter(id=id).update(status=status)
        data = studentregistermodel.objects.all()
        return render(request,'admins/viewregisterusers.html',{'data':data,'user_name': user_name})   

def deActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        user_name = request.session.get('user_name', None)
        status = 'waiting'
        print("PID = ", id, status)
        studentregistermodel.objects.filter(id=id).update(status=status)
        data = studentregistermodel.objects.all()
        return render(request,'admins/viewregisterusers.html',{'data':data,'user_name': user_name})


from django.shortcuts import render, redirect
from .models import Route
from .forms import RouteForm

def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            form = RouteForm()
            messages.success(request,'route added succefully')
  # Redirect to a route list page after saving
    else:
        form = RouteForm()
    return render(request, 'admins/route_form.html', {'form': form})

def viewroutes(request):
    routes = Route.objects.all()
    return render(request,'admins/routes.html',{'routes':routes})    

def edit_route(request, pk):
    route = Route.objects.get(pk=pk)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'admins/route_form.html', {'form': form})
