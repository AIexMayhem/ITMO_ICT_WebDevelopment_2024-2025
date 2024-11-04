from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from student_desc.forms import RegisterForm

@csrf_exempt

def home(request):
    return render(request, 'home.html')


@csrf_exempt
def register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    context['form'] = form
    return render(request, 'register.html', context)

