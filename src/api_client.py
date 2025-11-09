import requests
import json
from config.config import Config

class APIClient:
    """API客户端类"""
    
    def __init__(self):
        self.config = Config()
    
    def make_request(self, api_type, params=None):
        """通用API请求方法"""
        if api_type not in self.config.API_CONFIG:
            raise ValueError(f"不支持的API类型: {api_type}")
        
        api_config = self.config.API_CONFIG[api_type]
        headers = {
            'Authorization': f'Bearer {api_config["token"]}',
            'Content-Type': 'application/json'
        }
        
        try:
            if params:
                response = requests.post(api_config['url'], json=params, headers=headers, timeout=10)
            else:
                response = requests.get(api_config['url'], headers=headers, timeout=10)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"API请求失败 ({api_type}): {e}")
            return None
    
    def get_gold_price(self):
        """获取黄金价格"""
        # 根据实际API文档调整参数
        params = {
            "date": self.config.get_date()
        }
        return self.make_request("gold", params)
    
    def get_crypto_price(self):
        """获取虚拟货币价格"""
        # 根据实际API文档调整参数
        params = {
            "symbols": ["BTC", "ETH"]
        }
        return self.make_request("crypto", params)
    
    def get_news(self):
        """获取今日头条新闻"""
        # 根据实际API文档调整参数
        params = {
            "count": 10,  # 获取10条，取前3条
            "type": "headline"
        }
        return self.make_request("news", params)
    
    def get_oil_price(self):
        """获取广东油价"""
        params = {
            "province": "广东"
        }
        return self.make_request("oil", params)
