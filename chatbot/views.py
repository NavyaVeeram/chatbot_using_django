from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone


open_api_key = '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'
openai.api_key = open_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer
def index(request):
    return render(request,'index.html')
def contact_us(request):
    return render(request,'contact_us.html')
def index2(request):
    return render(request,'index2.html')
def about(request):
    return render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')
def safety(request):
    return render(request,'safety.html')
def services(request):
    return render(request,'services.html')
def faqs(request):
    return render(request,'faqs.html')
@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except Exception as e:
                error_message = 'Error creating account: {}'.format(str(e))
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Passwords don\'t match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')




