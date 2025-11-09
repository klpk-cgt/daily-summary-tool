#!/usr/bin/env python3
"""
每日信息汇总工具 - 主程序
"""

import os
import sys
from dotenv import load_dotenv

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import Config
from src.api_client import APIClient
from src.data_processor import DataProcessor
from src.report_generator import ReportGenerator

def main():
    """主函数"""
    print("🚀 开始生成每日信息汇总...")
    
    # 加载环境变量
    load_dotenv()
    
    # 初始化组件
    config = Config()
    api_client = APIClient()
    data_processor = DataProcessor()
    report_generator = ReportGenerator()
    
    # 检查API密钥
    required_tokens = ['GOLD_API_TOKEN', 'CRYPTO_API_TOKEN', 'NEWS_API_TOKEN', 'OIL_API_TOKEN']
    missing_tokens = [token for token in required_tokens if not os.getenv(token)]
    
    if missing_tokens:
        print(f"⚠️ 警告: 以下API密钥未设置: {', '.join(missing_tokens)}")
        print("请在GitHub仓库的Secrets中设置这些密钥")
    
    # 收集数据
    print("📊 正在获取黄金价格...")
    gold_data = api_client.get_gold_price()
    gold_price = data_processor.process_gold_data(gold_data)
    
    print("₿ 正在获取虚拟货币价格...")
    crypto_data = api_client.get_crypto_price()
    crypto_prices = data_processor.process_crypto_data(crypto_data)
    
    print("⛽ 正在获取广东油价...")
    oil_data = api_client.get_oil_price()
    oil_price = data_processor.process_oil_data(oil_data)
    
    print("📰 正在获取今日头条新闻...")
    news_data = api_client.get_news()
    news = data_processor.process_news_data(news_data)
    
    # 生成报告
    print("📄 正在生成汇总报告...")
    filepath, report_content = report_generator.generate_daily_report(
        gold_price, crypto_prices, oil_price, news
    )
    
    # 可选：生成HTML报告
    html_filepath = report_generator.generate_html_report(
        gold_price, crypto_prices, oil_price, news
    )
    
    # 输出结果
    print("\n" + "="*50)
    print("✅ 每日信息汇总完成！")
    print("="*50)
    print(report_content)
    print(f"📁 文件保存位置:")
    print(f"   - 文本格式: {filepath}")
    print(f"   - HTML格式: {html_filepath}")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 程序执行出错: {e}")
        sys.exit(1)
