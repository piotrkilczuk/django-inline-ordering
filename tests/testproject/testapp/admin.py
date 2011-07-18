from django.contrib import admin
import models
from inline_ordering.admin import OrderableStackedInline #, OrderableTabularInline


class ImageInline(OrderableStackedInline):
#class ImageInline(OrderableTabularInline):
    
    """
    This _must_ be draggable. Preferably, in future versions, it should allow 
    developer to use either Tabular and Stacked inlines. 
    """
    
    model = models.Image


class TestimonialInline(admin.StackedInline):
#class TestimonialInline(admin.TabularInline):
    
    """
    This _cannot_ be draggable. 
    """
    
    model = models.Testimonial


class GalleryAdmin(admin.ModelAdmin):
    
    model = models.Gallery
    inlines = (ImageInline, TestimonialInline,)
    
#    class Media:
#        js = (
#            'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js',
#            'http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js',
#        )


admin.site.register(models.Gallery, GalleryAdmin)