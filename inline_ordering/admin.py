from django.contrib.admin import StackedInline

class OrderableStackedInline(StackedInline):
    
    """Adds necessary media files to regular Django StackedInline"""
    
    class Media:
        js = (
              'http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js', 
              'inline_ordering.js',
        )