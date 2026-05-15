# AI 学习资料自动整理器
将杂乱的笔记、文章或 PDF 中的文字，一键整理成结构清晰的学习笔记，并同时保留原始内容，方便对照复习。

## 功能特点
- ✨ **智能整理**：调用 DeepSeek API 自动生成：
  - 一句话核心总结
  - 3~5 个关键知识点
  - 一道自测问题
- 📄 **保留原文**：输出文件同时包含你输入的原始文本和 AI 整理结果，无需来回翻看。
- 🖥️ **灵活输入**：
  - 直接运行脚本后粘贴文本（支持多行，Ctrl+D/Ctrl+Z 结束）
  - 或提前将内容保存为 `input.txt`，脚本自动读取
- 🔒 **本地优先**：所有数据都在本地处理，只有文本内容发送给 AI，输出结果保存在本地文件夹。
- 📂 **自动管理**：自动创建 `outputs/` 文件夹，输出文件自动带时间戳，不会覆盖历史记录。

## 项目结构
```
.
├── deepseek api测试.py      # 主程序
├── input.txt               # (可选) 输入文件，存在时自动优先读取
├── outputs/                # 整理后的笔记存放目录
├── .gitignore              # Git 忽略规则（含 outputs/、input.txt、密钥文件等）
└── README.md               # 项目说明
```

## 快速开始
### 1. 环境要求
- Python 3.8 或更高版本
- Git（可选，用于克隆仓库）
- 一个 [DeepSeek](https://platform.deepseek.com/) 账号（获取 API Key）

### 2. 克隆或下载代码
```bash
git clone https://github.com/lj346/learn-ai-organizer.git
cd learn-ai-organizer
```
或者直接下载 ZIP 包解压。

### 3. 安装依赖
```bash
pip install openai
```

### 4. 配置 API Key
**方式一（推荐）：使用环境变量**
- Windows（PowerShell）：
```powershell
$env:DEEPSEEK_API_KEY="你的真实API Key"
```
- Windows（CMD）：
```cmd
set DEEPSEEK_API_KEY=你的真实API Key
```
- Linux / macOS：
```bash
export DEEPSEEK_API_KEY="你的真实API Key"
```

**方式二：直接修改脚本**
打开 `deepseek api测试.py`，找到下面这行：
```python
DEEPSEEK_API_KEY = "你的DeepSeek API Key"
```
将 `YOUR_API_KEY_HERE` 替换为你的真实 API Key（注意不要上传到公开仓库）。

> ⚠️ **安全提醒**：如果你的仓库是公开的，千万不要把真实 API Key 硬编码提交到 GitHub。推荐始终使用环境变量。

### 5. 运行脚本
```bash
python "deepseek api测试.py"
```
脚本会按以下优先级获取输入内容：
1. 如果当前目录存在 `input.txt` 文件，自动读取该文件内容。
2. 如果没有 `input.txt`，则提示你在终端直接粘贴文本。粘贴后按 `Ctrl+D`（Linux/macOS）或 `Ctrl+Z` 然后回车（Windows）结束输入。

处理完成后，输出文件会自动保存在 `outputs/` 文件夹中，文件名格式为 `output_年月日_时分秒.txt`。

### 6. 查看结果
打开 `outputs/` 目录，找到最新生成的 `.txt` 文件，内容示例：
```
【原始笔记】
（你粘贴的原始文本）

【AI 整理】
核心总结（一句话）：
本文介绍了 Git Flow 分支模型及常用 Git 命令。

关键知识点：
- Git Flow 分支类型：main, develop, feature/*, release/*, hotfix/*
- 版本号规则：v0.0.1 内测版，v1.0.0 正式版
- 常用命令：git checkout -b、git merge、git tag

自测问题：
在 Git Flow 流程中，线上出现紧急问题应该使用哪个分支修复？修复后需要合并到哪些分支？
```

## 常见问题
### Q1: 运行时提示 `ModuleNotFoundError: No module named 'openai'`
需要安装依赖：`pip install openai`。如果使用了虚拟环境，请确保已激活虚拟环境。

### Q2: API 调用失败，提示 `AuthenticationError`
- 请检查 API Key 是否正确（是否复制完整，是否有多余空格）。
- 确认 DeepSeek 账户有余额或剩余免费额度。

### Q3: 推送代码到 GitHub 时出现 `Connection was reset`
通常是网络代理问题。可以尝试：
- 配置 Git 代理：`git config --global http.proxy http://127.0.0.1:7890`（端口换成你自己的代理端口）
- 或改用 SSH 方式推送（推荐）。

### Q4: 我想让输出格式更符合自己的习惯
编辑 `deepseek api测试.py` 中的 `system_prompt` 变量，修改输出格式。例如增加“延伸思考”部分，或要求用表格输出知识点。

## 后续计划
- [ ] 支持批量处理文件夹内的多个 `.txt` / `.md` 文件
- [ ] 增加从 PDF 直接提取文字的功能
- [ ] 提供配置文件，允许用户自定义输出模板
- [ ] 图形化界面（可选）

## 许可证
本项目仅供个人学习使用，你可以自由修改和分享。

## 作者
lj346

## 致谢
- [DeepSeek](https://www.deepseek.com/) 提供的高性价比 API
- 所有提出改进建议的网友
