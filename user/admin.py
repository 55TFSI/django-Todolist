from django.contrib import admin

# Register your models here.
from user.models import Quote, Article

admin.site.register(Quote)
admin.site.register(Article)