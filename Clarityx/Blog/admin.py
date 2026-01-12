from django.contrib import admin
from .models import Post

class Postadmin(admin.ModelAdmin):
    list_display = ["__str__","data"]
    list_filter = ["data"]
    search_fields = ["title","contenuto"]
    prepopulated_fields = {"slug":("title",)}

    class Meta:
        model= Post

admin.site.register(Post,Postadmin)
