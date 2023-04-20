from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "1881742"))
    API_HASH = getenv("API_HASH", "9302cd0cff1e2aa81379d95aeba7f27b")
    BOT_TOKEN = getenv("BOT_TOKEN", "6078472433:AAE9iX1kyC9NNCJOBDivaPsi9QiNXEa_Sp8")
    FSUB = getenv("FSUB", "Hackinsider")
    CHID = int(getenv("CHID", "1928008250"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://mailzedhacks:h5of0PptllVICBpe@cluster0.ex0xjgy.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
