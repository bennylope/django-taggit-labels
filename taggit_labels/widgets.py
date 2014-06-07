from django.forms.util import flatatt
from django.utils.safestring import mark_safe

from taggit.forms import TagWidget


class LabelWidget(TagWidget):
    """
    """
    input_type = 'hidden'
    model = None

    def __init__(self, *args, **kwargs):
        model = kwargs.pop('model', None)
        if model is None:
            from taggit.models import Tag
            self.model = Tag
        else:
            self.model = model
        super(LabelWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        tags = [o.tag for o in value.select_related("tag")]
        return_val = super(TagWidget, self).render(name, value, attrs)

        if attrs.get('class', None) is None:
            attrs.update({'class': 'tags'})
        list_attrs = flatatt(attrs)
        all_tags = self.model.objects.all()

        selected_tags = []
        for tag in all_tags:
            if tag in tags:
                selected_tags.append((tag.name, 'selected'))
            else:
                selected_tags.append((tag.name, ''))

        tag_li = "".join(["<li data-tag-name='{0}' class={1}>{0}</li>".format(
            tag[0], tag[1]) for tag in selected_tags])
        tag_ul = "<ul{0}>{1}</ul>".format(list_attrs, tag_li)
        return mark_safe(u"{0}{1}".format(tag_ul, return_val))

    class Media:
        css = {
            'all': ('css/taggit_labels.css',)
        }
        js = ('js/taggit_labels.js',)
