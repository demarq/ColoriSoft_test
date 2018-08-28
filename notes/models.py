from django.db import models
import re

class Notes(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50, default='Where is my Title? :(')
    text = models.CharField(verbose_name='Note', max_length=300, default='Where is my Text? :(')
    unique_symbols = models.IntegerField(verbose_name='Unique symbols counter', default=0)

    @staticmethod
    def calc_uniq_symbols(text=None):
        print(text)
        if text:
            return len(set(re.sub('[^a-zA-Zа-яА-Я\s]', ' ', text).split(' ')))
        else:
            return 0

    def __str__(self):
        return '%s : %s' % (self.title, self.unique_symbols)

