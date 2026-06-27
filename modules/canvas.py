from PIL import Image


class Canvas:

    def __init__(
        self,
        width=800,
        height=800,
        color=(255, 255, 255),
    ):

        self.width = width
        self.height = height
        self.color = color

    def create(self):

        return Image.new(
            "RGB",
            (self.width, self.height),
            self.color
        )

    def center_image(self, canvas, image):

        # Canvas size
        canvas_width = canvas.width
        canvas_height = canvas.height

        # Product size
        image_width = image.width
        image_height = image.height

        # Center Position
        x = (canvas_width - image_width) // 2
        y = (canvas_height - image_height) // 2

        # Paste Image
        canvas.paste(image, (x, y))

        return canvas