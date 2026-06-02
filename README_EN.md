# Xiao Liu Ren Divination

> A desktop divination tool based on the traditional Chinese Xiao Liu Ren (六壬) method, featuring **transparent step-by-step calculation display**.

---

## ✨ Features

- 🔮 **Transparent Calculation** — Shows all 3 steps (Month → Day → Hour) with full process
- 📖 **Full Interpretation** — 7 dimensions: career, wealth, love, health, lost items, travel, legal
- 🕐 **Real-time Shichen** — Auto-detects current Chinese time period (12 Shichen)
- 🎨 **GUI Interface** — Clean tkinter-based desktop GUI
- 🎲 **Two Divination Modes** — Time-based (uses current time) + Random
- ☯ **Trigram Symbols** — Each result with its corresponding trigram symbol
- 🌐 **Bilingual** — Full Chinese / English UI, switch anytime

---

## 📁 File Structure

```
xiao-liu-ren/
├── gui_divination_bilingual.py   ⭐ Recommended / 推荐
├── gui_divination_transparent.py     Enhanced with step display
├── gui_divination_enhanced.py       Enhanced GUI
├── gui_divination.py                 Basic GUI
├── divination.py                     Core logic (CLI)
├── README.md                        Bilingual documentation
├── README_EN.md                     English documentation
└── .gitignore
```

---

## 🚀 Quick Start

### Requirements
- Python 3.8+ (tkinter included)

### Run

**Windows:**
```bat
启动占卜程序.bat
```

**Manual:**
```bash
python gui_divination_bilingual.py
```

---

## 📖 How to Use

1. Enter your question in the input box (Chinese or English)
2. Click **「开始占卜」** or **「Random」** for a random divination
3. View the 3-step calculation process in the **Process** tab
4. View the full interpretation in the **Judgment** tab
5. Click **「EN/中」** to switch language anytime

---

## 🔮 Divination Method

Xiao Liu Ren uses a 3-step counting method:

| Step | Basis | Calculation |
|------|-------|-------------|
| Step 1 | Lunar Month | Count from **Yin** position |
| Step 2 | Lunar Day | Walk from Step 1 result |
| Step 3 | Hour (Shichen) | Walk from Step 2 result |

**The Six Spirits (六神):**

| Spirit | Trigram | Element | Meaning |
|--------|---------|---------|---------|
| Da An (大安) | ☳ | Wood | Stable, auspicious, stillness |
| Liu Lian (留连) | ☴ | Wood | Delay, obstacle, waiting |
| Su Xi (速喜) | ☲ | Fire | Quick joy, good news coming |
| Chi Kou (赤口) | ☵ | Metal | Conflict, mouth trouble |
| Xiao Ji (小吉) | ☶ | Earth | Small luck, partial success |
| Kong Wang (空亡) | ☱ | Metal | Emptiness, loss, void |

---

## 📖 Interpretation Dimensions

Each result includes:
- **Trigram & Element** — Element, direction, color, number
- **Meaning** — Core interpretation
- **Advice** — Practical guidance
- **Detail** — Full explanation covering:
  - Career & Academics
  - Wealth & Finance
  - Love & Relationships
  - Health & Wellness
  - Lost Items
  - Travel & Movement
  - Lawsuits & Disputes

---

## 📝 Examples

```
============================================================
Question: Will I get a promotion?
Divination Time: 2026-06-02 14:30:00
Lunar: 6月2日 未时 (13-15)
============================================================

[Step 1] Month Start
----------------------------------------
Month 6 -> [Da An]

[Step 2] Day Walk
----------------------------------------
From [Da An] walk 2 steps:
  Start: Da An (pos 1)
  Step 1: Da An -> Liu Lian

[Step 3] Hour Land
----------------------------------------
  Day position: Liu Lian (pos 2)
  Hour corresponds to: 14 -> Su Xi (pos 3)
  Calculate: Liu Lian (2) + Su Xi (3) -> Xiao Ji (5)

============================================================
Final Result: Xiao Ji (小吉) ☶
Element: Earth
Meaning: Small luck, partial success

This hexagram indicates moderate success.
Seek wealth in the NE; lost items are nearby.
============================================================
```

---

## 📜 Traditional Origins

Xiao Liu Ren (小六壬) is a traditional Chinese divination method from the **Liu Ren (六壬)** system, one of the Three Styles (三式) of Chinese metaphysical arts, along with Qi Men Dun Jia and Tai Yi. It uses a simple counting method based on the lunar calendar month, day, and Chinese time period (Shichen) to arrive at one of six spirit positions, each with a specific interpretation.

---

## 🛠️ Troubleshooting

**GUI doesn't appear:**
- Check Python installation: `python --version`
- Check tkinter: `python -c "import tkinter; print('OK')"`
- Try: `python gui_divination_transparent.py`

**Language switch shows old results:**
- This was a known bug, fixed in the latest version. Pull the latest code.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgments

Based on traditional Xiao Liu Ren (小六壬) divination method.  
Developed by **richard3153** — GitHub: [richard3153/xiao-liu-ren](https://github.com/richard3153/xiao-liu-ren)
