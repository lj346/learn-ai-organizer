import time
from pathlib import Path          # 导入 pathlib
from openai import OpenAI

# ---------- 配置 ----------
DEEPSEEK_API_KEY = "你的DeepSeek API Key"   # 替换成真实的 key
BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"
OUTPUT_DIR = "outputs"                       # 输出文件夹名称
# ------------------------

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=BASE_URL)

system_prompt = """
你是一个学习资料整理助手。用户会给你一段原始文本。
请严格按照以下格式输出，不要加额外内容：

核心总结（一句话）：
[写一句话]

关键知识点：
- [知识点1]
- [知识点2]
- [知识点3]
- [不超过5个]

自测问题：
[根据内容提一个有价值的问答题，答案应在原文中能找出]
"""

# ---------- 输入处理（优先读 input.txt，否则让用户粘贴）----------
input_path = Path("input.txt")                # 指向 input.txt 的路径对象

if input_path.exists():                       # 判断文件是否存在
    user_text = input_path.read_text(encoding="utf-8")   # 读文件（简便写法）
    print("📄 已从 input.txt 读取内容。")
else:
    print("📝 没有找到 input.txt，请在下方粘贴你的笔记/文章（粘贴后按 Ctrl+D 或 Ctrl+Z 并回车结束）：")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    user_text = "\n".join(lines)
    if not user_text.strip():
        print("❌ 未输入任何内容，退出。")
        exit(1)
    print("✅ 已接收文本，开始处理...\n")
# -------------------------------------------------------------

# 调用 API
try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0.3
    )
except Exception as e:
    print(f"❌ API 调用失败：{e}")
    exit(1)

result = response.choices[0].message.content

# ---------- 创建输出文件夹 ----------
output_dir = Path(OUTPUT_DIR)                     # 指向 outputs 文件夹
output_dir.mkdir(parents=True, exist_ok=True)     # 创建文件夹（安全）

# ---------- 生成输出文件路径 ----------
timestamp = time.strftime("%Y%m%d_%H%M%S")
output_filename = f"output_{timestamp}.txt"
output_path = output_dir / output_filename        # 拼接：outputs/output_xxx.txt

# ---------- 写文件（使用你熟悉的 open）----------
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result)

print(f"✅ 成功！结果已保存到 {output_path}")