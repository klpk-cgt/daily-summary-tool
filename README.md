# 每日信息汇总工具

自动收集和汇总每日的黄金价格、虚拟货币价格、广东油价和今日头条新闻。

## 功能特性

- 📊 自动获取黄金价格
- ₿ 实时虚拟货币行情（BTC/ETH）
- ⛽ 广东地区油价信息
- 📰 今日头条热点新闻
- ⏰ 每日自动执行
- 📁 多种格式输出（文本/HTML）

## 快速开始

### 环境要求

- Python 3.8+
- GitHub账户

### 安装步骤

1. **Fork此仓库**
2. **设置API密钥**：
   - 进入仓库 Settings → Secrets → Actions
   - 添加以下Secrets：
     - `GOLD_API_TOKEN`: 黄金价格API密钥
     - `CRYPTO_API_TOKEN`: 虚拟货币API密钥
     - `NEWS_API_TOKEN`: 新闻API密钥
     - `OIL_API_TOKEN`: 油价API密钥

3. **手动触发运行**：
   - 进入 Actions 页面
   - 选择 "每日信息汇总"
   - 点击 "Run workflow"

### 项目结构
