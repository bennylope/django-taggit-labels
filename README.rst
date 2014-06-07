====================
django-taggit-labels
====================

.. image:: https://badge.fury.io/py/django-taggit-labels.png
    :target: https://badge.fury.io/py/django-taggit-labels

.. image:: https://travis-ci.org/bennylope/django-taggit-labels.png?branch=master
    :target: https://travis-ci.org/bennylope/django-taggit-labels

Label widget(s) for `django-taggit <https://github.com/alex/django-taggit>`_.

Now instead of this:

.. image:: https://raw.githubusercontent.com/bennylope/django-taggit-labels/master/docs/taggit-text.png

You can use this:

.. image:: https://raw.githubusercontent.com/bennylope/django-taggit-labels/master/docs/taggit-labels.png

Overview
--------

This is a widget for use in the Django admin interface, and it depends on
Django's namespaced jQuery. It allows you to add and remove tags by selecting
or deselecting visual labels.

The label widget does not expose the input field so that you can add new tags. The
base label widget instead shows all available tags and lets you pick between
them in Django's admin interface. It presumes that you are using a managed (or
'curated' if you're feeling insufferable) tag list.

Quickstart
----------

Install django-taggit-labels::

    pip install django-taggit-labels

Add `taggit_labels` to your project::

    INSTALLED_APPS = (
        'taggit',
        'taggit_labels',
    )

Use the label widget::

    from taggit_labels.widgets import LabelWidget

    class ContentForm(forms.ModelForm):
        tags = TagField(required=False, LabelWidget)

You can use the widget with `your own tag model
<http://django-taggit.readthedocs.org/en/latest/custom_tagging.html>`_, too::

    from taggit_labels.widgets import LabelWidget

    class ContentForm(forms.Form):
        tags = TagField(required=False, LabelWidget(model=MyTag))

The `tag` model from taggit will be presumed if you do not specify a tag model.
