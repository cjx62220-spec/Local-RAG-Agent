import requests  # 导入 requests 库，用于发起网络请求
import re  # 导入 re，用于用正则从 HTML 中提取 <title> 内容

# 发送 GET 请求，获取百度首页的 HTML 内容
response = requests.get("https://www.baidu.com/")

# 百度首页有时编码信息在响应头里不够准确；这里直接用 apparent_encoding 做兜底，
# 让 response.text 更接近实际页面编码（避免中文乱码）
response.encoding = response.apparent_encoding

# 检查请求是否成功
if response.status_code == 200:
    # 从 HTML 中提取 <title>...</title> 内的文本
    # re.DOTALL：让 '.' 能匹配换行
    # re.IGNORECASE：不区分 title 标签大小写
    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, flags=re.DOTALL | re.IGNORECASE)

    if match:
        # title 内可能包含多余空白/换行，这里统一折叠为空格后再打印
        title = re.sub(r"\s+", " ", match.group(1)).strip()
    else:
        title = "没有找到标题"

    # 打印网页的标题
    print("网页的标题是：", title)
else:
    # 如果请求失败，输出错误信息
    print("请求失败，状态码：", response.status_code)