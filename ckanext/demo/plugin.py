import ckan.plugins as p


class DemoPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
