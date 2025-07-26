# 🧃 Emoji Tray — A Clean Emoji Picker for Linux (PySide6)

This is a simple emoji tray app built using PySide6. It pops up at a corner, lets you click an emoji, and inserts it into most applications using simulated keypresses.

---

## 🚀 Features

- 📌 Always-on-top emoji popup
- 🖱️ Mouse-based selection (no need to type or tab through)
- 💻 Works across most apps by simulating keypresses
- 🧠 Clean and modern PySide6 interface
- 🪄 Configurable keyboard shortcut (e.g., `Super + .`)

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/emoji-tray.git
cd emoji-tray
```
### create and Activate your venv

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### how to launch

```bash
python3 ./src/tray/main.py
```

## Add custom shortcut

1. Search for "Keyboard Shortcuts" in your Linux Mint (or other DE).

2. Click "Add custom shortcut"

3. Name: Emoji Tray
Command:
``` bash
    /full/path/to/your/project/venv/bin/python /full/path/to/your/project/main.py
```
    Shortcut: Press your desired combo, e.g., Super + .

✅ Now you can launch the emoji tray anywhere using that shortcut.