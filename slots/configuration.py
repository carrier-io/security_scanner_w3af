from pylon.core.tools import web


class Slot:
    integration_name = 'security_scanner_w3af'
    section_name = 'scanners'

    @web.slot(f'integrations_{section_name}_content')
    def integration_create_modal_content(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'integration/content.html',
                section_name=Slot.section_name
            )

    @web.slot(f'integrations_{section_name}_scripts')
    def integration_create_modal_scripts(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'integration/scripts.html',
            )