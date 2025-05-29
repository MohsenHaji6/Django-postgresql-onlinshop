from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Product, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'active']
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active')

    inlines = [
        CommentInline, 
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'active')
