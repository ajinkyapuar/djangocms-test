from djangocms_spa.cms_plugins import SPAPlugin

class TextPlugin(JsonOnlyPluginBase):
    name = _('Text')
    model = TextPluginModel
    frontend_component_name = 'cmp-text'
    
    def render_spa(self, request, context, instance):
        context = super(TextPlugin, self).render_spa(request, context, instance)
        context['content']['text'] = instance.text
        return context

plugin_pool.register_plugin(TextPlugin)