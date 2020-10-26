from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import *

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Paper)
admin.site.register(Poster)
admin.site.register(Project)
admin.site.register(Design)
admin.site.register(Use)
admin.site.register(Book)
admin.site.register(File)


