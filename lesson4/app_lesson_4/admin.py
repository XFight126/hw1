from django.contrib import admin
from .models import Adverisement
from django.utils.html import format_html

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'description', 'price', 'auction',
                    'created_add', 'updated_add', 'image', 'image_preview']
    list_filter = ['auction', 'created_add']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description', 'image', 'user')
        }),
        ('Финансы', {
            'fields':('price', 'auction')
        })
    )
    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{url}" width="100" height="100" />', url=obj.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" width="100" height="100" />')

    
    
    # создаем действие для отключения возможности торга
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='Сделать торг уместным')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Adverisement, AdvertisementAdmin)