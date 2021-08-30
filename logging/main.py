import logging 

logger = logging.getLogger(__name__)

#create handler

stram_h = logging.StreamHandler()
file_h = logging.StreamHandler("file.log")

#level and the format

stram_h.setLevel(logging.WARNING)

