from django.contrib import admin
from .models import Skill, Course, Career

# Tells Django's build in admin panel that the model exsits and should be manageable here
admin.site.register(Skill)
admin.site.register(Course)
admin.site.register(Career)
