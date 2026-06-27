from pathlib import Path

from PIL import Image

from rembg import remove

from config.settings import (
    BACKGROUND_ENGINE,
)


class BackgroundRemover:

    def __init__(self):

        self.engine = BACKGROUND_ENGINE

    def remove_background(self, image):

        if self.engine == "rembg":

            return self._remove_with_rembg(image)

        raise ValueError(
            f"Unknown Engine : {self.engine}"
        )

    def _remove_with_rembg(self, image):

        output = remove(image)

        return output