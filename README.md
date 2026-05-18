# AI Text Assistant — OpenAI API

A command-line AI assistant that processes and improves text using the OpenAI API.
Built with Python, it demonstrates real-world API integration and practical prompt engineering.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| ✍️ Improve text | Rewrites text to be clear, concise, and professional |
| ✅ Correct grammar | Fixes spelling, grammar, and punctuation errors |
| 📋 Summarize | Condenses any text into 3 essential bullet points |
| 🎭 Standardize tone | Rewrites in Formal, Casual, or Friendly tone |

---

## 🧠 Tech Stack

- **Python 3.10+**
- **OpenAI API** (`gpt-4o-mini`)
- **python-dotenv** for secure key management

---

## ⚙️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/pedroceoloni/ai-openai-assistant.git
cd ai-openai-assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your API key**
```bash
cp .env.example .env
```
Open `.env` and replace `your_api_key_here` with your real [OpenAI API key](https://platform.openai.com/api-keys).

**4. Run the assistant**
```bash
python main.py
```

---

## 💡 Usage Examples

### Improve Text
**Input:**
```
i have problem with my system not working good and need help fast
```
**Output:**
```
I am experiencing issues with my system and require immediate assistance.
```

---

### Correct Grammar
**Input:**
```
She dont knows how to use the system since yesterday
```
**Output:**
```
She doesn't know how to use the system since yesterday.
```

---

### Summarize Text
**Input:**
```
Artificial intelligence is transforming industries worldwide. From healthcare
to finance, AI tools are automating repetitive tasks, improving decision-making,
and enabling new business models. However, concerns about job displacement and
ethical use remain important topics of discussion.
```
**Output:**
```
• AI is transforming multiple industries by automating tasks and improving decisions.
• New business models are emerging as a direct result of AI adoption.
• Job displacement and ethical concerns are key challenges that must be addressed.
```

---

### Standardize Tone

**Input (Casual → Formal):**
```
hey can u check this out asap? kinda important lol
```
**Output:**
```
Could you please review this at your earliest convenience? It is a matter of some importance.
```

---

## 📁 Project Structure

```
ai-openai-assistant/
│
├── main.py           # Core application logic
├── requirements.txt  # Python dependencies
├── .env.example      # API key template (safe to commit)
├── .gitignore        # Keeps .env out of version control
└── README.md         # Project documentation
```

---

## 🔒 Security Note

Your API key is stored in a local `.env` file which is listed in `.gitignore`.
This means it will **never be accidentally committed to GitHub**.
Always use `.env.example` as the public template.

---

## 📫 Contact

Pedro Ceoloni — pedroceoloni@hotmail.com  
GitHub: [@pedroceoloni](https://github.com/pedroceoloni)
