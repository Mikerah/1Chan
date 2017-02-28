from django.forms import ModelForm
from channels.models import Board, Thread, Reply

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_title', 'author', 'thread_post']
    
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['author', 'reply']