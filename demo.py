from US_Visa.logger import logging
from US_Visa.exception import USvisaException
import sys




logging.info("Exception file testing")

try:
    2/0
except Exception as e:
    raise USvisaException(e,sys)