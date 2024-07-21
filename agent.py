from llama_index.core.agent import ReActAgent
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.tools import FunctionTool


from tools import (
    get_stock_data,
    get_stock_info,
    get_company_info,
    get_stock_dividends,
    get_income_stmt,
    get_balance_sheet,
    get_cash_flow,
    get_analyst_recommendations,
)
import prompts
from llms import get_together_lm

# Define tools for each function
get_stock_data_tool = FunctionTool.from_defaults(fn=get_stock_data)
get_stock_info_tool = FunctionTool.from_defaults(fn=get_stock_info)
get_company_info_tool = FunctionTool.from_defaults(fn=get_company_info)
get_stock_dividends_tool = FunctionTool.from_defaults(fn=get_stock_dividends)
get_income_stmt_tool = FunctionTool.from_defaults(fn=get_income_stmt)
get_balance_sheet_tool = FunctionTool.from_defaults(fn=get_balance_sheet)
get_cash_flow_tool = FunctionTool.from_defaults(fn=get_cash_flow)
get_analyst_recommendations_tool = FunctionTool.from_defaults(
    fn=get_analyst_recommendations
)


prefix_msgs = [
    ChatMessage(role=MessageRole.SYSTEM, content=prompts.GPT_FINANCIAL_ANALYST_SYS_STR)
]


financial_react_agent = ReActAgent.from_tools(
    [
        get_stock_data_tool,
        get_stock_info_tool,
        get_company_info_tool,
        get_stock_dividends_tool,
        get_income_stmt_tool,
        get_balance_sheet_tool,
        get_cash_flow_tool,
        get_analyst_recommendations_tool,
    ],
    llm=get_together_lm(),
    prefix_messages=prefix_msgs,
    token_counting=True,
    verbose=True,
    max_iterations=20,
)
