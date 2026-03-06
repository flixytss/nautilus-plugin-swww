from gi.repository import Nautilus, GObject
import subprocess
import os

class ImageCommandExtension(GObject.GObject, Nautilus.MenuProvider):

    def run_command(self, menu, file):
        path = file.get_location().get_path()

        os.system(f"swww-setter {path}") # Needs swww-setter

    def get_file_items(self, files):
        if len(files) != 1:
            return

        file = files[0]

        mime_type = file.get_mime_type()

        if mime_type and mime_type.startswith("image/"):
            item = Nautilus.MenuItem(
                name="ImageCommandExtension::RunImage",
                label="Set SWWW Wallpaper",
                tip="Put this image as the swww background"
            )

            item.connect("activate", self.run_command, file)

            return [item]
