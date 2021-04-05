from django.contrib import admin

# Register your models here.
from .models import Experiment, Content, Vote

admin.site.register(Experiment)
admin.site.register(Content)
admin.site.register(Vote)
