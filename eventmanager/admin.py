from django.contrib import admin
from .models import Event, Comment, EventLike, CommentLike

# Register your models here.

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(EventLike)
admin.site.register(CommentLike)