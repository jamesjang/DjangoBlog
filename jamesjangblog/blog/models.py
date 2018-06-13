from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return super(BlogPostManager,self).get_queryset().filter(posttype='blog')

class TutorialPostManager(models.Manager):
    def get_queryset(self):
        return super(TutorialPostManager,self).get_queryset().filter(posttype='tutorial')

#post model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    CATEGORY_CHOICES = (
        ('blog' , 'Blog'),
        ('tutorial', 'Tutorial'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blog_posts')
    body = HTMLField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    posttype = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='blog')
 
  # The default manager
    objects = models.Manager()
 
    # Custom made manager
    published = PublishedManager()

    blogposts = BlogPostManager()

    tutorialposts = TutorialPostManager()


    class Meta:
        ordering = ('-publish',)
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail_view', args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.DO_NOTHING, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
# Create your models here.
