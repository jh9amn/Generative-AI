> https://smithery.ai/
> https://github.com/openbnb-org/mcp-server-airbnb


# 🧠 Model Context Protocol (MCP) Servers — Complete Guide from Scratch

---

## 📌 What is MCP (Model Context Protocol)?

**Model Context Protocol (MCP)** is a standardized way to connect **AI models (like LLMs)** with external tools, APIs, and data sources.

👉 Think of MCP as a **bridge** between:

* 🧠 AI Models (LLMs)
* 🔧 Tools (search, database, APIs)
* 📂 External Data (files, websites, apps)

---

## 🎯 Why MCP is Important?

Without MCP:

* AI is limited to its training data
* No real-time info
* No external actions

With MCP:

* ✅ Real-time web search
* ✅ Access databases
* ✅ Run commands
* ✅ Interact with apps (GitHub, Airbnb, etc.)
* ✅ Build AI agents & copilots

---

## 🏗️ MCP Architecture

```
User → AI Model → MCP Client → MCP Server → Tool/API → Response → AI → User
```

### Components:

| Component      | Description                  |
| -------------- | ---------------------------- |
| **AI Model**   | GPT / LLM handling reasoning |
| **MCP Client** | Sends tool requests          |
| **MCP Server** | Executes tool logic          |
| **Tools/APIs** | External capabilities        |

---

## 🔌 What is an MCP Server?

An **MCP Server** is a tool provider that:

* Exposes capabilities (search, booking, file access)
* Communicates with AI via MCP standard
* Runs locally or remotely

---

## 📦 Types of MCP Servers

### 1. 🌐 Web Search Server

* Example: DuckDuckGo MCP
* Use: Fetch latest info

### 2. 🏠 API-Based Servers

* Example: Airbnb MCP
* Use: Booking, listings

### 3. 📁 File System Server

* Read/write local files

### 4. 🧑‍💻 Dev Tool Servers

* GitHub, terminal, code execution

### 5. 🧠 Custom Servers

* Your own APIs / business logic

---

## ⚙️ Basic MCP Config Structure

```json
{
  "preferences": {
    "featureFlag": true
  },
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "package-name"]
    }
  }
}
```

---

## 🔍 Example 1: DuckDuckGo Search MCP

```json
{
  "duckduckgo-search": {
    "command": "npx",
    "args": [
      "-y",
      "duckduckgo-mcp-server"
    ]
  }
}
```

### 🔧 What it does:

* Enables AI to search internet
* Returns real-time results

---

## 🏠 Example 2: Airbnb MCP Server

```json
{
  "airbnb": {
    "command": "npx",
    "args": [
      "-y",
      "@openbnb/mcp-server-airbnb"
    ]
  }
}
```

### 🔧 What it does:

* Fetch Airbnb listings
* Supports booking-related queries

---

## 🚀 Running MCP Servers

### Step 1: Install Node.js

```bash
node -v
npm -v
```

---

### Step 2: Run MCP Server

```bash
npx -y duckduckgo-mcp-server
```

---

### Step 3: Connect to AI Client

* Use tools like:

  * LangChain
  * OpenAI SDK
  * Custom agent frameworks

---

## 🔗 MCP with LangChain (Example)

```python
from langchain.tools import Tool

def search_tool(query):
    # connect to MCP server
    return "Search result"

tool = Tool(
    name="Search",
    func=search_tool,
    description="Search the web"
)
```

---

## 🧠 MCP in AI Copilot (Your Use Case)

### Architecture for AI Developer Copilot:

```
User → Chat UI → LLM
                 ↓
            MCP Client
                 ↓
     ------------------------
     |   Search MCP         |
     |   GitHub MCP         |
     |   File System MCP    |
     ------------------------
                 ↓
             Response
```

---

## 🛠️ Useful MCP Servers

| Tool       | Package                    |
| ---------- | -------------------------- |
| Web Search | duckduckgo-mcp-server      |
| Airbnb     | @openbnb/mcp-server-airbnb |
| Filesystem | (custom / community)       |
| GitHub     | (custom MCP)               |

---

## ⚠️ Common Mistakes

### ❌ Wrong Key

```json
"commands": "npx"
```

✔ Fix:

```json
"command": "npx"
```

---

### ❌ Typo in JSON

```json
"coworkSch,eduledTasksEnabled"
```

✔ Fix:

```json
"coworkScheduledTasksEnabled"
```

---

### ❌ Invalid JSON Format

* Missing commas
* Wrong brackets

---

## 🔐 Security Considerations

* Avoid:

  * `--ignore-robots-txt`
  * Untrusted MCP servers

* Always:

  * Validate inputs
  * Restrict permissions
  * Use sandboxing

---

## 📁 Full Working MCP Config

```json
{
  "preferences": {
    "coworkWebSearchEnabled": true,
    "ccdScheduledTasksEnabled": false,
    "coworkScheduledTasksEnabled": false
  },
  "mcpServers": {
    "duckduckgo-search": {
      "command": "npx",
      "args": [
        "-y",
        "duckduckgo-mcp-server"
      ]
    },
    "airbnb": {
      "command": "npx",
      "args": [
        "-y",
        "@openbnb/mcp-server-airbnb"
      ]
    }
  }
}
```

---

## 🎯 When Should You Use MCP?

Use MCP when you want:

* 🔄 Real-time data
* 🔧 Tool integration
* 🤖 AI agents
* 🧠 Smart copilots
* 📡 External API access

---

## 🔥 Next Steps (Recommended for You)

Since you're building an **AI Developer Copilot**, next learn:

1. ✅ MCP + LangChain integration
2. ✅ RAG (Retrieval-Augmented Generation)
3. ✅ Tool calling agents
4. ✅ Custom MCP server creation

---

## 💡 Summary

* MCP = Tool bridge for AI
* MCP Server = Tool provider
* Enables real-world AI capabilities
* Essential for modern AI apps

---

## 🚀 Want More?

I can help you next with:

* ✅ Build your **own MCP server**
* ✅ Integrate MCP with **Express.js / Node**
* ✅ Create full **AI Copilot architecture**

Just tell me 👍
