from django.db import models

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class MyCustomTag(TagBase):
    description = models.CharField(max_length=100, blank=True, null=True)


class TaggedWhatever(GenericTaggedItemBase):
    tag = models.ForeignKey(MyCustomTag)


class Content(models.Model):
    title = models.CharField(max_length=20)
    tags = TaggableManager()


class MyContent(models.Model):
    title = models.CharField(max_length=20)
    tags = TaggableManager(through=TaggedWhatever)
