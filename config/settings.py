from pathlib import Path

# ===========================
# PROJECT ROOT
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# FOLDERS
# ===========================

INPUT_FOLDER = BASE_DIR / "input"
OUTPUT_FOLDER = BASE_DIR / "output"

ASSETS_FOLDER = BASE_DIR / "assets"

FONTS_FOLDER = ASSETS_FOLDER / "fonts"
TEMPLATE_FOLDER = ASSETS_FOLDER / "templates"
LOGO_FOLDER = ASSETS_FOLDER / "logo"

# ===========================
# DEFAULT IMAGE SETTINGS
# ===========================

BACKGROUND_COLOR = (255, 255, 255)

EXPORT_FORMAT = "PNG"

EXPORT_QUALITY = 100

# ===========================
# AI ENGINE SETTINGS
# ===========================

BACKGROUND_ENGINE = "rembg"

USE_ALPHA_MATTING = True

POST_PROCESS_MASK = True