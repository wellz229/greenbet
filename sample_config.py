#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("6006790382:AAFfUhxNwbwJXEecpoOJMbh3mKlEn5cOUuU", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("24378907", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("f94b60656cb010fdbb1f4cdf83eb8f69", "")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("AQFz_hsAvYiz6dYNtuu6VzM1-F6LPzZCBKU_iRFm0IlykkdO6eRox85HsZgXIcEFSKZ_FBwetdEDD9uhDrztJ0aWbGnGQRVS4QGk3zisuA4Gn5eEcqrbInS3asRkFeCbXucHS_ODxfvB20w2p0E1KXQjeDUTU2s8DMlSvzQrNkDITLMvCNkdQEQfCiJ7m0LZjO_JUfkX2twYiVsTn6jmET5NZTq5Acimmf2dDPXFl3l2eAcLEKh-R3mUk7iEt2ilAVnkbIis6B8zvmI3m3fxMLTDgqrnhoAqoxC5RAzgpwwyaUIasxLKPlkZKwEJqhN_JzEuBKbzTy1HkYypemVTWNFNoI18zgAAAABu1nR1AA", "")

    # Database URI
    DB_URI = os.environ.get("postgresql://botgreenvip:changeme@localhost:5432/botgreenvip", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
