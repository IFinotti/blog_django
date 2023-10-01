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
