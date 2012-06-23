======================
django-inline-ordering
======================

This app aims at easing implementing drag & drop reordering of inline data in 
Django Admin. 

Recent version of `Grappelli <http://code.google.com/p/django-grappelli/>`_ includes 
drag and drop inlines, so if you are already using Grappelli, installing 
django-inline-ordering does not make sense. If you didn't evaluate Grappelli yet,
I encourage you to do so!

The django-inline-ordering is being tested during development on: 

- Firefox 3.5+
- Internet Explorer 7+
- Google Chrome 10+
- Opera 11+ 

Suggestions on how to improve django-inline-ordering are very welcome.

Installation
------------

1. Put 'inline_ordering' on your python path

2. Add 'inline_ordering' to INSTALLED_APPS tuple in settings file 

Usage
-----

For each model that you want to be reorderable with drag & drop, you need to 
setup an admin class and slightly modify model declaration. This way you can 
easily apply reordering to existing model classes. You'll also have to run 
``collectstatic`` task or copy one file to your MEDIA_ROOT when using Django 
< 1.3.

Let's start with a simple example: Gallery has many Images. User might 
want to reorder the photos in the gallery to fit his likings.

1. Setup your admin inline class to inherit after OrderableStackedInline
   
   ::
     
     from inline_ordering.admin import OrderableStackedInline
     
     
     class ImageInline(OrderableStackedInline):
    
       model = Image 
     
     
     class GalleryAdmin(ModelAdmin):
         
         model = Gallery
         inlines = (ImageInline, )

2. Setup your model to inherit after Orderable
   
   ::
   
     from inline_ordering.models import Orderable
     
     class Image(Orderable):
       src = models.ImageField(upload_to='gallery/images')
       title = models.CharField(max_length=255)
       alt = models.TextField()
     
     class Meta(Orderable.Meta):
       pass
    
   As ordering column was named ``inline_ordering_position``, avoid using
   this name in your model.

   The Meta class declaration is NOT necessary - add it only if you need to set
   your own meta attributes. 
    
3. Make ``inline_ordering.js`` accessible over HTTP

   Since Django 1.3, there is a `staticfiles app`_ that django-inline-ordering is 
   aware of. Just run ``manage.py collectstatic`` to copy/symlink media files.
   
   The simplest way, back in Django 1.2, was to copy
   ``media/inline_ordering.js`` to your ``MEDIA_ROOT``.

   If you however believe that would make a mess, take advantage of the 
   'INLINE_ORDERING_JS' setting and set it to a location which should be requested 
   when accessing orderable inlines:

   ``INLINE_ORDERING_JS = STATIC_URL + '/js/third_party/inline_ordering.js'``

.. _staticfiles app: http://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/

Known issues
------------

1. Reordering won't work for new records until saved. This needs a onchange 
   handler for the record form or some model refactoring. 

2. At this point there is no support for tabular inlines. If you would like to 
   approach this problem, fork the project on Github.

Development
-----------

A simple test project has been added in fdc2189 under tests/testproject. Use 
tools/buildenv.sh to build a virtualenv for development and syncdb to create 
necessary models and admin permissions.

Version 1.0.1 is likely to be the last one, as I'm planning to release a new
library to support ordering in Django admin both of inlines as well as on the
change list. 

Kudos
-----
simon for http://djangosnippets.org/snippets/1053/