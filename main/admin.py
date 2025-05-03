from django.contrib import admin
from django.utils.html import format_html
from .trnaslations import CustomAdmin, StalkInline
from .models import About, Contact, Character, Carousel, Certificate, Client, Category, Product, Table, AboutImage, \
    Phone


class AboutImageInline(admin.StackedInline):
    model = AboutImage
    extra = 1


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 1


@admin.register(About)
class AboutAdmin(CustomAdmin):
    list_display = ('text', 'display_image')
    inlines = [AboutImageInline]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Contact)
class ContactAdmin(CustomAdmin):
    list_display = ('email', 'phone', 'telegram', 'instagram', 'facebook', 'whatsapp')
    inlines = [PhoneInline]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True


class CharacterInline(StalkInline):
    model = Character
    extra = 1


class TableInline(StalkInline):
    model = Table
    extra = 1


@admin.register(Product)
class ProductAdmin(CustomAdmin):
    list_display = ('name', 'display_image', 'category')
    inlines = [CharacterInline, TableInline]

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Carousel)
class CarouselAdmin(CustomAdmin):
    list_display = ('text', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('display_image',)

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('display_image',)

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Category)
class CategoryAdmin(CustomAdmin):
    list_display = ('name', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)
