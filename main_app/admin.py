from django.contrib import admin
from .models import DishCategory, Dishes, Whyus, Chefs, Gallery, Special, Events, Reviews, Contact, BookTable, About
# Register your models here.


class DishInLine(admin.TabularInline):
    model = Dishes

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_visible')
    list_filter = ('is_visible',)
    list_editable = ('position', 'is_visible')
    inlines = (DishInLine,)



@admin.register(Dishes)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title','position','ingredients','price',
                    'category','is_visible','photo', 'discount')

    list_filter = ('is_visible',)

    list_editable = ('ingredients','price','position',
                    'category','is_visible','photo', 'discount')


@admin.register(Whyus)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'position')
    list_editable =('desc', 'position')



@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):

    list_display = ('title', 'position', 'desk',
                    'ingredients', 'photo', 'is_visible')

    list_filter = ('is_visible',)

    list_editable = ('position', 'desk',
                    'ingredients', 'photo', 'is_visible')


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_visible')

    list_filter = ('is_visible',)

    list_editable = ('is_visible',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('position', 'photo', 'is_visible')

    list_filter = ('is_visible',)

    list_editable = ('photo', 'is_visible')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ('is_proccesed',)


@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'people', 'message')
    list_filter = ('is_processed',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'photo')
