import omni.ext
import carb

from .menu import RosBridgeMenu


class Extension(omni.ext.IExt):
    def on_startup(self, ext_id):
        self._menu = None
        self._menu = RosBridgeMenu()

    def on_shutdown(self):
        if self._menu is not None:
            self._menu.shutdown()
            self._menu = None
