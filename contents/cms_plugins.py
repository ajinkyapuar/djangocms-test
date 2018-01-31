from cms.plugin_pool import plugin_pool
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from djangocms_spa.cms_plugins import SPAPluginBase
from djangocms_text_ckeditor.cms_plugins import TextPlugin as TextPluginOriginal


class TextPlugin(TextPluginOriginal, SPAPluginBase):
    name = _('Text')
    frontend_component_name = 'cmp-text'
    
    def render_spa(self, request, context, instance):
        context = super(TextPlugin, self).render_spa(request, context, instance)
        context['content']['text'] = mark_safe(instance.body)
        return context


plugin_pool.unregister_plugin(TextPluginOriginal)
plugin_pool.register_plugin(TextPlugin)
