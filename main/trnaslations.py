from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import Contact, About, Carousel, Category, Product, Character, Table


class CustomAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class StalkInline(TranslationStackedInline):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(About)
class ItemTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Category)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Carousel)
class ItemTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Contact)
class ItemTranslationOptions(TranslationOptions):
    fields = ('address',)


@register(Product)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'scope')


@register(Table)
class ItemTranslationOptions(TranslationOptions):
    fields = ('color',)


@register(Character)
class ItemTranslationOptions(TranslationOptions):
    fields = ('key', 'value')
