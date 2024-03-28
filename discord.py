import time
import board
from adafruit_pyportal import PyPortal
from adafruit_portalbase.network import CONTENT_TEXT

# Set up where we'll be fetching data from
DATA_SOURCE = "https://img.shields.io/discord/512935636638892032.svg"
# a regular expression for finding the data within the SVG xml text!
DATA_LOCATION = [r">([0-9]+ online)<"]

cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE, regexp_path=DATA_LOCATION,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/Discord.bmp",
                    text_font=cwd+"/fonts/Collegiate-50.bdf",
                    text_position=(70, 210), text_color=0x000000)

while True:
    try:
        value = pyportal.fetch(force_content_type=CONTENT_TEXT)
        print("Response is", value)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(60)
