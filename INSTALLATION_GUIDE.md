# Ping Pong Game - Complete Installation Guide

## Prerequisites

You need:
- A computer (Windows, Mac, or Linux)
- Python 3.7 or higher installed
- Internet connection (for downloading dependencies)

---

## Step-by-Step Installation

### Step 1: Check if Python is Installed

Open a terminal/command prompt and check your Python version:

**On Windows:**
- Press `Win + R`, type `cmd`, press Enter
- Type: `python --version` or `python3 --version`

**On Mac:**
- Press `Cmd + Space`, type `terminal`, press Enter
- Type: `python3 --version`

**On Linux:**
- Open Terminal (Ctrl + Alt + T)
- Type: `python3 --version`

You should see something like `Python 3.x.x`. If not, install Python from [python.org](https://www.python.org/downloads/)

---

### Step 2: Get the Game Files

You have two options:

#### Option A: Clone from Git (if you have git access)

```bash
git clone <repository-url>
cd TestRepo
git checkout claude/ping-pong-game-oFKmt
```

#### Option B: Download Files Directly

If you already have the repository on your machine, navigate to it:

**On Windows:**
```cmd
cd C:\path\to\TestRepo
```

**On Mac/Linux:**
```bash
cd /path/to/TestRepo
```

---

### Step 3: Verify Game Files

Make sure you're in the correct folder and the game files exist:

**On Windows:**
```cmd
dir
```

**On Mac/Linux:**
```bash
ls
```

You should see:
- `ping_pong.py`
- `requirements.txt`
- `README.md`

---

### Step 4: Install Pygame

Still in the TestRepo folder, run:

**On Windows:**
```cmd
pip install -r requirements.txt
```

**On Mac/Linux:**
```bash
pip3 install -r requirements.txt
```

Or install pygame directly:

**On Windows:**
```cmd
pip install pygame
```

**On Mac/Linux:**
```bash
pip3 install pygame
```

You should see installation progress and a success message.

---

### Step 5: Run the Game

**On Windows:**
```cmd
python ping_pong.py
```

**On Mac/Linux:**
```bash
python3 ping_pong.py
```

---

## Game Controls

Once the game window opens:

| Action | Player 1 (Left Paddle) | Player 2 (Right Paddle) |
|--------|------------------------|-------------------------|
| Move Up | W | UP Arrow |
| Move Down | S | DOWN Arrow |
| Quit Game | ESC | ESC |

---

## Troubleshooting

### Problem: "Python is not recognized"
**Solution:** Python is not installed or not in PATH. Download and install Python from [python.org](https://www.python.org/downloads/). During installation, check "Add Python to PATH".

### Problem: "pip is not recognized"
**Solution:** Try `python -m pip install pygame` instead.

### Problem: "No module named pygame"
**Solution:** Make sure pygame installed successfully. Try running the install command again.

### Problem: Game window doesn't open
**Solution:**
- Make sure you're running the command from the TestRepo folder
- Check that `ping_pong.py` exists in the current folder
- Try running: `python3 ping_pong.py` (with python3 instead of python)

### Problem: Permission errors on Mac/Linux
**Solution:** Try with `sudo pip3 install pygame` (you'll need to enter your password)

---

## Quick Reference Card

### Complete Command Sequence

**Windows:**
```cmd
cd C:\path\to\TestRepo
pip install pygame
python ping_pong.py
```

**Mac/Linux:**
```bash
cd /path/to/TestRepo
pip3 install pygame
python3 ping_pong.py
```

---

## Example: Full Installation on Different Systems

### Windows Example:
```
1. Open Command Prompt (Win + R, type "cmd")
2. cd C:\Users\YourName\Documents\TestRepo
3. pip install pygame
4. python ping_pong.py
5. Play the game!
```

### Mac Example:
```
1. Open Terminal (Cmd + Space, type "terminal")
2. cd /Users/YourName/Documents/TestRepo
3. pip3 install pygame
4. python3 ping_pong.py
5. Play the game!
```

### Linux Example:
```
1. Open Terminal (Ctrl + Alt + T)
2. cd /home/yourname/TestRepo
3. pip3 install pygame
4. python3 ping_pong.py
5. Play the game!
```

---

## Need More Help?

If you're still having issues:
1. Make sure you're in the correct folder (should contain ping_pong.py)
2. Check Python version is 3.7 or higher: `python --version`
3. Verify pygame installed: `pip show pygame`

Enjoy the game!
