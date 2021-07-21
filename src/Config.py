import os

class Config:
    aid = int(os.environ.get("API_ID", None))
    ahash = os.environ.get("API_HASH", None)
    bot_token = os.environ.get("BOT_TOKEN", None)
    sudo = [1482778942, 1608141072]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
