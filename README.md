 <div align="center"> 🦁 FinSafari | 金融探险家


  
# 🎯 智能股票信号追踪系统 | AI-Powered Stock Signal Tracker

### 🌟 **FinSafari** - Let AI be your investment guide!

[🇨🇳 中文版](#-中文版) | [🇺🇸 English](#-english-version)

</div>

---

## 🇨🇳 中文版

### 🎨 项目亮点
- 🤖 **AI智能分析** - 基于大语言模型的股票信号解析
- 📊 **实时数据监控** - 25只热门股票实时追踪
- ⚡ **闪电般响应** - Vite + React极速体验
- 🎭 **优雅UI设计** - shadcn/ui + Tailwind美学界面
- 🔐 **安全可靠** - Supabase身份认证与数据保护

### 🛠️ 技术栈构成

| 层级 | 技术 | 描述 |
|---|---|---|
| 🎮 前端框架 | React 18 + TypeScript | 类型安全，开发高效 |
| ⚡ 构建工具 | Vite | 极速冷启动，HMR |
| 🎨 UI组件 | shadcn/ui + Tailwind CSS | 原子化样式，优雅美观 |
| 🔐 认证 | Supabase Auth | 企业级身份认证 |
| 📊 数据 | Alpha Vantage API | 专业金融数据 |
| 🗄️ 数据库 | Supabase Postgres | 实时数据同步 |
| 🐍 AI后端 | Python FastAPI | 智能信号处理 |

### 🚀 快速开始

#### 📋 环境要求
```bash
Node.js ≥ 18.0.0
Python ≥ 3.8 (可选，用于AI功能)
```

#### 🎯 安装步骤

```bash
# 1️⃣ 克隆项目
git clone https://github.com/yourusername/FinSafari.git
cd FinSafari

# 2️⃣ 安装依赖
npm install

# 3️⃣ 环境配置
cp .env.example .env.local
# 编辑 .env.local 填入您的API密钥

# 4️⃣ 启动开发服务器
npm run dev

# 5️⃣ 构建生产版本
npm run build
```

#### 🔧 环境变量配置
```env
# Alpha Vantage API
VITE_ALPHA_VANTAGE_API_KEY=your_api_key_here

# Supabase
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_key
```

### 📁 项目结构
```
FinSafari/
├── 📱 src/                    # 前端源码
│   ├── 🧩 components/         # React组件
│   ├── 📄 pages/            # 页面组件
│   ├── 🔌 services/          # API服务
│   ├── 🪝 hooks/            # 自定义Hook
│   ├── 📊 data/             # 样本数据
│   └── ⚙️ lib/              # 工具函数
├── 🐍 js.tool/              # Python AI服务
│   ├── 🚀 app.py            # Flask应用
│   ├── 🤖 llm_service.py    # AI信号生成
│   └── 📈 stock_data_fetcher.py
├── 🏗️ public/              # 静态资源
├── 📦 package.json         # 项目配置
└── ⚙️ vite.config.ts       # Vite配置
```

### 🎮 核心功能
- **📊 实时信号面板** - 动态展示最新交易信号
- **🔍 智能搜索** - 股票代码/名称模糊搜索
- **⭐ 个人关注** - 自定义股票关注列表
- **📈 深度分析** - AI生成的市场洞察报告
- **🔔 即时通知** - 重要信号推送提醒

### 📊 可用脚本
```bash
npm run dev        # 启动开发服务器
npm run build      # 构建生产版本
npm run preview    # 预览构建结果
npm run lint       # 代码检查
```

### 🤝 贡献指南
欢迎提交Issue和Pull Request！让我们一起打造更好的FinSafari！

### 📄 许可证

---

## 🇺🇸 English Version

### 🎨 Project Highlights
- 🤖 **AI Intelligence** - LLM-based stock signal analysis
- 📊 **Real-time Monitoring** - 25 popular stocks live tracking
- ⚡ **Lightning Fast** - Vite + React blazing performance
- 🎭 **Elegant UI** - shadcn/ui + Tailwind beautiful interface
- 🔐 **Security First** - Supabase auth & data protection

### 🛠️ Tech Stack

| Layer | Technology | Description |
|---|---|---|
| 🎮 Frontend | React 18 + TypeScript | Type-safe, efficient development |
| ⚡ Build Tool | Vite | Lightning-fast cold start, HMR |
| 🎨 UI Framework | shadcn/ui + Tailwind CSS | Atomic styling, elegant design |
| 🔐 Auth | Supabase Auth | Enterprise-grade authentication |
| 📊 Data | Alpha Vantage API | Professional financial data |
| 🗄️ Database | Supabase Postgres | Real-time data sync |
| 🐍 AI Backend | Python FastAPI | Intelligent signal processing |

### 🚀 Quick Start

#### 📋 Requirements
```bash
Node.js ≥ 18.0.0
Python ≥ 3.8 (optional, for AI features)
```

#### 🎯 Installation

```bash
# 1️⃣ Clone repository
git clone https://github.com/yourusername/FinSafari.git
cd FinSafari

# 2️⃣ Install dependencies
npm install

# 3️⃣ Environment setup
cp .env.example .env.local
# Edit .env.local with your API keys

# 4️⃣ Start dev server
npm run dev

# 5️⃣ Build for production
npm run build
```

#### 🔧 Environment Variables
```env
# Alpha Vantage API
VITE_ALPHA_VANTAGE_API_KEY=your_api_key_here

# Supabase
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_key
```

### 📁 Project Structure
```
FinSafari/
├── 📱 src/                    # Frontend source
│   ├── 🧩 components/         # React components
│   ├── 📄 pages/            # Page components
│   ├── 🔌 services/          # API services
│   ├── 🪝 hooks/            # Custom hooks
│   ├── 📊 data/             # Sample data
│   └── ⚙️ lib/              # Utility functions
├── 🐍 js.tool/              # Python AI services
│   ├── 🚀 app.py            # Flask application
│   ├── 🤖 llm_service.py    # AI signal generation
│   └── 📈 stock_data_fetcher.py
├── 🏗️ public/              # Static assets
├── 📦 package.json         # Project config
└── ⚙️ vite.config.ts       # Vite config
```

### 🎮 Core Features
- **📊 Real-time Dashboard** - Dynamic trading signal display
- **🔍 Smart Search** - Stock code/name fuzzy search
- **⭐ Personal Watchlist** - Custom stock monitoring
- **📈 Deep Analytics** - AI-generated market insights
- **🔔 Instant Alerts** - Important signal notifications

### 📊 Available Scripts
```bash
npm run dev        # Start development server
npm run build      # Build for production
npm run preview    # Preview build result
npm run lint       # Code linting
```

### 🤝 Contributing
Issues and PRs are welcome! Let's build better FinSafari together!

### 📄 License
        
