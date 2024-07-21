# Finvest AI

Finvest AI is a financial chat application powered by the Llama3 AI framework and Yahoo Finance data. This application allows users to interact with an AI financial analyst to get various types of stock and company information.

## Overview

This project is designed to provide real-time financial insights and analytics through a chat-based interface. Users can obtain detailed financial data and analysis on stocks, companies, and financial metrics by conversing with the AI agent.

## Features

- **Stock Data**: Retrieve historical stock price movements, including key metrics such as open price, close price, high price, low price, volume, and adjusted close price.
- **Stock Information**: Get a comprehensive snapshot of stock data including current price, market cap, volume, financial ratios, dividend yield, and analyst ratings.
- **Company Information**: Access detailed information about a company, including market capitalization, sector, industry, financial metrics, and more.
- **Stock Dividends**: View information on past and upcoming dividend payments, including dates, amounts, and yields.
- **Income Statements**: Obtain detailed financial performance metrics such as revenue, gross profit, operating expenses, and earnings per share (EPS).
- **Balance Sheets**: Get information on a company's assets, liabilities, and shareholders' equity.
- **Cash Flow Statements**: Understand a company's cash inflows and outflows from various activities to assess liquidity and financial flexibility.
- **Analyst Recommendations**: View buy and sell decisions made by experienced analysts.

## Requirements

- Python 3.x
- Streamlit
- Llama3 (including `llama_index` module)
- Yahoo Finance API
- TogetherAI
- Groq

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/adiagarwalrock/finvest-ai.git
   cd finvest-ai
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Ensure that you have the necessary API keys and environment variables set up for accessing Yahoo Finance data.

   - **GROQ_API_KEY**: Your Groq API key
    - **TOGETHER_AI_API_KEY**: Your Together


## Configuration

- **`agent.py`**: Contains definitions of various financial tools and the AI agent. Customize the tools by modifying the function definitions and descriptions.
- **`app.py`**: Configures the Streamlit interface and integrates with the `financial_react_agent`. Customize the UI and agent settings as needed.

## Usage

To run the application, execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Code Explanation

### `agent.py`

- **Tool Definitions**: Uses the `FunctionTool` class to define tools for retrieving various types of financial data from Yahoo Finance.
- **`ReActAgent`**: Creates an AI agent with the specified tools and configuration for processing chat messages.
- **`prefix_msgs`**: Sets the initial system message to configure the AI agent's behavior.

### `app.py`

- **Streamlit Configuration**: Sets up the Streamlit page layout, title, and initial state for the chat interface.
- **Chat Interface**: Manages chat history and interactions with the AI agent, displaying user and assistant messages.
- **Agent Interaction**: Uses the `financial_react_agent` to process user inputs and generate responses.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or report bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please do not contact the author directly. Instead, open an [issue on GitHub](https://github.com/adiagarwalrock/finvest-ai/issues).
