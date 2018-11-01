from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # since is one person we use 'auth.user'
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # the true means it can be blank if you dont what publish it yet or put nlll
    published_date = models.DateTimeField(blank=True,null=True)

    # publication method
    def publish(self):
        # grab published_date to be equal to timezone
        self.published_date = timezone.now()
        self.save()

    # grab those comment filter  them if truly approved comment
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # idea behind it after someone create a post or a comment where should the web site take them
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
        # go to post detail page for the primary key of the post just created

    def __str__(self):
        return self.title

class Comment(models.Model):
    # each comments is going to be connected to a blog
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    # boolean true or flase approve or not default flase it not been approved
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
