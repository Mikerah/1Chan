from django.shortcuts import render
from .models import *

def index(request):
    list_of_boards = Board.objects.all()
    return render(request, 'channels/index.html', {'list_of_boards': list_of_boards})
    
def board(request):
    pass
