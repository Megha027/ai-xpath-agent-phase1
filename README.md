# 🤖 AI XPath Agent (Phase 1)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parser-orange)
![Ollama](https://img.shields.io/badge/Ollama-Qwen2.5%3A3B-purple)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered XPath generation tool built using **Python**, **Selenium**, **BeautifulSoup**, and **Ollama**.

This project extracts interactive web elements from a webpage, generates XPath locators using a locally running Large Language Model (LLM), validates the generated XPath using Selenium, and exports the results to an Excel report.

**Phase 1** focuses on building a simple, end-to-end AI-assisted XPath generation workflow.

---

# 📌 Project Status

**Current Version:** Phase 1 (v1.0)

### ✅ Completed

- Browser Automation
- DOM Extraction
- HTML Parsing
- AI XPath Generation
- XPath Validation
- Excel Report Generation

### 🚀 Next Phase

- Duplicate XPath Detection
- Retry Mechanism
- Smarter XPath Generation

---

# 📌 Features

- Launch browser using Selenium
- Open any target webpage
- Extract interactive elements (Input, Button, Link)
- Parse HTML using BeautifulSoup
- Generate XPath using Ollama (Qwen2.5:3B)
- Validate generated XPath using Selenium
- Export results to Excel
- Modular project architecture

---

# 🏗️ Architecture

```
                +------------------+
                |    main.py       |
                +--------+---------+
                         |
                         v
                +------------------+
                | Orchestrator     |
                +--------+---------+
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
+---------------+  +--------------+  +----------------+
| BrowserAgent  |  | DOM Agent    |  | AI Agent       |
+---------------+  +--------------+  +----------------+
        |                |                |
        |                |                |
        |                +------HTML------+
        |                                 |
        |                          Generate XPath
        |                                 |
        +---------------------------------+
                         |
                         v
               +-------------------+
               | XPath Validator   |
               +-------------------+
                         |
                         v
                +------------------+
                | Excel Writer     |
                +------------------+
```

---

# 📂 Project Structure

```
XpathAgentPython/
│
├── agents/
│   ├── ai_agent.py
│   ├── dom_agent.py
│   └── orchestrator.py
│
├── browser/
│   └── browser_manager.py
│
├── models/
│   └── web_element.py
│
├── prompts/
│   └── xpath_prompt.txt
│
├── reports/
│
├── services/
│   └── excel_writer.py
│
├── utils/
│   ├── logger.py
│   ├── prompt_loader.py
│   └── response_parser.py
│
├── validators/
│   └── xpath_validator.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

- Python 3.11
- Selenium
- BeautifulSoup4
- LXML
- Ollama
- Qwen2.5:3B
- OpenPyXL

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-github-username>/ai-xpath-agent.git
```

## 2. Navigate to the Project

```bash
cd ai-xpath-agent
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Ollama

Download and install Ollama from:

https://ollama.com

---

## 5. Pull the AI Model

```bash
ollama pull qwen2.5:3b
```

---

## 6. Start Ollama

```bash
ollama serve
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🔄 Workflow

```
Start Browser
      │
      ▼
Open Target URL
      │
      ▼
Extract Interactive Elements
      │
      ▼
Generate XPath using AI
      │
      ▼
Validate XPath
      │
      ▼
Export Excel Report
      │
      ▼
Close Browser
```

---

# 📝 Example Console Output

```
Element : Full Name

XPath : //input[@id='userName']

Validation : VALID

------------------------------------------------------

Element : Email

XPath : //input[@id='userEmail']

Validation : VALID

------------------------------------------------------

Element : Submit

XPath : //button[@id='submit']

Validation : VALID
```

---

# 📊 Example Excel Report

| Element | Tag | AI XPath | Validation |
|---------|-----|-----------|------------|
| Full Name | Input | //input[@id='userName'] | VALID |
| Email | Input | //input[@id='userEmail'] | VALID |
| Submit | Button | //button[@id='submit'] | VALID |

---

# 📸 Screenshots

## Console Output

Place your screenshot here.

```
images/
    console_output.png
```

---

## Excel Report

Place your screenshot here.

```
images/
    excel_report.png
```

---

# 💡 Use Cases

- Selenium Test Automation
- XPath Generation
- QA Productivity
- Automation Framework Development
- AI-assisted Testing
- Learning Selenium with AI

---

# 🚀 Roadmap

## Phase 2

- Detect duplicate XPaths
- Retry invalid XPath generation
- Generate more reliable locators

## Phase 3

- Self-healing XPath generation
- CSS Selector generation
- Relative XPath generation
- Multiple locator strategies

## Phase 4

- FastAPI REST API
- HTML Report
- JSON Export
- Screenshot Capture
- Support for multiple LLMs

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Megha Baghele**

QA Engineer | AI Automation Enthusiast

GitHub:
https://github.com/<your-github-username>

LinkedIn:
https://linkedin.com/in/<your-linkedin-profile>