"""
设置模块
"""
from .config import Config, Target

configInside = Config()
config = Target(configInside.menu())
