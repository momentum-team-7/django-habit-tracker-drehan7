from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect
from .models import Profile, User
from .forms import ProfileForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@login_required
def home_page(request):
    profiles = Profile.objects.all()
    current_user = User.objects.get(pk = request.user.pk)
    if current_user not in [profile.user for profile in profiles]:
        return HttpResponseRedirect('/create_profile')
    
    profile = Profile.objects.get(user = request.user)

    return render(request, 'home_page.html', {'profile': profile})

def create_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, initial={'user':user})
        if form.is_valid():
            profile = Profile.objects.create(
                user = user,
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name']
            )
            profile.save()
        return HttpResponseRedirect('/home/')
    else:
        form = ProfileForm(request.POST, initial={'user':user})

    return render(request, 'create_profile.html', {'form':form})