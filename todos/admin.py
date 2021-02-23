from django.contrib import admin
from .models import Todo
from .models import Category
#from .models import User_Category


admin.site.register(Todo)
admin.site.register(Category)
#admin.site.register(User_Category)