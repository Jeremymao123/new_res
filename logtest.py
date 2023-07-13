"""
Author:朱海辉
Time: 2022/11/15 16:59
Project: python_unittestProject
"""
import logging

from loguru import logger

logger.add(sink="log1.log",
           encoding="utf-8",
           level = "INFO",
           rotation="100 MB")
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")