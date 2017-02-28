from django.db import models

class Board(models.Model):
    board_name = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.board_name)
    
class Thread(models.Model):
    board = models.ForeignKey(Board)
    thread_title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    thread_post = models.TextField()
    
    def __str__(self):
        return str(self.thread_title)
    
class Reply(models.Model):
    thread = models.ForeignKey(Thread)
    author = models.CharField(max_length=100)
    reply = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
