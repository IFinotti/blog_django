from django.db import models
from utils.rands import new_slugify

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
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title

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

     