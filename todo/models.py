from django.db import models

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
#words, 'danger', 'info', 'success' correspond to the bootstrap colors for buttons!!
# Create your models here.
class TodoModel(models.Model): # I made a table with this class and from models.Model
    title = models.CharField(max_length=100) # insdie models. there are nuemrous fields. the fields let you decide that the data inside the tablew will be texts.
      # you also have to set (max_length = something) otherwises it will throw an error.
    memo = models.TextField()
    #models.TextField()is used when the text data will be long wherea modesl.CharField is used when the text data is not that long, such that just a title.
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title
