import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Financial AI Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize agents
@st.cache_resource
def initialize_agents():
    """Initialize the AI agents"""
    
    # Use the working model
    model_id = "openai/gpt-oss-120b"
    
    web_search_agent = Agent(
        name="Web Search Agent",
        role="Search the web for financial information",
        model=Groq(id=model_id),
        tools=[DuckDuckGo()],
        instructions=[
            "Always include sources",
            "Provide clear and accurate information"
        ],
        show_tool_calls=False,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance AI Agent",
        role="Analyze stocks and provide financial data using Yahoo Finance",
        model=Groq(id=model_id),
        tools=[
            YFinanceTools(
                stock_price=True, 
                analyst_recommendations=True, 
                stock_fundamentals=True,
                company_news=True
            ),
        ], 
        instructions=[
            "Use tables to display the data",
            "Provide clear stock ticker symbols",
            "For Indian stocks use .NS suffix (e.g., TCS.NS, RELIANCE.NS)",
            "For US stocks use just the symbol (e.g., AAPL, MSFT, TSLA)",
            "Format responses in a clear, structured manner"
        ],
        show_tool_calls=False,
        markdown=True,
    )
    
    # Combined agent with all tools - but use sparingly to avoid rate limits
    multi_ai_agent = Agent(
        name="Multi AI Agent",
        role="Financial analysis expert with web search capability",
        model=Groq(id=model_id),
        tools=[
            YFinanceTools(
                stock_price=True, 
                analyst_recommendations=True, 
                stock_fundamentals=True,
                company_news=True
            ),
        ],
        instructions=[
            "Prioritize Yahoo Finance tools for stock data",
            "Use tables to display the data",
            "For Indian stocks: TCS.NS, RELIANCE.NS, INFY.NS, TATAMOTORS.NS",
            "For US stocks: AAPL, MSFT, TSLA, NVDA, GOOGL",
            "Provide comprehensive financial analysis"
        ],
        show_tool_calls=False,
        markdown=True,
    )
    
    return web_search_agent, finance_agent, multi_ai_agent

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agents_initialized" not in st.session_state:
    try:
        st.session_state.web_agent, st.session_state.finance_agent, st.session_state.multi_agent = initialize_agents()
        st.session_state.agents_initialized = True
    except Exception as e:
        st.error(f"Error initializing agents: {str(e)}")
        st.session_state.agents_initialized = False

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Agent selection
    agent_type = st.selectbox(
        "Select Agent",
        ["Multi-Agent Team", "Finance Agent", "Web Search Agent"],
        help="Choose which agent to use for your queries"
    )
    
    st.divider()
    
    # Example queries
    st.subheader("💡 Example Queries")
    
    example_queries = [
        "What is the stock price of NVDA?",
        "Get analyst recommendations for TSLA",
        "Show fundamentals for AAPL",
        "What is the stock price of TATAMOTORS.NS?",
        "Compare TCS.NS and INFY.NS stock prices"
    ]
    
    for query in example_queries:
        if st.button(query, key=query, use_container_width=True):
            st.session_state.example_query = query
    
    st.divider()
    
    # Ticker symbols helper
    with st.expander("📌 Common Stock Tickers"):
        st.markdown("""
**US Stocks** (no suffix):
- AAPL, MSFT, GOOGL, TSLA, NVDA

**Indian Stocks** (add .NS):
- TCS.NS, INFY.NS, RELIANCE.NS
- TATAMOTORS.NS, TATASTEEL.NS
- HDFCBANK.NS, WIPRO.NS
        """)
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # API Status
    st.subheader("🔑 API Status")
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        st.success("✅ Groq API Key loaded")
    else:
        st.error("❌ Groq API Key missing")
    
    st.divider()
    
    # Info
    st.info("""
    **About**
    
    This Financial AI Agent provides:
    - Real-time stock prices
    - Analyst recommendations
    - Company fundamentals
    - Latest financial news
    - Web search capabilities
    """)

# Main content
st.title("📊 Financial AI Agent")
st.markdown("Get real-time financial insights powered by AI")

# Check if agents are initialized
if not st.session_state.agents_initialized:
    st.error("⚠️ Agents failed to initialize. Please check your API keys in the .env file.")
    st.stop()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle example query from sidebar
if "example_query" in st.session_state:
    prompt = st.session_state.example_query
    del st.session_state.example_query
else:
    # Chat input
    prompt = st.chat_input("Ask about stocks, market trends, or financial news...")

if prompt:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        response_container = st.empty()
        with st.spinner("Analyzing..."):
            try:
                # Select the appropriate agent
                if agent_type == "Finance Agent":
                    selected_agent = st.session_state.finance_agent
                elif agent_type == "Web Search Agent":
                    selected_agent = st.session_state.web_agent
                else:
                    selected_agent = st.session_state.multi_agent
                
                # Get response from agent using print_response to capture output
                response_text = ""
                
                # Add retry logic for function calling errors
                max_retries = 2
                retry_count = 0
                success = False
                
                while retry_count < max_retries and not success:
                    try:
                        # Capture the response
                        run_response = selected_agent.run(prompt, stream=False)
                        
                        # Extract the content from response
                        if hasattr(run_response, 'content'):
                            response_text = run_response.content
                        elif hasattr(run_response, 'messages') and len(run_response.messages) > 0:
                            # Get the last message content
                            last_message = run_response.messages[-1]
                            if hasattr(last_message, 'content'):
                                response_text = last_message.content
                            else:
                                response_text = str(last_message)
                        else:
                            response_text = str(run_response)
                        
                        success = True
                        
                    except Exception as e:
                        error_str = str(e)
                        if "tool_use_failed" in error_str and retry_count < max_retries - 1:
                            retry_count += 1
                            # If TATA is mentioned, suggest the correct ticker
                            if "TATA" in prompt.upper():
                                prompt = prompt + " (Note: For Indian stocks, use .NS suffix like TATA.NS)"
                            continue
                        else:
                            raise e
                
                if not response_text:
                    response_text = "I apologize, but I couldn't generate a proper response. Please try rephrasing your question or use a more specific stock ticker symbol."
                
                # Display response
                response_container.markdown(response_text)
                
                # Add assistant response to chat
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                
            except Exception as e:
                error_str = str(e)
                
                # Provide helpful error messages
                if "Ratelimit" in error_str or "rate" in error_str.lower():
                    error_message = """⚠️ Rate limit reached. 
                    
**Please try**:
- Use the **Finance Agent** for stock data (no rate limits)
- Wait a moment before using Web Search again
- For TATA stocks try: **TATAMOTORS.NS**, **TCS.NS**, **TATASTEEL.NS**"""
                
                elif "404" in error_str or "Not Found" in error_str:
                    # Extract ticker if possible
                    ticker_hint = ""
                    if "TATA" in prompt.upper():
                        ticker_hint = "\n\n**Common TATA tickers**: TATAMOTORS.NS, TCS.NS, TATASTEEL.NS, TATAPOWER.NS"
                    
                    error_message = f"""❌ Stock ticker not found. 
                    
**Tips**:
- Check the ticker symbol spelling
- Indian stocks need .NS suffix (e.g., RELIANCE.NS, INFY.NS)
- US stocks don't need suffix (e.g., AAPL, MSFT, TSLA){ticker_hint}"""
                
                elif "tool_use_failed" in error_str:
                    if "TATA" in prompt.upper():
                        error_message = """❌ Unable to fetch stock data. 
                        
**TATA Group Stock Tickers**:
- 🚗 **TATAMOTORS.NS** - Tata Motors
- 💻 **TCS.NS** - Tata Consultancy Services  
- ⚙️ **TATASTEEL.NS** - Tata Steel
- ⚡ **TATAPOWER.NS** - Tata Power
- 🏭 **TATACHEM.NS** - Tata Chemicals

Try: "What is the stock price of TATAMOTORS.NS?\""""
                    else:
                        error_message = """❌ Unable to process your request. 
                        
**Tips**: 
- Use correct ticker symbols (e.g., AAPL, MSFT, GOOGL)
- Indian stocks: Add .NS suffix (TCS.NS, RELIANCE.NS)
- Try the **Finance Agent** for pure stock queries"""
                else:
                    error_message = f"❌ Error occurred: {error_str}\n\n**Tip**: Try the **Finance Agent** for stock data."
                
                response_container.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Footer
st.divider()
st.caption("⚠️ Disclaimer: This is a demo application. Always verify financial information from official sources before making investment decisions.")
