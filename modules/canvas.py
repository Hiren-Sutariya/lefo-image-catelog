from PIL import Image


class Canvas:

    def __init__(
        self,
        width=800,
        height=800,
        color=(255, 255, 255, 255)
    ):

        self.width = width
        self.height = height
        self.color = color

    def create(self):
        """
        Create a new white RGBA canvas.
        """

        return Image.new(
            "RGBA",
            (self.width, self.height),
            self.color
        )

    def center_image(self, canvas, image):
        """
        Center any image on the canvas.
        """

        # Convert to RGBA if needed
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        canvas_width = canvas.width
        canvas_height = canvas.height

        image_width = image.width
        image_height = image.height

        x = (canvas_width - image_width) // 2
        y = (canvas_height - image_height) // 2

        # Preserve transparency
        canvas.paste(image, (x, y), image)

        return canvas