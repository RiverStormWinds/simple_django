from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, ProvInfo
from booktest.models import HeroInfo
from django.contrib import admin

list_display = ['btitle', 'bpub_date']


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


# @admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

    fields = ['bpub_date', 'btitle']

    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]

    # list_display = ['id', 'name', 'gender', 'hcontent']


class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]


class ProvInfoAdmin(admin.ModelAdmin):
    list_display = ['provinceid', 'province']
    list_filter = ['provinceid']
    search_fields = ['province']
    list_per_page = 10

    fields = [('provinceid', 'province')]

    # fieldsets = [
    #     ('basic', {'fields': ['btitle']}),
    #     ('more', {'fields': ['bpub_date']}),
    # ]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(ProvInfo, ProvInfoAdmin)

# admin.site.register(HeroInfo)

