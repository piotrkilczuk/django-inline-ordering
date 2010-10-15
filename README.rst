======================
django-inline-ordering
======================

This app aims at easing implementing drag & drop reordering of inline data in 
Django Admin. 

Recent version of `Grappelli <http://code.google.com/p/django-grappelli/>`_ includes 
drag and drop inlines, so if you are already using Grappelli, installing 
django-inline-ordering does not make sense. If you didn't evaluate Grappelli yet,
I encourage you to do so!

Suggestions on how to improve django-inline-ordering are very welcome.

Installation
------------

1. Put 'inline-ordering' on your python path

2. Add 'inline-ordering' to INSTALLED_APPS tuple in settings file 

Usage
-----

For each model that you want to be reorderable with drag & drop, you need to 
setup an admin class and slightly modify model declaration. This way you can 
easily apply reordering to existing model classes. You'll also have to copy one
file to your MEDIA_ROOT and that's all :)

Let's start with a simple example: Gallery has many GalleryPhotos. User might 
want to reorder the photos in the gallery to fit his likings.

1. Setup your admin inline class to inherit after OrderableStackedInline
   
   ::
     
     from inline_ordering.admin import OrderableStackedInline
     
     class GalleryPhotoInline(OrderableStackedInline):
    
       model = GalleryPhoto 

2. Setup your model to inherit after Orderable
   
   ::
   
     from inline_ordering.models import Orderables
     
     class GalleryPhoto(Orderable):
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

   The simplest way is to copy ``media/inline_ordering.js`` to your ``MEDIA_ROOT``.

   If you however believe that would make a mess, take advantage of the 
   'INLINE_ORDERING_JS' setting and set it to a location which should be requested 
   when accessing orderable inlines:

   ``INLINE_ORDERING_JS = MEDIA_URL + '/js/third_party/inline_ordering.js'``
  
Known issues
------------

1. Reordering might not work if primary key is not named 'id'. This is a matter 
   of a proper jQuery selector.

2. Reordering won't work for new records until saved. This needs a onchange 
   handler for the record form. 

3. Possibly ordering will break when there are multiple stacked inlines on your admin page.

Kudos
-----
simon for http://djangosnippets.org/snippets/1053/