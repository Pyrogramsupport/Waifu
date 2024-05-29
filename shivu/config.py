class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6679467894"
    sudo_users = "6679467894 1060707656"
    GROUP_ID = -1002159833810
    TOKEN = "7182024060:AAEV0GAAQUlw_E-UnNTOxd7K3A6dOpR6muM"
    mongo_url = "mongodb+srv://Siva:siva@secure.ffezokv.mongodb.net/?retryWrites=true&w=majority&appName=Secure"
    PHOTO_URL = ["https://graph.org/file/cb65e2e8ea675f4b494af.jpg", "https://graph.org/file/1e64d77e0bec543c39f45.jpg"]
    SUPPORT_CHAT = "secure_chattt"
    UPDATE_CHAT = "secure_updates"
    BOT_USERNAME = "secure_x_robot"
    CHARA_CHANNEL_ID = "-1002212512545"
    api_id = 19042248
    api_hash = "a1d443cb79941a89c493f22abf4f84cb"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
