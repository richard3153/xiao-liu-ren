# 小六壬占卜程序 / Xiao Liu Ren Divination

> 🔮 基于传统小六壬法开发的桌面占卜工具，支持**透明推算过程展示**  
> A desktop divination tool based on the traditional Xiao Liu Ren method, featuring **transparent calculation process display**.

---

## ✨ 功能特色 / Features

| 🇨🇳 中文 | 🇬🇧 English |
|-----------|-------------|
| 🔮 透明推算：分三步显示完整占卜过程 | 🔮 Transparent calculation: 3-step divination process display |
| 📖 完整卦象解读：涵盖七个维度 | 📖 Full interpretation: 7 dimensions covered |
| 🕐 实时时辰：自动获取当前时辰 | 🕐 Real-time Shichen: auto-detect current time period |
| 🎨 图形界面：基于 tkinter 的友好 GUI | 🎨 GUI: tkinter-based friendly interface |
| 🎲 两种占卜模式：时间占卜 + 随机占卜 | 🎲 Two modes: Time-based + Random divination |
| ☯ 卦象符号：每个结果配有对应符号 | ☯ Trigram symbols: each result with its symbol |
| 🌐 双语界面：中英文一键切换 | 🌐 Bilingual UI: one-click Chinese/English switch |

---

## 📁 文件说明 / File Structure

```
xiao-liu-ren/
├── gui_divination_bilingual.py   ⭐ 推荐 / Recommended
├── gui_divination_transparent.py     透明推算版 / Transparent calculation
├── gui_divination_enhanced.py       增强版 GUI / Enhanced GUI
├── gui_divination.py                 基础版 GUI / Basic GUI
├── divination.py                     核心逻辑（命令行版）/ Core logic (CLI)
├── README.md                         说明文档（中英混排）/ Bilingual docs
├── README_EN.md                      英文文档 / English documentation
└── .gitignore
```

> **推荐使用 `gui_divination_bilingual.py`**，支持中英文界面一键切换。  
> **Recommended: `gui_divination_bilingual.py`** — supports one-click Chinese/English UI switch.

---

## 🚀 快速开始 / Quick Start

### 环境要求 / Requirements
- Python 3.8+（tkinter 已内置）/ Python 3.8+ (tkinter included)

### 运行 / Run

**Windows（双击）：**
```bat
启动占卜程序.bat
```

**手动运行 / Manual：**
```bash
python gui_divination_bilingual.py
```

---

## 📖 使用说明 / How to Use

1. 在输入框输入你的问题（中文或英文均可）  
   Enter your question in the input box (Chinese or English)
2. 点击 **「开始占卜」**，或点击 **「随机占卜」** 进行随机占卜  
   Click **「Start Divination」**, or **「Random」** for a random divination
3. 在 **「推算过程」** 标签页查看三步推算详情  
   View the 3-step calculation process in the **Process** tab
4. 在 **「卦象解读」** 标签页查看完整解读  
   View the full interpretation in the **Judgment** tab
5. 点击 **「EN/中」** 按钮随时切换界面语言  
   Click **「EN/中」** to switch UI language anytime

---

## 🔮 占卜方法 / Divination Method

小六壬使用三步计数法：  
Xiao Liu Ren uses a 3-step counting method:

| 步骤 | 依据 | 推算方法 |
|------|------|----------|
| Step 1 | 农历月份 | 从**寅**位开始数 |
| Step 2 | 农历日期 | 从 Step 1 结果继续数 |
| Step 3 | 时辰（小时） | 从 Step 2 结果继续数 |

**六神对照表 / The Six Spirits：**

| 六神 | 卦象 | 五行 | 含义（中文） | Meaning (EN) |
|------|------|------|-------------|---------------|
| 大安 Da An | ☳ | 木 Wood | 安稳、吉祥、静止 | Stable, auspicious, stillness |
| 留连 Liu Lian | ☴ | 木 Wood | 犹豫、阻碍、拖延 | Delay, obstacle, waiting |
| 速喜 Su Xi | ☲ | 火 Fire | 快速、喜庆、好消息 | Quick joy, good news coming |
| 赤口 Chi Kou | ☵ | 金 Metal | 口舌、冲突、是非 | Conflict, mouth trouble |
| 小吉 Xiao Ji | ☶ | 土 Earth | 小吉、顺利、小成 | Small luck, partial success |
| 空亡 Kong Wang | ☱ | 金 Metal | 落空、丢失、虚幻 | Emptiness, loss, void |

---

## 📖 解读维度 / Interpretation Dimensions

每个结果包含七个维度的完整解读：  
Each result includes full interpretation across 7 dimensions:

- **事业学业** / Career & Academics
- **财运财富** / Wealth & Finance
- **感情婚姻** / Love & Relationships
- **健康身体** / Health & Wellness
- **失物寻找** / Lost Items
- **出行搬家** / Travel & Movement
- **官非诉讼** / Lawsuits & Disputes

---

## 📝 示例 / Example

```
============================================================
Question / 问题: 明天面试能顺利通过吗？
Divination Time: 2026-06-02 14:30:00
Lunar: 6月2日 未时 (13-15)
============================================================

[Step 1] 月起始 / Month Start
----------------------------------------
Month 6 -> [大安 / Da An]

[Step 2] 日走位 / Day Walk
----------------------------------------
From [大安 / Da An] walk 2 steps:
  起点:大安(位置1) / Start: Da An (pos 1)
  第1步:大安 → 留连 / Step 1: Da An -> Liu Lian

[Step 3] 时落位 / Hour Land
----------------------------------------
  日期位置:留连(位置2) / Day position: Liu Lian (pos 2)
  时辰对应:14 -> 速喜(位置3) / Hour corresponds to: 14 -> Su Xi (pos 3)
  推算:留连(2) + 速喜(3) → 小吉(5) / Calculate: Liu Lian (2) + Su Xi (3) -> Xiao Ji (5)

============================================================
Final Result / 最终结果: 小吉 Xiao Ji ☶
Element / 五行: 土 / Earth
Meaning / 含义: 小吉、顺利、小成 / Small luck, partial success

此卦象显示事情有小成，需要踏实努力。
Seek wealth in the NE; lost items are nearby.
============================================================
```

---

## 📜 传统渊源 / Traditional Origins

小六壬是中国传统术数**六壬**体系的简化版本，与**奇门遁甲**、**太乙**并称为"三式"。  
Xiao Liu Ren is a simplified version of the traditional Chinese **Liu Ren (六壬)** system, one of the **Three Styles (三式)** of Chinese metaphysical arts, along with Qi Men Dun Jia and Tai Yi.

它通过农历月、日、时辰三个参数，以简单计数方式得出六神位置，每个位置对应特定的吉凶含义。  
It uses three parameters (lunar month, day, and Shichen) to arrive at one of six spirit positions through simple counting, each with specific auspicious/malicious meanings.

---

## 🛠️ 故障排除 / Troubleshooting

**双击脚本没反应 / Double-click script does nothing：**
- 检查 Python 安装：`python --version`
- 检查 tkinter：`python -c "import tkinter; print('OK')`
- 尝试直接运行：`python gui_divination_bilingual.py`

**切换语言后显示还是中文 / Still shows Chinese after switching language：**
- 已修复，请更新到最新版本 / Fixed in latest version, please update

---

## 📄 许可证 / License

MIT License — 自由使用、修改和分发。  
MIT License — free to use, modify, and distribute.

---

## 🙏 致谢 / Acknowledgments

基于传统小六壬占卜方法开发。  
Based on traditional Xiao Liu Ren divination method.

开发者 / Developed by **richard3153**  
GitHub: [richard3153/xiao-liu-ren](https://github.com/richard3153/xiao-liu-ren)
