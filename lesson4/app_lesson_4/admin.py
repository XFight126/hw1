from django.contrib import admin
from .models import Adverisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_add', 'updated_add']
    list_filter = ['auction', 'created_add']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description')
        }),
        ('Финансы', {
            'fields':('price', 'auction')
        })
    )
    
    
    # создаем действие для отключения возможности торга
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='Сделать торг уместным')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Adverisement, AdvertisementAdmin)