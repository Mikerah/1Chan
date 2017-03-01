from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    list_of_boards = Board.objects.all()
    return render(request, 'channels/index.html', {'list_of_boards': list_of_boards})
    
def board(request, board_name):
    board = get_object_or_404(Board, board_name=board_name)
    context = {'board': board}
    return render(request, 'channels/board.html', context)
