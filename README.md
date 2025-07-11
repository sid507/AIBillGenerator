# 🧾 AI Bill Generator

Generate beautiful, themed bills from natural language prompts using LLMs, LangChain, and Jinja2! Extract structured data (date, items, totals, and even bill themes) from plain text and instantly render stylish receipts as HTML or PNG.

---

## 🚀 Features

- **Natural Language to Bill:**  
  Enter prompts like “Generate a bill for 3 burgers and 2 fries with a dark theme for today” and get a ready-to-render bill.

- **Dynamic Theme Extraction:**  
  The AI can pick from classic, modern, café, dark, or even invent new themes based on your prompt.

- **Structured Output:**  
  LLM returns a strict JSON format with all bill details and theme CSS.

- **Instant Rendering:**  
  Bills are rendered using Jinja2 templates and can be displayed in a web app (Streamlit) or downloaded as PNG.

- **Customizable:**  
  Easily add new themes or modify templates to fit your brand.

---

## 🛠️ How It Works

1. **User Input:**  
   User enters a prompt describing the bill and (optionally) the theme.

2. **LLM Extraction:**  
   The system prompt guides the LLM to extract date, items, grand total, and theme, filling in missing info if needed.

3. **Backend Processing:**  
   The backend parses the LLM’s JSON output.

4. **Template Rendering:**  
   Data and theme are injected into a Jinja2 HTML template.

5. **Display/Download:**  
   The bill is shown in the web app and can be downloaded as an image.

---

## 📦 Example Prompt & Output

**Prompt:**  
```
Generate a bill for 2 cappuccinos and 1 croissant with a cozy café theme.
```

**LLM Output (JSON):**
```json
{
  "date": "2025-07-11",
  "items": [
    {"name": "Cappuccino", "qty": 2, "price": 120},
    {"name": "Croissant", "qty": 1, "price": 80}
  ],
  "grandTotal": 320,
  "theme": {
    "font_family": "'Comic Sans MS', cursive",
    "bg": "#fff8dc",
    "font_color": "#4b2e2e",
    "header_text": "☕ Cozy Cafe Receipt ☕",
    "footer_text": "Hope you enjoyed your coffee! Come back soon!"
  }
}
```

---

## 🖼️ Themes Included

- **Classic**
- **Crumbled Paper**
- **Modern Blue**
- **Dark Mode**
- **Café**
- *(Or invent your own!)*

---

## 🏗️ Project Structure

```
AI_Trip_Planner/
├── streamlit_app.py         # Streamlit frontend
├── utils/
│   └── billGenerator.py     # Bill rendering logic
├── tools/
│   └── billGeneratorTool.py # LLM tool integration
├── templates/
│   └── bill.html            # Jinja2 bill template
├── prompt_library/
│   └── prompt.py            # System prompt for LLM
```

---

## ⚡ Quick Start

1. **Clone the repo:**
   ```sh
   git clone https://github.com/sid507/AIBillGenerator.git
   cd AIBillGenerator
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   playwright install
   ```

3. **Run the backend and Streamlit app:**
   ```sh
   # Start backend (FastAPI or your preferred server)
   # Then in another terminal:
   streamlit run streamlit_app.py
   ```

4. **Try it out!**  
   Enter a prompt and see your bill generated instantly.

---

## 🤖 Tech Stack

- Python, LangChain, OpenAI/LLM
- Jinja2 (HTML templating)
- Playwright (for PNG rendering)
- Streamlit (web UI)
- FastAPI (backend)

---

## 🌟 Contributing

Pull requests and suggestions are welcome!  
Feel free to open an issue or submit a PR for new themes, features, or bug fixes.

---

## 📄 License

MIT License

---

**Connect with me on [LinkedIn](https://www.linkedin.com/in/sid507/)!**  
Happy billing! 🧾✨
