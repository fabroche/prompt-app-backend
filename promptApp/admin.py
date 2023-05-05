from django.contrib import admin

# Register your models here.
from promptApp.models.prompt.prompt import Prompt
from promptApp.models.user.user import User

admin.site.register(Prompt)
admin.site.register(User)
