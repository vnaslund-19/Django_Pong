from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pong/index.html')

def play_1v1(request):
    return render(request, 'pong/1v1.html')

def play_AI(request):
    return render(request, 'pong/1vAI.html')

def spectate(request):
    return render(request, 'pong/AIvsAI.html')