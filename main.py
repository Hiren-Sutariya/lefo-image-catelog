from config.settings import INPUT_FOLDER, OUTPUT_FOLDER

from modules.image_loader import ImageLoader
from modules.canvas import Canvas


def main():

    image_path = INPUT_FOLDER / "test.jpg"


    loader = ImageLoader(image_path)

    image = loader.load()

    info = loader.get_info()

    print("=" * 40)
    print("IMAGE INFORMATION")
    print("=" * 40)

    print(f"Width  : {info['width']} px")
    print(f"Height : {info['height']} px")
    print(f"Format : {info['format']}")
    print(f"Mode   : {info['mode']}")

    print("=" * 40)

    canvas_engine = Canvas(
        width=800,
        height=800
    )

    canvas = canvas_engine.create()

    final_image = canvas_engine.center_image(
        canvas,
        image
    )

    output_path = OUTPUT_FOLDER / "centered.png"

    final_image.save(output_path)

    print("✅ Image Centered Successfully")


if __name__ == "__main__":
    main()