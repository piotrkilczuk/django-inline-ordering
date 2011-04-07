from django.contrib.admin import TabularInline, StackedInline


class OrderableStackedInline(StackedInline):
    
    """Adds necessary media files to regular Django StackedInline"""
    
    class Media:
        js = ('inline_ordering.js',)


class OrderableTabularInline(TabularInline):
    
    """Adds necessary media files to regular Django TabularInline"""
    
    class Media:
        js = ('inline_ordering.js',)
