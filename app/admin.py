from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from import_export.admin import ExportActionMixin

class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    pass
# Register your models here.
from import_export import resources
from app.models import Book, Author, Category

admin.site.register(Author)
admin.site.register(Category)


class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)
        fields = (
            'id',
            'name',
            'author',
            'author_email',
            'imported',
            'published',
            'price',
            'categories',
        )
     

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Book, BookAdmin)