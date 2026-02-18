"""InvenTree Work Instructions plugin."""

from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, UserInterfaceMixin

from . import PLUGIN_VERSION


class WorkInstrPlugin(SettingsMixin, UserInterfaceMixin, InvenTreePlugin):
    """Plugin that shows a Work Instructions panel on Part detail pages."""

    AUTHOR = "Mathew Rupp"
    DESCRIPTION = "Show a Work Instructions link panel on Part detail pages"
    VERSION = PLUGIN_VERSION
    MIN_VERSION = "0.12.0"
    NAME = "inventree-workinstr"
    SLUG = "workinstr"
    TITLE = "Work Instructions"

    SETTINGS = {
        "BASE_URL": {
            "name": "Work Instructions Base URL",
            "description": "Hostname + port of the MkDocs server",
            "default": "http://mat-eng:8088",
        },
        "PARAMETER_NAME": {
            "name": "Part Parameter Name",
            "description": "Name of the InvenTree Part Parameter holding the slug",
            "default": "Work Instruction",
        },
    }

    def get_ui_panels(self, request, context=None, **kwargs):
        """Return UI panels for work instructions."""
        if context is None:
            return []

        if context.get("target_model") != "part":
            return []

        target_id = context.get("target_id")
        if not target_id:
            return []

        from part.models import PartParameter

        param = PartParameter.objects.filter(
            part_id=target_id,
            template__name=self.get_setting("PARAMETER_NAME"),
        ).first()

        if not param:
            return []

        slug = str(param.data).strip()
        if not slug:
            return []

        base_url = self.get_setting("BASE_URL").rstrip("/")
        full_url = f"{base_url}/{slug.strip('/')}/"

        return [
            {
                "key": "work-instructions",
                "title": "Work Instructions",
                "icon": "ti:file-text:outline",
                "source": self.plugin_static_file(
                    "WorkInstrPanel.js:renderWorkInstrPanel"
                ),
                "context": {
                    "url": full_url,
                    "slug": slug,
                },
            }
        ]
