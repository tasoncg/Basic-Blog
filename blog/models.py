from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    content=models.TextField(max_length=5000,help_text='You are only allowed to post charecters')
    pub_date = models.DateField(default=date.today)
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog-detail',args=[str(self.id)])
    class Meta:
        ordering=['-pub_date']

class Author(models.Model):
    name=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    information=models.CharField(max_length=1000)


    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])
    def __str__(self):
        return self.name.username

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    content=models.TextField(max_length=1000)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE)
    post_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['post_date']
    def __str__(self):
        if len(self.content)>75:
            title=self.content[:75]+'...'
        else: title=self.content
        return title




