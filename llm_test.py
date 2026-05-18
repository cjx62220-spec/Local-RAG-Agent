from openai import OpenAI

# 1. 你的硅基流动 Key（直接用你之前跑通的）
api_key = 'sk-ghwlqhnnjhncittaotjzrgyomwhftwuzahpkcgjkdngmuuyh' 

# 2. 初始化客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.siliconflow.cn/v1" 
)

# 3. 提前定义好 LangGPT 结构化提示词（注意：必须放在外面）
sys_prompt = """
# Role: 数据抽取专家

## Profile
- author: 万涛
- version: 1.0
- language: 中文
- description: 你是一个无情的 JSON 生成机器。你的任务是从用户输入的散文或日记中，提取出关键结构化信息。

## Rules
1. 必须且只能输出合法的 JSON 格式字符串！
2. 绝对禁止输出任何解释性文字、问候语，严禁使用 ```json 这样的 Markdown 代码块标记。
3. 如果找不到对应的信息，该字段的值填 null。

## Workflow
1. 阅读用户输入的文本。
2. 提取以下三个字段：
   - `destinations`: 计划前往的城市（数组格式）
   - `transportation`: 提到的交通工具
   - `accommodation`: 住宿偏好
3. 直接输出最终的 JSON。
"""

# 4. 提前定义好要测试的用户输入
user_input = "等今年清明节放完假，我打算弄个15天的穷游计划。先去西安看兵马俑，然后转战成都吃火锅，最后去重庆走走。为了省钱，晚上可以选择在绿皮火车上度过，或者到了当地直接住青旅，主打一个特种兵式旅游。"

print("正在调用大模型提取结构化数据，请稍候...\n")

# 5. 发送请求（把刚才定义好的变量塞进 messages 里）
response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_input}
    ]
)

# 6. 打印 AI 纯净的 JSON 回复
ai_answer = response.choices[0].message.content
print(f"提取结果：\n{ai_answer}")