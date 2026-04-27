from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.text import slugify
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
class Article(models.Model):
    # BASIC INFO
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    # CONTENT
    content = HTMLField()
    excerpt = models.TextField(max_length=300, blank=True)
    article_background = models.TextField(max_length=5000)
    background = models.TextField(max_length=5000)
    # RELATIONS
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, blank=True)
    # STATUS
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    # ANALYTICS
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    # TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_published and not self.published_at:
            from django.utils import timezone
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title