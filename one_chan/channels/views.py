from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    list_of_boards = Board.objects.all()
    return render(request, 'channels/index.html', {'list_of_boards': list_of_boards})
    
def board(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    context = {'board': board}
    return render(request, 'channels/board.html', context)
