from django.contrib import admin

from .models import Post
from projects.models import Project
from endpoints.models import Endpoint

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Endpoint)


