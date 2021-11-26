import logging

"""
Critical
Error
Warning
Info
Debug
"""
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p',  filename="demo.log",level=logging.DEBUG)
logging.critical("THis is critical")
logging.error("THis is critical")
logging.info("THis is critical")
logging.warning("THis is critical")
logging.debug("THis is critical")




