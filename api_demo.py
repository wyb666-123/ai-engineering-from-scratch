import os, json, urllib.request
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ["ZHIPU_API_KEY"]
BASE_URL = "https://open.bigmodel.cn/api/paas/v4"
MODEL = os.environ.get("ZHIPU_MODEL", "glm-4-flash")
PROMPT = "What is a neural network in one sentence?"

def call_with_sdk():
    from openai import OpenAI
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    resp = client.chat.completions.create(
        model=MODEL, max_tokens=256,
        messages=[{"role": "user", "content": PROMPT}])
    return resp.choices[0].message.content

def call_with_raw_http():
    url = f"{BASE_URL}/chat/completions"
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {API_KEY}"}
    body = json.dumps({"model": MODEL, "max_tokens": 256,
        "messages": [{"role": "user", "content": PROMPT}]}).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("=== SDK 版 ==="); print(call_with_sdk())
    print("\n=== 原始 HTTP 版 ==="); print(call_with_raw_http())
