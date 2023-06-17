from django.db import models

# Create your models here.

class WordCount(models.Model):
    pk_word_count = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255,unique=True)
    count = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'word_count'
    
    def __str__(self) -> str:
        return f'{self.word}-{self.count}'