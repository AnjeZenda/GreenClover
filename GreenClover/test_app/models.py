from django.db import models
import json

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    style = models.CharField(default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

class Info(models.Model):
    dates = models.CharField(max_length=300)
    is_free = models.BooleanField(default=False)
    km = models.PositiveIntegerField()

    def set_dates(self, dates):
        self.dates = json.dumps(dates)
    
    def get_dates(self):
        return json.loads(self.dates)
    