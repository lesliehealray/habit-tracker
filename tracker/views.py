from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from tracker.models import Habit, Log
from django.shortcuts import render, redirect, get_object_or_404


from tracker.forms import CustomUserCreationForm, HabitForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'home.html', {
        'habits': habits,
    })

def log_list(request):
    logs = Log.objects.all()
    return render(request, 'log_list.html',{
        'logs': logs,
    })

def create_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect(to=habit)
    else:
        form = HabitForm()
    
    return render(request, "create_habit.html", {"form": form})