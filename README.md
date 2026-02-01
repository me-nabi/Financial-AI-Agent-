# Financial AI Agent 

A powerful multi-agent financial intelligence system built with **Phidata** and **Groq**, designed to provide real-time stock analysis, market insights, and financial news through an interactive web interface.

## 🚀 Features

### 🤖 Multi-Agent Architecture
- **Finance AI Agent**: Specialized in analyzing stock data, providing analyst recommendations, fundamentals, and company news
- **Web Search Agent**: Searches the web for latest financial information and news articles
- **Team Collaboration**: Agents work together to provide comprehensive financial insights

### 📊 Capabilities
- Real-time stock price tracking
- Analyst recommendations analysis
- Company fundamentals and financial metrics
- Latest news aggregation with sources
- Interactive chat interface via Phidata Playground
- Streaming responses for real-time feedback

### 🛠️ Technologies
- **Phidata Framework**: Multi-agent orchestration and playground
- **Groq LLM**: Fast inference using `llama-3.1-8b-instant` model
- **YFinance**: Real-time financial data and stock information
- **DuckDuckGo**: Web search for latest news and articles
- **FastAPI + Uvicorn**: Backend API server
- **Python 3.12**: Modern Python with async support

## 📸 Screenshots

### Analyst Recommendations & News Analysis
![Tesla Analysis](https://raw.githubusercontent.com/yourusername/yourrepo/main/screenshots/tesla-analysis.png)
*Multi-agent analysis showing TSLA analyst recommendations and latest news with data tables*

### Real-Time Stock Price Queries
![Stock Price Query](https://raw.githubusercontent.com/yourusername/yourrepo/main/screenshots/stock-price.png)
*Interactive chat interface querying real-time stock prices for TSLA and TATA*

## 🔧 Installation

### Prerequisites
- Python 3.12 or higher
- Groq API Key ([Get it here](https://console.groq.com/))
- Phidata API Key ([Get it here](https://phidata.app/))

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd FinancialAPP_Agentic_Rag
```

2. **Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
PHI_API_KEY=your_phi_api_key_here
```

## 🚦 Usage

### Option 1: Run Playground (Web Interface)

Start the interactive Phidata Playground:
```bash
python playground.py
```

Access the web interface at: `http://localhost:7777`

### Option 2: Run CLI Agent

Execute the command-line agent:
```bash
python financial_agent.py
```

## 📁 Project Structure

```
FinancialAPP_Agentic_Rag/
├── financial_agent.py      # CLI multi-agent implementation
├── playground.py            # Web-based playground interface
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project metadata
├── .env                    # Environment variables (API keys)
├── .gitignore              # Git ignore patterns
└── README.md               # Project documentation
```

## 🧩 Components

### financial_agent.py
Multi-agent system with team collaboration for CLI usage. Demonstrates:
- Agent team coordination
- Streaming responses
- Combined financial and web search capabilities

### playground.py
Web-based interactive interface featuring:
- Phidata Playground integration
- Real-time chat interface
- Agent selection and configuration
- Session management and history

## 🔑 API Keys Setup

### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Add to `.env` file as `GROQ_API_KEY`

### Phidata API Key
1. Visit [Phidata App](https://phidata.app/)
2. Sign up or log in
3. Generate an API key from settings
4. Add to `.env` file as `PHI_API_KEY`

## 📊 Example Queries

Try these queries in the playground:

- "What is the current stock price of NVDA?"
- "Summarize analyst recommendations for TSLA"
- "Get the latest news and fundamentals for AAPL"
- "Compare stock prices of MSFT and GOOGL"
- "What are the top analyst recommendations for tech stocks?"

## 🎯 Agent Capabilities

### Finance AI Agent
- `get_stock_price()`: Retrieve current stock prices
- `get_analyst_recommendations()`: Get analyst ratings and recommendations
- `get_stock_fundamentals()`: Access company fundamentals (PE ratio, market cap, etc.)
- `get_company_news()`: Fetch latest company-specific news

### Web Search Agent
- `duckduckgo_search()`: Search web for financial news and articles
- `duckduckgo_news()`: Get latest news from multiple sources
- Always includes sources for verification

## ⚙️ Configuration

### Customize Agent Behavior

Edit `playground.py` or `financial_agent.py` to modify:
- Model selection: Change `id="llama-3.1-8b-instant"` to other Groq models
- Instructions: Customize agent behavior and output format
- Tools: Add or remove tools based on requirements
- Agent names and roles: Personalize agent identities

### Supported Groq Models
- `llama-3.1-8b-instant` (Current - fast and efficient)
- `llama-3.3-70b-versatile`
- Check [Groq Docs](https://console.groq.com/docs/models) for latest models

## 🐛 Troubleshooting

### Common Issues

**Import Error: No module named 'phi'**
```bash
pip install phidata
```

**API Key Error**
- Ensure `.env` file exists with valid API keys
- Verify `python-dotenv` is installed
- Check API keys are not expired

**Model Decommissioned Error**
- Update model ID in code to a supported model
- Check Groq documentation for current models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Phidata](https://phidata.app/) - Multi-agent framework
- [Groq](https://groq.com/) - Fast LLM inference
- [YFinance](https://github.com/ranaroussi/yfinance) - Financial data
- [DuckDuckGo](https://duckduckgo.com/) - Web search capabilities

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

**Note**: This is a demo application. Always verify financial information from official sources before making investment decisions.