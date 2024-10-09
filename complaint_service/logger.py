from loguru import logger
import sys

logger.remove()
logger.add("test_logs.log",enqueue=True, level = 'DEBUG', mode='w')