from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserSignup, UserLogin, EventForm , BookEventForm
from .models import Event , BookedEvent
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def create_event(request):
    if request.user.is_anonymous:
        return redirect('signin')
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('dashboard')

    context = {
        'form':form,
    }
    return render(request, 'create_event.html', context)

def event_update(request, event_id):
    event = Event.objects.get(id=event_id)
    if not (request.user.is_staff or request.user == event.user):
        return redirect('no-access')
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events-list')
    context = {
        "event": event,
        "form":form,
    }
    return render(request, 'event_update.html', context)

def dashboard(request):
    events = Event.objects.filter(user=request.user)
    booked = BookedEvent.objects.filter(user=request.user)

    context = {
        'events':events,
        'booked' : booked
    }
    return render(request, 'dashboard.html',context)

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)

    context = {
        'event': event
    }
    return render(request,'event_detail.html',context)


def events_list(request):
    events = Event.objects.all()
    context = {
        'events':events,
    }

    return render(request, 'events_list.html',context)

def event_book(request, event_id):
    if request.user.is_anonymous:
        return redirect('signin')
    event = Event.objects.get(id=event_id)
    form = BookEventForm()
    if request.method == "POST":
        form = BookEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.event = Event.objects.get(id=event_id)
            event.save()
            return redirect('dashboard')

    context = {
        'form':form,
        'event': event,

    }
    return render(request, 'book_event.html', context)

class Signup(View):
    form_class = UserSignup
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, "You have successfully signed up.")
            login(request, user)
            return redirect("home")
        messages.warning(request, form.errors)
        return redirect("signup")


class Login(View):
    form_class = UserLogin
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, "Welcome Back!")
                return redirect('dashboard')
            messages.warning(request, "Wrong email/password combination. Please try again.")
            return redirect("login")
        messages.warning(request, form.errors)
        return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("login")

