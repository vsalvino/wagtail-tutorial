from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    pass

    ### STEP 2 ####
    #body = RichTextField(blank=True)
    #
    #content_panels = Page.content_panels + [
    #    FieldPanel('body'),
    #]
    #
    #template = 'home/my_homepage.html'
    ### END STEP 2 ###


    ### STEP 4 ###
    #def get_context(self, request):
    #    # Run the superclass context
    #    context = super().get_context(request)
    #    # Get published blog pages ordered newest to oldest
    #    blogpages = BlogPage.objects.live().order_by('-date')
    #    # Update template context
    #    context['blogpages'] = blogpages
    #    return context
    ### END STEP 4 ###



### STEP 3 ###
#class BlogPage(Page):
#    date = models.DateField("Post date")
#    intro = models.CharField(max_length=250)
#    image = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, related_name='+')
#    body = RichTextField(blank=True)
#
#    content_panels = Page.content_panels + [
#        FieldPanel('date'),
#        FieldPanel('intro'),
#        ImageChooserPanel('image'),
#        FieldPanel('body'),
#    ]
#
#    template = 'home/my_blogpage.html'
### END STEP 3 ###
