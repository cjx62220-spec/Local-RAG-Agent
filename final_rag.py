import os
import sys
import docx2txt # 直接用这个库，不走 LangChain 的 Loader 绕弯路

# 1. 强制添加路径
sys.path.append(r'C:\Users\81806\AppData\Roaming\Python\Python310\site-packages')
sys.path.append(r'C:\Users\81806\AppData\Local\Programs\Python\Python310\Lib\site-packages')

# 2. 导入核心组件 (避开那几个报错的 loader)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.schema import Document

# --- 配置区域 ---
MY_API_KEY = "sk-ghwlqhnnjhncittaotjzrgyomwhftwuzahpkcgjkdngmuuyh"
MY_BASE_URL = "https://api.siliconflow.cn/v1"

# --- 核心逻辑：暴力读取 Word ---
print("🚀 正在用最原始的方式读取论文 (绕过系统兼容性 Bug)...")
text = docx2txt.process("毕业论文.docx")
docs = [Document(page_content=text)] # 手动封装成 LangChain 能认的格式

# 切分
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
chunks = text_splitter.split_documents(docs)

# 向量化
embeddings = OpenAIEmbeddings(
    openai_api_key=MY_API_KEY,
    openai_api_base=MY_BASE_URL,
    model="BAAI/bge-m3"
)
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

print("🧠 正在呼叫 DeepSeek 指导老师...")
llm = ChatOpenAI(
    openai_api_key=MY_API_KEY,
    openai_api_base=MY_BASE_URL,
    model_name="deepseek-ai/DeepSeek-V3",
    temperature=0.1
)

rag_chat = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

# --- 终极火力测试 ---
question = "论文摘要里提到了本项目的什么意义？"
print(f"\n👤 提问：{question}")
answer = rag_chat.run(question)
print(f"\n🤖 导师回答：\n{'-'*40}\n{answer}\n{'-'*40}")