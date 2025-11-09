import json
from datetime import datetime

class DataProcessor:
    """数据处理类"""
    
    @staticmethod
    def process_gold_data(raw_data):
        """处理黄金价格数据"""
        if not raw_data:
            return "暂无数据"
        
        try:
            # 根据实际API响应结构调整
            # 示例: {"price": 520.5, "unit": "元/克"}
            if 'price' in raw_data:
                return f"{raw_data['price']} {raw_data.get('unit', '元/克')}"
            else:
                return "数据格式异常"
        except Exception as e:
            return f"数据处理错误: {e}"
    
    @staticmethod
    def process_crypto_data(raw_data):
        """处理虚拟货币数据"""
        if not raw_data:
            return {"BTC": "暂无数据", "ETH": "暂无数据"}
        
        try:
            result = {}
            # 根据实际API响应结构调整
            if isinstance(raw_data, dict) and 'data' in raw_data:
                for coin in raw_data['data']:
                    if coin['symbol'] == 'BTC':
                        result['BTC'] = f"${coin.get('price', 'N/A')}"
                    elif coin['symbol'] == 'ETH':
                        result['ETH'] = f"${coin.get('price', 'N/A')}"
            return result
        except Exception as e:
            return {"BTC": f"错误: {e}", "ETH": f"错误: {e}"}
    
    @staticmethod
    def process_news_data(raw_data):
        """处理新闻数据"""
        if not raw_data:
            return ["暂无新闻数据"]
        
        try:
            news_list = []
            # 根据实际API响应结构调整
            if isinstance(raw_data, dict) and 'data' in raw_data:
                for i, news in enumerate(raw_data['data'][:3]):  # 取前3条
                    title = news.get('title', '无标题')
                    news_list.append(f"{i+1}. {title}")
            return news_list if news_list else ["暂无新闻数据"]
        except Exception as e:
            return [f"新闻数据处理错误: {e}"]
    
    @staticmethod
    def process_oil_data(raw_data):
        """处理油价数据"""
        if not raw_data:
            return "暂无油价数据"
        
        try:
            # 根据实际API响应结构调整
            if isinstance(raw_data, dict) and 'data' in raw_data:
                oil_data = raw_data['data']
                return f"92号汽油: {oil_data.get('92', 'N/A')}元/升"
            return "油价数据格式异常"
        except Exception as e:
            return f"油价数据处理错误: {e}"
