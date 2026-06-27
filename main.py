from config.settings import INPUT_FOLDER, OUTPUT_FOLDER

from modules.image_loader import ImageLoader
from modules.background import BackgroundRemover
from modules.canvas import Canvas


def main():

    print("=" * 50)
    print("🚀 ImageFlow AI Started")
    print("=" * 50)

    # --------------------------
    # Load Image
    # --------------------------

    image_path = INPUT_FOLDER / "test.jpg"

    loader = ImageLoader(image_path)

    image = loader.load()

    info = loader.get_info()

    print("\n📷 Image Information")

    print(f"Width  : {info['width']} px")
    print(f"Height : {info['height']} px")
    print(f"Format : {info['format']}")
    print(f"Mode   : {info['mode']}")

    # --------------------------
    # Remove Background
    # --------------------------

    print("\n🎯 Removing Background...")

    bg = BackgroundRemover()

    transparent_image = bg.remove_background(image)

    transparent_output = OUTPUT_FOLDER / "transparent.png"

    transparent_image.save(transparent_output)

    print("✅ Background Removed")

    # --------------------------
    # Create Canvas
    # --------------------------

    print("\n🖼️ Creating Canvas...")

    canvas_engine = Canvas(
        width=800,
        height=800
    )

    canvas = canvas_engine.create()

    # --------------------------
    # Center Image
    # --------------------------

    final_image = canvas_engine.center_image(
        canvas,
        transparent_image
    )

    final_output = OUTPUT_FOLDER / "final.png"

    final_image.save(final_output)

    print("✅ Final Image Saved")

    print("\n📂 Output Files")

    print("transparent.png")

    print("final.png")

    print("\n🎉 Done")


if __name__ == "__main__":
    main()