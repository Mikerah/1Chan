from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def index(request):
    list_of_boards = Board.objects.all()
    return render(request, 'channels/index.html', {'list_of_boards': list_of_boards})
    
def board(request, board_name):
    board = get_object_or_404(Board, board_name=board_name)
    if request.method == 'POST':
        new_thread_form = ThreadForm(request.POST)
        if new_thread_form.is_valid():
            new_thread = Thread(board=board, thread_title=new_thread_form.cleaned_data['thread_title'], \
                            author=new_thread_form.cleaned_data['author'], thread_post=new_thread_form.cleaned_data['thread_post'])
            new_thread.save()
            return HttpResponseRedirect('/{}'.format(board))
    else:
        new_thread_form = ThreadForm()
    context = {'board': board, 'thread_form': new_thread_form}
    return render(request, 'channels/board.html', context)
