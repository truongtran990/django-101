from django.contrib import admin

from user.models import Book, Author, Publisher

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Book, BookAdmin)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass