import os
from datetime import datetime, timedelta
import requests

class Config:
    """配置文件类"""
    
    # API配置
    API_CONFIG = {
        "gold": {
            "url": "https://api.example.com/gold",  # 替换为实际黄金API地址
            "token": os.getenv('GOLD_API_TOKEN', '')
        },
        "crypto": {
            "url": "https://api.example.com/crypto",  # 替换为实际虚拟货币API地址
            "token": os.getenv('CRYPTO_API_TOKEN', '')
        },
        "news": {
            "url": "https://api.example.com/news",  # 替换为实际新闻API地址
            "token": os.getenv('NEWS_API_TOKEN', '')
        },
        "oil": {
            "url": "https://v3.alapi.cn/api/oil",
            "token": os.getenv('OIL_API_TOKEN', '')
        }
    }
    
    # 文件路径配置
    OUTPUT_DIR = "output"
    
    @staticmethod
    def get_date():
        """获取当前日期"""
        return datetime.now().strftime("%Y年%m月%d日")
    
    @staticmethod
    def get_yesterday():
        """获取昨天日期"""
        return (datetime.now() - timedelta(days=1)).strftime("%Y年%m月%d日")
