from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
    
class CommentsActiveManager(models.Manager):
    def get_queryset(self):
        return super(CommentsActiveManager, self).get_queryset().filter(active=True)
    
class Comment(models.Model):
    PRODUCT_STAR = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('average')),
        ('4', _('good')),
        ('5', _('very good')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',
                                verbose_name=_('product'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                related_name='comments', verbose_name=_('author'))
    body = models.TextField(verbose_name=_('Comment'))
    active = models.BooleanField(default=True, verbose_name=_('actives'))
    star = models.CharField(max_length=10, choices=PRODUCT_STAR, verbose_name=_('Enter your score'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # Manager
    objects = models.Manager()
    comments_active_manager = CommentsActiveManager()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])