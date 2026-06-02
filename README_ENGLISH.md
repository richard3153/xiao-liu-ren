# Xiao Liu Ren Divination

> 🔮 A desktop divination tool based on the traditional Chinese Xiao Liu Ren (六壬) method, featuring **transparent calculation process display** and **bilingual Chinese/English interface**.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔮 Transparent Calculation | 3-step divination process: Month Start → Day Walk → Hour Land |
| 📖 Full Interpretation | 7 dimensions: Career, Wealth, Love, Health, Lost Items, Travel, Lawsuits |
| 🕐 Real-time Shichen | Auto-detects current Chinese time period (时辰) |
| 🎨 GUI Interface | tkinter-based friendly interface |
| 🎲 Two Modes | Time-based divination + Random divination |
| ☯ Trigram Symbols | Each result paired with its trigram symbol |
| 🌐 Bilingual | Full Chinese/English UI switching (点击 "Switch to English" / 点击"切换到中文") |

---

## 📦 File Structure

```
xiao-liu-ren/
├── gui_divination_bilingual.py   ⭐ Recommended / 推荐（双语版）
├── gui_divination_transparent.py   透明推算版 / Transparent calculation
├── gui_divination_enhanced.py    增强版 / Enhanced version
├── gui_divination.py               基础版 / Basic version
├── divination.py                   Core logic (CLI) / 核心逻辑（命令行版）
├── README.md                       Documentation / 说明文档
├── .gitignore
└── 启动透明推算版.bat              Windows launcher / Windows启动脚本
```

---

## 🚀 Quick Start

### Requirements

- Python 3.6+
- tkinter (bundled with Python)

### How to Run

```bash
# Bilingual version (Recommended / 推荐)
python gui_divination_bilingual.py

# Transparent calculation version
python gui_divination_transparent.py
```

**Windows Users**: Double-click `启动透明推算版.bat` to launch.

---

## 📖 Usage

1. Enter your question, e.g.:
   - `Will this project succeed?`
   - `How is my luck recently?`
2. Click **"开始占卜 / Start Divination"** to see the 3-step process
3. Check the **"总体判断 / Overall Judgment"** tab for detailed interpretation
4. Click **"查看详解 / View Details"** for full trigram interpretation
5. Click **"Switch to English / 切换到中文"** to toggle language

---

## 🔮 Divination Principle

### Six Spirits Quick Reference

| Spirit | Element | Trigram | Meaning | Numbers |
|--------|----------|---------|---------|---------|
| 大安 Da An | Wood 木 | ☳ | Stable, Auspicious | 1,5,7 |
| 留连 Liu Lian | Earth 土 | ☷ | Delay, Entanglement | 2,8,10 |
| 速喜 Su Xi | Fire 火 | ☲ | Joy, Speed | 3,6,9 |
| 赤口 Chi Kou | Metal 金 | ☱ | Conflict, Danger | 4,7,10 |
| 小吉 Xiao Ji | Water 水 | ☵ | Harmony, Smooth | 1,5,7 |
| 空亡 Kong Wang | Earth 土 | ☶ | Empty, Failure | 3,6,9 |

### Calculation Steps

**Step 1 — Month Start**
```
Month 1 → Da An     Month 2 → Liu Lian     Month 3 → Su Xi
Month 4 → Chi Kou   Month 5 → Xiao Ji      Month 6 → Kong Wang  (then cycles)
```

**Step 2 — Day Walk**
> From month position, walk (day - 1) steps forward

**Step 3 — Hour Land**
> From day position, add the hour's corresponding spirit position → final result

---

## 🛠️ Development

```bash
git clone https://github.com/richard3153/xiao-liu-ren.git
cd xiao-liu-ren
python gui_divination_bilingual.py
```

### Core Classes

| Class | Description |
|-------|-------------|
| `XiaoLiuRen` | Divination logic / 占卜逻辑类 |
| `DivinationGUI` | GUI interface / 图形界面类 |

---

## 🤝 Contributing

Contributions welcome!

- Lunar calendar integration / 农历转换集成
- More interpretation dimensions / 更多解读维度
- UI/UX improvements / 界面改进
- Package as standalone EXE / 打包为EXE

---

## 📄 License

[MIT License](LICENSE)

---

## 🙏 Acknowledgments

- Traditional Xiao Liu Ren inheritors / 传统小六壬法传承人
- [Xiao Liu Ren - Baidu Baike](https://baike.baidu.com/item/小六壬)

---

> ⚠️ **Disclaimer**: This program is for entertainment and cultural research only. Not for real-world decision making.  
> 声明：本程序仅供娱乐和文化研究使用，不构成任何现实决策建议。
