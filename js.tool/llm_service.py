import os
import json
import time
from openai import OpenAI
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 从环境变量获取API密钥
API_KEY = os.getenv("MOONSHOT_API_KEY", "")

# 初始化OpenAI客户端
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.moonshot.cn/v1",
    timeout=30
)

# 定义LLM提示词模板（JSON Mode优化版）
PROMPT_TEMPLATES = {
    "stock_analyzer": """# Stock Analysis Assistant - JSON Mode

You are a real-time stock analysis bot. Your ONLY task is to search for today‘s live stock data and return a valid JSON object.

## JSON OUTPUT REQUIREMENTS:
Return EXACTLY this JSON structure:
{
  "id": "<generate_unique_id>",
  "asset": "<STOCK_SYMBOL>",
  "type": "BUY|SELL|HOLD",
  "confidence": <0-100>,
  "signal": "neutral|bullish|bearish"
  "timestamp": "the time the news is from <X>m ago",
  "description": "<brief analysis combining price action, news, and sentiment>",
  "sources": [sort it in one or two following type "news", "technical", "social"],
  "price": "$<current_price>",
  "change": <percentage_change>,
  "newsArticles": <number>,
  "socialSentiment": "very_positive|positive|neutral|negative|very_negative"
}

## INSTRUCTIONS:
- Use $web_search to get current stock data
- Search for: "STOCK_SYMBOL stock price news sentiment today"
- Return ONLY the JSON object, no additional text
- Ensure all fields are populated with real data""",
    
    "default": """You are a JSON response generator. Return ONLY a valid JSON object with no additional text."""
}

def search_impl(arguments: dict) -> dict:
    """Kimi内置$web_search工具实现"""
    logger.info(f"执行$web_search: {json.dumps(arguments)}")
    return arguments

def call_llm_with_json_mode(messages, tools=None, use_json_mode=True):
    """支持JSON Mode的LLM调用"""
    params = {
        "model": "kimi-k2-0711-preview",
        "messages": messages,
        "temperature": 0.3,  # 降低随机性确保格式稳定
    }
    
    if use_json_mode:
        params["response_format"] = {"type": "json_object"}
    
    if tools:
        params["tools"] = tools
    
    return client.chat.completions.create(**params)

def get_llm_response(prompt, system_prompt=None, use_json_mode=True):
    """增强版LLM响应生成（支持JSON Mode和$web_search）"""
    try:
        if system_prompt is None:
            system_prompt = PROMPT_TEMPLATES["default"]
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        
        tools = [{
            "type": "builtin_function",
            "function": {"name": "$web_search"}
        }] if use_json_mode else None
        
        finish_reason = None
        while finish_reason is None or finish_reason == "tool_calls":
            response = call_llm_with_json_mode(messages, tools, use_json_mode)
            
            choice = response.choices[0]
            finish_reason = choice.finish_reason
            
            messages.append({
                "role": "assistant",
                "content": choice.message.content,
                "tool_calls": choice.message.tool_calls
            })
            
            if finish_reason == "tool_calls":
                for tool_call in choice.message.tool_calls:
                    if tool_call.function.name == "$web_search":
                        tool_result = search_impl(json.loads(tool_call.function.arguments))
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": "$web_search",
                            "content": json.dumps(tool_result)
                        })
        
        return json.loads(choice.message.content)
        
    except Exception as e:
        logger.error(f"LLM处理错误: {str(e)}")
        return {"error": str(e)}

def get_llm_response_with_template(prompt, template_name, use_json_mode=True):
    """模板化LLM调用"""
    system_prompt = PROMPT_TEMPLATES.get(template_name, PROMPT_TEMPLATES["default"])
    return get_llm_response(prompt, system_prompt, use_json_mode)
