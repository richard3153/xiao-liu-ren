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

---

## 📦 文件说明 / File Structure

```
xiao-liu-ren/
├── gui_divination_transparent.py   ⭐ Recommended / 推荐
├── gui_divination_enhanced.py     Enhanced GUI / 增强版GUI
├── gui_divination.py               Basic GUI / 基础版GUI
├── divination.py                   Core logic (CLI) / 核心逻辑（命令行版）
├── README.md                       Documentation / 说明文档
├── .gitignore
└── 启动透明推算版.bat              Windows launcher / Windows启动脚本
```

---

## 🚀 快速开始 / Quick Start

### 环境要求 / Requirements

- Python 3.6+
- tkinter (bundled with Python / Python 自带)

### 启动方式 / How to Run

```bash
# 透明推算版（推荐 / Recommended）
python gui_divination_transparent.py

# 增强版 / Enhanced version
python gui_divination_enhanced.py
```

**Windows 用户 / Windows Users**：双击 `启动透明推算版.bat` 即可 / Double-click to launch.

---

## 📖 使用说明 / Usage

### 中文

1. 输入要占卜的问题，例如：
   - `近期运势如何？`
   - `这个项目能成功吗？`
2. 点击**「开始占卜」**，查看三步推算过程：
   ```
   【第一步：月起始】农历6月 → 【空亡】
   【第二步：日走位】从【空亡】走2步 → 【大安】
   【第三步：时落位】从【大安】加【空亡】→ 【空亡】
   ```
3. 在**「总体判断」**标签页查看详细解读
4. 点击**「查看详解」**查看完整卦象解读

### English

1. Enter your question, e.g.:
   - `How is my luck recently?`
   - `Will this project succeed?`
2. Click **"开始占卜 / Start Divination"** to see the 3-step process:
   ```
   [Step 1: Month Start] Month 6 → [Kong Wang]
   [Step 2: Day Walk] From [Kong Wang], walk 2 steps → [Da An]
   [Step 3: Hour Land] From [Da An] + [Kong Wang] → [Kong Wang]
   ```
3. Check the **"总体判断 / Overall Judgment"** tab for detailed interpretation
4. Click **"查看详解 / View Details"** for full trigram interpretation

---

## 🔮 小六壬占卜原理 / Divination Principle

### 六神速查 / Six Spirits Quick Reference

| 六神 Spirit | 五行 Element | 卦象 Trigram | 含义 Meaning | 数字 Numbers |
|-------------|--------------|--------------|--------------|--------------|
| 大安 Da An | 木 Wood | ☳ | 安稳、吉祥 Stable, Auspicious | 1,5,7 |
| 留连 Liu Lian | 土 Earth | ☷ | 拖延、纠缠 Delay, Entanglement | 2,8,10 |
| 速喜 Su Xi | 火 Fire | ☲ | 喜庆、快速 Joy, Speed | 3,6,9 |
| 赤口 Chi Kou | 金 Metal | ☱ | 口舌、凶险 Conflict, Danger | 4,7,10 |
| 小吉 Xiao Ji | 水 Water | ☵ | 和合、顺利 Harmony, Smooth | 1,5,7 |
| 空亡 Kong Wang | 土 Earth | ☶ | 虚空、失败 Void, Failure | 3,6,9 |

### 推算步骤 / Calculation Steps

**Step 1 — 月起始 / Month Start**
```
正月→大安   二月→留连   三月→速喜
四月→赤口   五月→小吉   六月→空亡  (循环 / cycle)
```

**Step 2 — 日走位 / Day Walk**
> From month position, walk (day - 1) steps forward

**Step 3 — 时落位 / Hour Land**
> From day position, add the hour's corresponding spirit position → final result

---

## 🛠️ 开发说明 / Development

```bash
git clone https://github.com/richard3153/xiao-liu-ren.git
cd xiao-liu-ren
python gui_divination_transparent.py
```

### 核心类 / Core Classes

| Class | Description |
|-------|-------------|
| `XiaoLiuRen` | Divination logic / 占卜逻辑类 |
| `DivinationGUI` | GUI interface / 图形界面类 |

---

## 🤝 贡献 / Contributing

Contributions welcome! / 欢迎贡献！

- 农历转换集成 / Lunar calendar integration
- 更多解读维度 / More interpretation dimensions
- UI/UX 改进 / UI/UX improvements
- 打包为 EXE / Package as standalone EXE

---

## 📄 许可证 / License

[MIT License](LICENSE)

---

## 🙏 致谢 / Acknowledgments

- 传统小六壬法传承人 / Traditional Xiao Liu Ren inheritors
- [小六壬 - 百度百科](https://baike.baidu.com/item/小六壬)

---

> ⚠️ **声明 / Disclaimer**：本程序仅供娱乐和文化研究使用，不构成任何现实决策建议。  
> This program is for entertainment and cultural research only. Not for real-world decision making.
