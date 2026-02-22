from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("8214341889:AAHd34_G1lDkoOBo3lemYQfdkvs8r3XdnNQ", None)
DURATION_LIMIT = int(getenv("90", "90"))

OWNER_ID = "7558720792"

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/b3d0e737737d67a5bf5a5.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/agajayofficialchannel")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/freeapisleakhere")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
