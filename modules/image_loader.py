from PIL import Image
from pathlib import Path


class ImageLoader:

    def __init__(self, image_path):

        self.image_path = Path(image_path)

    def load(self):

        if not self.image_path.exists():

            raise FileNotFoundError(
                f"Image not found : {self.image_path}"
            )

        image = Image.open(self.image_path)

        return image

    def get_info(self):

        image = self.load()

        return {

            "width": image.width,

            "height": image.height,

            "mode": image.mode,

            "format": image.format

        }