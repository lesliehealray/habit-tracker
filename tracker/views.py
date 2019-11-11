from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from tracker.models import Habit, Log
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tracker.serializers import LogSerializer, CommentSerializer
from django.http import Http404

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

def habit_detail(request, slug):
    habit = get_object_or_404(Habit, slug=slug)
    return render(request, 'habit_detail.html',{
        'habit': habit,
    })

def create_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect(to='home')
    else:
        form = HabitForm()
    
    return render(request, "create_habit.html", {"form": form})

class LogEdit(UpdateView):
    model = Log
    fields = ['log_number_completed', 'log_detail']

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'log_edit_success.html', {'log': self.object})

def log_entry(request, slug, pk):
    log = get_object_or_404(Log, id=pk)
    habit = get_object_or_404(Habit, slug=slug)
    if log.habit.slug != habit.slug:
        raise Http404
    return render(request, 'log_entry.html', {
        'log': log,
    })

def get_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    log = get_object_or_404(Log, id=pk)
    if comment.log.id != log.id:
        raise Http404
    return render(request,'log_entry.html'), {
        'comment': comment,
    }

class logapi(APIView):
    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        log = self.get_object(pk)
        log_serializer = LogSerializer(log)
        return Response(log_serializer.data)

    def put(self, request, pk, format=None):
        log = self.get_object(pk)
        serializer = LogSerializer(log, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


