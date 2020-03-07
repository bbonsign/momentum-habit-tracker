from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Log, Observer
from .forms import HabitForm, LogForm, ObserverForm


@login_required(login_url='/accounts/login')
def habits(request):
    user = User.objects.get(username=request.user.username)
    habits = user.habits.all()
    context = {'habits': habits}
    return render(request, 'core/habits.html', context=context)


@login_required(login_url='/accounts/login')
def habit_logs(request, pk):
    user = User.objects.get(username=request.user.username)
    habit = Habit.objects.get(pk=pk)
    logs = Log.objects.filter(owner=user, habit=habit)
    observers = habit.observers.all()
    observers_usernames = [obs.observer.username for obs in observers]
    context = {'logs': logs, 'habit': habit, 'observers': observers_usernames}
    return render(request, 'core/habit_logs.html', context=context)


@login_required(login_url='/accounts/login/')
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.owner = request.user
            habit.save()
        return redirect('habits')
    else:
        form = HabitForm()
    context = {'form': form, 'type': 'habit'}
    return render(request, 'core/add_form.html', context=context)


@login_required(login_url='/accounts/login/')
def add_log(request):
    get_habit_pk = request.GET.get('habit', -1)
    get_date = request.GET.get('date', -1)
    if request.method == "POST":
        user = request.user
        habit = Habit.objects.get(pk=request.POST['habit'])
        form = LogForm(request.POST)
        if form.is_valid():
            if Log.objects.filter(owner=user, date=request.POST['date'], habit=habit):
                form = LogForm()
                context = {'form': form, 'type': 'log', 'warning': True}
                return render(request, 'core/add_form.html', context=context)
            else:
                log = form.save(commit=False)
                log.owner = user
                log.save()
                habit_pk = log.habit.pk
                return redirect('habit_logs', habit_pk)
    else:
        if not(get_date == -1 and get_habit_pk == -1):
            habit = Habit.objects.get(pk=get_habit_pk)
            form = LogForm(initial={'habit': habit, 'date': get_date})
        else:
            form = LogForm()
    context = {'form': form, 'type': 'log'}
    return render(request, 'core/add_form.html', context=context)


@login_required(login_url='/accounts/login/')
def add_observer(request, pk):
    if request.method == "POST":
        form = ObserverForm(request.POST)
        if form.is_valid():
            habit = Habit.objects.get(pk=pk)
            if Observer.objects.filter(observer=User.objects.get(pk=request.POST['observer']), habit=habit):
                form = ObserverForm()
                context = {'form': form, 'type': 'observer', 'warning': True}
                return render(request, 'core/add_form.html', context=context)
            else:
                observer = form.save(commit=False)
                observer.habit = habit
                observer.save()
                return redirect('habit_logs', pk)
        return redirect('habit_logs', pk)
    else:
        form = ObserverForm()
    return render(request, 'core/add_form.html', {'form': form})
