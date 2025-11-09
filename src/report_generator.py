import os
from datetime import datetime
from config.config import Config

class ReportGenerator:
    """报告生成类"""
    
    def __init__(self):
        self.config = Config()
        # 确保输出目录存在
        os.makedirs(self.config.OUTPUT_DIR, exist_ok=True)
    
    def generate_daily_report(self, gold_price, crypto_prices, oil_price, news):
        """生成每日汇总报告"""
        
        # 报告内容模板
        report_content = f"""每日信息汇总
日期：{self.config.get_date()}

黄金价格：{gold_price}

虚拟货币价格：
比特币(BTC): {crypto_prices.get('BTC', '暂无数据')}
以太坊(ETH): {crypto_prices.get('ETH', '暂无数据')}

广东油价：{oil_price}

今日头条新闻：
{chr(10).join(news)}

生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        # 保存文件
        filename = f"daily_summary_{datetime.now().strftime('%Y%m%d')}.txt"
        filepath = os.path.join(self.config.OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"报告已生成: {filepath}")
        return filepath, report_content
    
    def generate_html_report(self, gold_price, crypto_prices, oil_price, news):
        """生成HTML格式报告（可选）"""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>每日信息汇总 - {self.config.get_date()}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ color: #333; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
        .section {{ margin: 20px 0; }}
        .news-item {{ margin: 5px 0; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>每日信息汇总</h1>
        <h2>日期：{self.config.get_date()}</h2>
    </div>
    
    <div class="section">
        <h3>💰 黄金价格</h3>
        <p>{gold_price}</p>
    </div>
    
    <div class="section">
        <h3>₿ 虚拟货币价格</h3>
        <p>比特币(BTC): {crypto_prices.get('BTC', '暂无数据')}</p>
        <p>以太坊(ETH): {crypto_prices.get('ETH', '暂无数据')}</p>
    </div>
    
    <div class="section">
        <h3>⛽ 广东油价</h3>
        <p>{oil_price}</p>
    </div>
    
    <div class="section">
        <h3>📰 今日头条新闻</h3>
        {"".join([f'<p class="news-item">{news_item}</p>' for news_item in news])}
    </div>
    
    <div class="footer">
        <p><small>生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small></p>
    </div>
</body>
</html>
"""
        
        filename = f"daily_summary_{datetime.now().strftime('%Y%m%d')}.html"
        filepath = os.path.join(self.config.OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
