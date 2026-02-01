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
- **Phidata Framework**: Multi-agent orchestration
- **Streamlit**: Interactive web interface
- **Groq LLM**: Fast inference using `llama-3.3-70b-versatile` model
- **YFinance**: Real-time financial data and stock information
- **DuckDuckGo**: Web search for latest news and articles
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
```

## 🚦 Usage

### Option 1: Run Streamlit App (Web Interface)

Start the interactive Streamlit web interface:
```bash
streamlit run streamlit_app.py
```

Access the web interface at: `http://localhost:8501`

### Option 2: Run CLI Agent

Execute the command-line agent:
```bash
python financial_agent.py
```

## 📁 Project Structure

```
Financial AI Agent/
├── financial_agent.py      # CLI multi-agent implementation
├── streamlit_app.py        # Streamlit web interface
├── playground.py            # Phidata playground (legacy)
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project metadata
├── .env                    # Environment variables (API keys)
├── .gitignore              # Git ignore patterns
└── README.md               # Project documentation
```

## 🧩 Components

### streamlit_app.py
Custom Streamlit web interface featuring:
- Interactive chat interface
- Agent selection (Multi-Agent, Finance, Web Search)
- Real-time responses
- Chat history management
- Example queries
- API status monitoring

### financial_agent.py
Multi-agent system with team collaboration for CLI usage. Demonstrates:
- Agent team coordination
- Streaming responses
- Combined financial and web search capabilities

## 🔑 API Keys Setup

### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Add to `.env` file as `GROQ_API_KEY`

## 📊 Example Queries

Try these queries in the Streamlit app:

**US Stocks:**
- "What is the stock price of NVDA?"
- "Summarize analyst recommendations for TSLA"
- "Get the latest news and fundamentals for AAPL"
- "Compare stock prices of MSFT and GOOGL"

**Indian Stocks (use .NS suffix):**
- "What is the stock price of TATAMOTORS.NS?"
- "Show fundamentals for TCS.NS"
- "Compare INFY.NS and WIPRO.NS"
- "Get analyst recommendations for RELIANCE.NS"

### Common Stock Tickers

**US Market** (no suffix needed):
- AAPL (Apple), MSFT (Microsoft), GOOGL (Google)
- TSLA (Tesla), NVDA (Nvidia), META (Meta)

**Indian Market** (add .NS for NSE):
- **TATA Group**: TATAMOTORS.NS, TCS.NS, TATASTEEL.NS, TATAPOWER.NS
- **IT**: INFY.NS (Infosys), WIPRO.NS, TECHM.NS
- **Banking**: HDFCBANK.NS, ICICIBANK.NS, SBIN.NS
- **Other**: RELIANCE.NS, ITC.NS, LT.NS
- `get_stock_fundamentals()`: Access company fundamentals (PE ratio, market cap, etc.)
- `get_company_news()`: Fetch latest company-specific news

### Web Search Agent
- `duckduckgo_search()`: Search web for financial news and articles
- `duckduckgo_news()`: Get latest news from multiple sources
- Always includes sources for verification

## ⚙️ Configuration

### Customize Agent Behavior

Edit `streamlit_app.py` or `financial_agent.py` to modify:
- Model selection: Change `id="llama-3.3-70b-versatile"` to other Groq models
- Instructions: Customize agent behavior and output format
- Tools: Add or remove tools based on requirements
- Agent names and roles: Personalize agent identities

### Supported Groq Models
- `llama-3.3-70b-versatile` (Current - versatile and powerful)
- `llama-3.1-8b-instant` (Fast and efficient)
- Check [Groq Docs](https://console.groq.com/docs/models) for latest models

## 🐛 Troubleshooting

### Common Issues

**Import Error: No module named 'phi'**
```bash
pip install phidata
```

**DuckDuckGo Rate Limit (202 Error)**
- Use the **Finance Agent** instead of Multi-Agent for stock queries
- The Finance Agent doesn't use web search and has no rate limits
- Wait a few minutes before using Web Search Agent again

**Invalid Stock Ticker (404 Error)**
- Indian stocks need `.NS` suffix (e.g., TATAMOTORS.NS, TCS.NS)
- US stocks don't need any suffix (e.g., AAPL, MSFT)
- Check ticker spelling on Yahoo Finance website

**API Key Error**
- Ensure `.env` file exists with valid API keys
- Verify `python-dotenv` is installed
- Check API keys are not expired

**Model Decommissioned Error**
- Update model ID in code to a supported model
- Current recommended: `openai/gpt-4o-mini`
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