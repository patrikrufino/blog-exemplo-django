from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', editable=False)
    tags = models.ManyToManyField('Tag', verbose_name='Tags', related_name='videos')
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name