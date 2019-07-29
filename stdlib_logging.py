import os
import platform
import logging

if platform.platform().startswith("Windows"):
    # 这是在 Windows 平台下
    logging_file = os.path.join(
        os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "test.log"
    )
else:
    # 这是其他平台下
    logging_file = os.path.join(os.getenv("HOME"), "test.log")

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    filename=logging_file,
    filemode="w",
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
