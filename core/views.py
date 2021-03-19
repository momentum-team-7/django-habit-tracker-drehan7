from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Profile, User, Habit, HabitLog
from .forms import ProfileForm, HabitForm, HabitLogForm

# Create your views here.
def index(request):
    return render(request, "index.html", {})


@login_required
def home_page(request):
    profiles = Profile.objects.all()
    current_user = User.objects.get(pk=request.user.pk)
    if current_user not in [profile.user for profile in profiles]:
        return HttpResponseRedirect("/create_profile")

    profile = Profile.objects.get(user=request.user)
    habits = Habit.objects.filter(author=profile)
    habit_logs = HabitLog.objects.filter(
        habit_id__in=[habit.pk for habit in habits]
    ).order_by("-date")

    return render(
        request,
        "home_page.html",
        {"profile": profile, "habits": habits, "habit_logs": habit_logs},
    )


@login_required
def create_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, initial={"user": user})
        if form.is_valid():
            profile = Profile.objects.create(
                user=user,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            profile.save()
        return HttpResponseRedirect("/home/")
    else:
        form = ProfileForm(request.POST, initial={"user": user})

    return render(request, "create_profile.html", {"form": form})


@login_required
def add_habit(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            new_habit = Habit.objects.create(
                title=form.cleaned_data["title"],
                author=user_profile,
                description=form.cleaned_data["description"],
                goal=form.cleaned_data["goal"],
            )
            new_habit.save()
        return HttpResponseRedirect("/home/")
    else:
        form = HabitForm(request.POST)

    return render(request, "add_habit.html", {"form": form, "profile": user_profile})


@login_required
def habit_info(request, habitpk):
    habit = Habit.objects.get(pk=habitpk)
    habit_logs = HabitLog.objects.filter(habit=habit)

    return render(
        request, "habit_info.html", {"habit": habit, "habit_logs": habit_logs}
    )


def add_log(request, habitpk):
    habit = Habit.objects.get(pk=habitpk)
    if request.method == "POST":
        form = HabitLogForm(request.POST, initial={"habit": habit})
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(f"/home/habit_info/{habitpk}/")
    else:
        form = HabitLogForm(request.POST, initial={"habit_id": habit.pk})

    return render(request, "add_log.html", {"form": form, "habit": habit})
