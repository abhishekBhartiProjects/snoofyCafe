from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            print('redirect is called')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    print('Invalid form')
    return render(request, 'users/register.html', {'form': form})
