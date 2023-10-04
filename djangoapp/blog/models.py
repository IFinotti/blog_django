from django.db import models
from django.contrib.auth.models import User
from utils.rands import new_slugify
from django.urls import reverse
from utils.images import resize_image
from django_summernote.models import AbstractAttachment


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name

        file_changed = False
        current_file_name = str(self.cover.name)
        
        if self.file:
            file_changed=current_file_name != self.file.name

        if file_changed:
            resize_image(self.file, 900, True, 70)
        
        return super().save(*args, **kwargs)

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True, 
        blank=True,
        max_length=255
    )

    # that method is used to overwrite the creation of a slug.
    # it saves and creates a slug automatically,
    # the user has no need to send a slug by itself
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name, 5)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True, 
        blank=True,
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True,
        default="", 
        null=False, 
        blank=True, 
        max_length=255
    )
    is_published = models.BooleanField(
        default=False, 
        help_text='This field must be marked to the page be show publicly'
    )
    content = models.TextField(default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title

class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True,
        default="", 
        null=False, 
        blank=True, 
        max_length=255
    )
    objects = PostManager()
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False, 
        help_text='This field must be marked to the post be show publicly'
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text='Do you wanna show the image cover on the post content too??'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # user.post_created_by.all
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, 
        null=True, related_name='post_created_by'
    )
    updated_at = models.DateTimeField(auto_now=True)
    # user.post_updated_by.all
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, 
        null=True, related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title, 5)

        cover_changed = False
        current_cover_name = str(self.cover.name)
        
        if self.cover:
            cover_changed=current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)
        
        return super().save(*args, **kwargs)