"""core/llm.py — 教程第 1 步：打通 LLM API。

读取环境变量 OPENAI_API_KEY / OPENAI_BASE_URL（DeepSeek 用 https://api.deepseek.com/v1），
发一条测试消息并打印回复，用于验证环境是否调通。

运行：
    python core/llm.py
"""
import os

try:
    from dotenv import load_dotenv
    load_dotenv()  # 若项目根目录有 .env 会自动加载，没有也不会报错
except ImportError:
    pass

from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = os.environ.get("OPENAI_BASE_URL")
MODEL = os.environ.get("OPENAI_MODEL", "deepseek-chat")


def get_client() -> OpenAI:
    if not API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY 未设置。请先执行：\n"
            '  export OPENAI_API_KEY="sk-你的真实key"\n'
            '  export OPENAI_BASE_URL="https://api.deepseek.com/v1"'
        )
    return OpenAI(api_key=API_KEY, base_url=BASE_URL)


def chat(prompt: str, *, model: str = MODEL, temperature: float = 0.7) -> str:
    """向大模型发一条 user 消息，返回回复文本。"""
    client = get_client()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    test_prompt = "用一句话向一个零基础初学者解释：什么是 Agent？"
    print(f"[测试] model={MODEL}  prompt={test_prompt!r}")
    try:
        reply = chat(test_prompt)
        print("\n模型回复：")
        print(reply)
        print("\n✅ LLM API 调通，教程第 1 步完成！")
    except Exception as exc:  # noqa: BLE001
        print(f"\n❌ 调用失败：{type(exc).__name__}: {exc}")
        print("常见原因：Key 是占位符/填错、BASE_URL 不对、或网络被代理拦。")
