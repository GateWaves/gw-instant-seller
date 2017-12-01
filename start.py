#!/usr/bin/env python3
import logging
import config

if __name__ == "__main__":
    if config.DEBUG:
        logging.error("YOU ARE RUNNING IN A DEBUG MODE! Don't use this in production.")
        if config.WAVES_NETWORK_TYPE == 'W':
            logging.error("Cowardly refusing to start a mainnet version in a debug mode.")
            exit(0)
    from src.api import start
    start()
