from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request, 'home.html') 

def authView(request):
    if request.method == 'POST':  #  عدلنا  'post'  لـ  'POST'
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')  #  أضفنا  return redirect  هنا
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})