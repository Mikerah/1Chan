from django.db import models

class Board(models.Model):
    board_name = models.CharField(max_length=30)
    
class Thread(models.Model):
    board = models.ForeignKey(Board)
    thread_title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    thread_post = models.TextField()
    
class Reply(models.Model):
    thread = models.ForeignKey(Thread)
    author = models.CharField(max_length=100)
    reply = models.TextField()
    
