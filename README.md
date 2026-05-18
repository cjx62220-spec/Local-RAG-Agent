# 🧠 Local-RAG-Agent: 基于大模型的纯本地化检索增强生成系统

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Local-orange.svg)
![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek--V3-blueviolet.svg)

## 📖 项目简介
本项目是一个脱离传统“拖拽式”低代码平台、完全**纯代码从零构建**的本地化检索增强生成（RAG）系统。旨在解决大模型在特定垂直领域的“幻觉”问题，实现对超长非结构化文档的精准知识检索与智能问答。系统数据完全本地化流转，保障数据隐私与安全。

## ✨ 核心特性
* **📄 自动化文档解析**：集成 `docx2txt` 等工具，针对非结构化长文档实现深度清洗与提取。
* **✂️ 智能物理切片**：采用 `RecursiveCharacterTextSplitter` 算法，自定义 Chunk Size 与 Overlap，保证上下文语义连贯。
* **🧮 高效向量检索**：接入 `BAAI/bge-m3` 顶级 Embedding 模型，结合本地化部署的 `Chroma` 向量数据库，实现基于余弦相似度的 Top-K 精准召回。
* **🔗 大模型无缝联动**：基于 `LangChain` 框架的 `RetrievalQA` 链，无缝对接 `DeepSeek-V3` (通过硅基流动 API)，并辅以严苛的 System Prompt 约束，确保回答 100% 忠于本地知识库。

## 架构概览

```mermaid
graph TD
    A[📄 本地长文档] -->|解析| B(文本清洗 docx2txt)
    B --> C{智能切片 TextSplitter}
    C -->|Chunk| D[向量化 BAAI/bge-m3]
    D --> E[(本地 ChromaDB 向量库)]
    
    F[👤 用户提问 Query] --> G[相似度检索 Top-K]
    E -.->|提供高维向量| G
    G -->|召回相关上下文| H(组装 System Prompt)
    H --> I[🧠 大模型 DeepSeek-V3]
    I --> J((✨ 输出精准回答))
    
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef database fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    class E database;

## 🛠️ 技术栈
* **核心语言**: Python
* **大模型/API**: DeepSeek-V3, 硅基流动 (SiliconFlow) API
* **AI 编排框架**: LangChain
* **向量数据库**: ChromaDB (本地持久化部署)
* **Embedding 模型**: BAAI/bge-m3
* **前端交互**: Vue.js (构建流式输出的问答交互界面)

## 🚀 快速启动

### 1. 环境准备
```bash
# 克隆仓库
git clone [https://github.com/YourUsername/Local-RAG-Agent.git](https://github.com/YourUsername/Local-RAG-Agent.git)
cd Local-RAG-Agent

# 推荐使用 conda 或 venv 创建虚拟环境以隔离依赖
python -m venv venv
source venv/bin/activate  # Windows 用户请使用 venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
