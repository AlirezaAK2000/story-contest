from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from first.ibm import natural_language_understanding
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from django.core.exceptions import ValidationError

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    audio_path = models.URLField(blank=True , null=True)
    image = models.ImageField(null=True , default=None , upload_to = 'post_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail' , kwargs = {'pk' : self.pk})
    
    def clean(self):
        res = natural_language_understanding.analyze(
            html=self.content,
            features=Features(emotion=EmotionOptions())).get_result()
        
        emotions = res['emotion']['document']['emotion']
        
        if emotions['anger'] > 0.5 or emotions['disgust'] > 0.5:
            raise ValidationError("Too much anger or disgust in your story.")
        

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    audio_path = models.URLField(blank=True , null=True)
    

    def clean(self):
        res = natural_language_understanding.analyze(
            html=self.content,
            features=Features(emotion=EmotionOptions())).get_result()
        
        emotions = res['emotion']['document']['emotion']
        
        if emotions['anger'] > 0.5 or emotions['disgust'] > 0.5:
            raise ValidationError("Too much anger or disgust in your comment.")
        
    def get_absolute_url(self):
        return reverse('post-detail' , kwargs = {'pk' : self.post.pk})