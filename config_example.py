WAVES_API_URL = "http://10.137.0.24:6869"
WAVES_API_KEY = "qwertyiopavz32awrg23423"
WAVES_NETWORK_TYPE = 'L' # W for mainnet, T for testnet, L for devnet

SUPPORTED_ASSETS = ['']

LOG_DIR = "logs"

PORT = 64912

DEBUG = True

import logging
from logging.handlers import RotatingFileHandler
import os.path
logFormatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = RotatingFileHandler(os.path.join(LOG_DIR, "gw-instant-seller.log"), maxBytes=200000, backupCount=5000) # Max log size is 1GB
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

rootLogger.setLevel(logging.DEBUG)
