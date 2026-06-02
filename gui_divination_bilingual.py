# -*- coding: utf-8 -*-
"""
小六壬占卜程序 - 双语透明推算版
Xiao Liu Ren Divination - Bilingual Transparent Version
支持中文/英文界面切换 | Supports Chinese/English UI switching
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import random
import sys
import os

# ============================================================
# 双语文本字典 | Bilingual Text Dictionary
# ============================================================
TEXTS = {
    "zh": {
        "title": "🔮 小六壬占卜程序",
        "subtitle": "— 月起始 → 日走位 → 时落位 —",
        "input_hint": "占卜输入 / Divination Input",
        "input_label": "请输入要占卜的事情：",
        "time_prefix": "当前时间：",
        "shichen_prefix": "时辰：",
        "btn_divine": "开始占卜",
        "btn_random": "随机占卜",
        "btn_detail": "查看详解",
        "btn_clear": "清空结果",
        "btn_lang": "Switch to English",
        "tab_process": "推算过程",
        "tab_judgment": "总体判断",
        "warn_no_question": "请输入要占卜的事情！\nPlease enter a question!",
        "warn_no_result": "请先进行占卜\nPlease divine first",
        "detail_title": "{0} - 详细解读",
        "footer": "声明：本程序仅供参考娱乐，不构成任何建议 | For entertainment only",
    },
    "en": {
        "title": "🔮 Xiao Liu Ren Divination",
        "subtitle": "— Month Start → Day Walk → Hour Land —",
        "input_hint": "Divination Input / 占卜输入",
        "input_label": "Enter your question:",
        "time_prefix": "Time: ",
        "shichen_prefix": "Shichen: ",
        "btn_divine": "Start Divination",
        "btn_random": "Random Divination",
        "btn_detail": "View Details",
        "btn_clear": "Clear Result",
        "btn_lang": "切换到中文",
        "tab_process": "Calculation Process",
        "tab_judgment": "Overall Judgment",
        "warn_no_question": "Please enter a question!\n请输入要占卜的事情！",
        "warn_no_result": "Please divine first\n请先进行占卜",
        "detail_title": "{0} - Detailed Interpretation",
        "footer": "Disclaimer: For entertainment only | 仅供参考娱乐",
    }
}

# ============================================================
# 六神中英文数据 | Six Spirits Bilingual Data
# ============================================================
SPIRITS = {
    "大安": {
        "en": "Da An", "trigram": "☳",
        "wuxing_zh": "木 (Wood)", "wuxing_en": "Wood",
        "meaning_zh": "安稳、吉祥、静止、守成",
        "meaning_en": "Stable, Auspicious, Still, Maintain",
        "advice_zh": "此卦象显示事情平稳安定，适合守成等待。\n求财可往西南方，失物不远可自行找回。",
        "advice_en": "This hexagram indicates stability. Suitable for maintaining status quo.\nSeek wealth in the SW; lost items are nearby.",
        "detail_zh": "大安事事昌，求财在坤方，失物去不远，宅舍保安康",
        "detail_en": "Da An: All matters prosper; wealth in SW; lost items nearby; home safe.",
        "aspect_zh": {
            "career": "事业：平稳发展，适合守成，不宜冒进",
            "wealth": "财运：求财在坤方（西南方），正财稳定",
            "love":   "感情：感情稳定，适合维系现有关系",
            "health": "健康：身体安康，无大碍",
            "lost":  "失物：失物不远，多在家中或常去之处",
            "travel": "出行：出行平安，无阻碍",
            "lawsuit":"官非：官事平缓，无大碍",
        },
        "aspect_en": {
            "career": "Career: Steady development, good for maintaining",
            "wealth": "Wealth: Seek wealth in SW direction, stable income",
            "love":  "Love: Relationship stable, good for maintaining bond",
            "health": "Health: Good health, no major issues",
            "lost":  "Lost: Items are nearby, likely at home",
            "travel": "Travel: Safe travel, no obstacles",
            "lawsuit":"Lawsuit: Legal matters mild, no major issues",
        }
    },
    "留连": {
        "en": "Liu Lian", "trigram": "☷",
        "wuxing_zh": "土 (Earth)", "wuxing_en": "Earth",
        "meaning_zh": "纠缠、拖延、犹豫、反复",
        "meaning_en": "Entangled, Delayed, Hesitant, Repeated",
        "advice_zh": "此卦象显示事情有拖延，需要耐心等待。\n不宜急于求成，官事应缓处理。",
        "advice_en": "This hexagram indicates delay. Patience is needed.\nLegal matters should be handled slowly.",
        "detail_zh": "留连事难成，求谋日未明，官事只宜缓，去者未回程",
        "detail_en": "Liu Lian: Matters hard to complete; plans unclear; legal matters wait.",
        "aspect_zh": {
            "career": "事业：事情拖延，难以速成，需耐心等待",
            "wealth": "财运：求财不成，财运平平，不宜投资",
            "love":  "感情：感情纠缠，有阻碍，需时间化解",
            "health": "健康：病者拖延，恢复缓慢",
            "lost":  "失物：失物难寻，多在暗处或被人误拿",
            "travel": "出行：出行有阻，不宜远行",
            "lawsuit":"官非：官事拖延，宜缓不宜急",
        },
        "aspect_en": {
            "career": "Career: Matters delayed, hard to complete quickly",
            "wealth": "Wealth: Wealth blocked, average luck, not good for investing",
            "love":  "Love: Relationship entangled, obstacles need time",
            "health": "Health: Illness lingers, slow recovery",
            "lost":  "Lost: Items hard to find, likely hidden",
            "travel": "Travel: Travel obstructed, not good for long trips",
            "lawsuit":"Lawsuit: Legal matters delayed, slow is better",
        }
    },
    "速喜": {
        "en": "Su Xi", "trigram": "☲",
        "wuxing_zh": "火 (Fire)", "wuxing_en": "Fire",
        "meaning_zh": "喜庆、快速、成功、光明",
        "meaning_en": "Joyful, Fast, Successful, Bright",
        "advice_zh": "此卦象显示喜事临近，事情会快速解决。\n求财可往南方，失物可在午时找到。",
        "advice_en": "This hexagram indicates good news is coming, matters resolve quickly.\nSeek wealth in the South; lost items found at noon.",
        "detail_zh": "速喜喜来临，求财向南行，失物申未午，逢人路上寻",
        "detail_en": "Su Xi: Joy is coming; seek wealth in the South; ask people on the road.",
        "aspect_zh": {
            "career": "事业：喜事临近，事业快速成功，有贵人相助",
            "wealth": "财运：求财向南行（南方），财运亨通",
            "love":  "感情：感情喜庆，有喜讯传来",
            "health": "健康：病者快速康复，身体健康",
            "lost":  "失物：失物在南方，午时（11-13点）可寻回",
            "travel": "出行：出行顺利，有喜事",
            "lawsuit":"官非：官事快速解决，有贵人相助",
        },
        "aspect_en": {
            "career": "Career: Good news coming, career success fast, help available",
            "wealth": "Wealth: Seek wealth in the South, wealth luck is excellent",
            "love":  "Love: Relationship joyful, good news coming",
            "health": "Health: Illness recovers quickly, body is healthy",
            "lost":  "Lost: Items in the South, found around 11-13:00",
            "travel": "Travel: Smooth travel, good news along the way",
            "lawsuit":"Lawsuit: Legal matters resolve quickly, help available",
        }
    },
    "赤口": {
        "en": "Chi Kou", "trigram": "☱",
        "wuxing_zh": "金 (Metal)", "wuxing_en": "Metal",
        "meaning_zh": "口舌、凶险、争执、疾病",
        "meaning_en": "Conflict, Danger, Dispute, Illness",
        "advice_zh": "此卦象显示有口舌是非，需防官非疾病。\n失物应尽快寻找，出行小心谨慎。",
        "advice_en": "This hexagram indicates conflict and danger. Beware of lawsuits and illness.\nLost items should be sought quickly; travel with caution.",
        "detail_zh": "赤口主口伤，官事且紧防，失物急去寻，行人有惊慌",
        "detail_en": "Chi Kou: Mainly conflict; beware of lawsuits; seek lost items urgently.",
        "aspect_zh": {
            "career": "事业：有口舌是非，需防小人，不宜妄动",
            "wealth": "财运：求财无利，且有破财之虞",
            "love":  "感情：感情有口舌，争执多，需忍让",
            "health": "健康：病者有险，需防病情加重",
            "lost":  "失物：失物在西方，需急寻，否则难找回",
            "travel": "出行：出行有险，需小心谨慎",
            "lawsuit":"官非：官事凶险，需紧防，宜和解",
        },
        "aspect_en": {
            "career": "Career: Have conflict disputes, beware of villains",
            "wealth": "Wealth: Wealth seeking unfavorable, risk of losing money",
            "love":  "Love: Relationship has conflicts, need tolerance",
            "health": "Health: Illness has dangers, prevent worsening",
            "lost":  "Lost: Items in the West, urgently or hard to recover",
            "travel": "Travel: Travel has dangers, be very careful",
            "lawsuit":"Lawsuit: Legal matters dangerous, caution needed",
        }
    },
    "小吉": {
        "en": "Xiao Ji", "trigram": "☵",
        "wuxing_zh": "水 (Water)", "wuxing_en": "Water",
        "meaning_zh": "和合、顺利、喜悦、婚姻",
        "meaning_en": "Harmony, Smooth, Joy, Marriage",
        "advice_zh": "此卦象显示和合顺利，有喜事临门。\n婚姻和合，求财有利，失物在西南方。",
        "advice_en": "This hexagram indicates harmony and smoothness, good fortune arrives.\nMarriage is harmonious, wealth seeking is favorable.",
        "detail_zh": "小吉最吉昌，路上好商量，阴人来报喜，失物在坤方",
        "detail_en": "Xiao Ji: Most auspicious; good for negotiation; someone brings good news.",
        "aspect_zh": {
            "career": "事业：和合顺利，有人相助，事业吉昌",
            "wealth": "财运：求财有利，财运亨通，多有意外之财",
            "love":  "感情：婚姻和合，感情顺利，有喜事",
            "health": "健康：身体康健，病者易愈",
            "lost":  "失物：失物在坤方（西南方），可寻回",
            "travel": "出行：出行顺利，得顺风，有贵人相助",
            "lawsuit":"官非：官事和解，无大碍",
        },
        "aspect_en": {
            "career": "Career: Harmonious and smooth, someone helps, career auspicious",
            "wealth": "Wealth: Wealth seeking favorable, luck good, unexpected wealth",
            "love":  "Love: Marriage harmonious, relationship smooth, good news",
            "health": "Health: Body healthy, illness recovers easily",
            "lost":  "Lost: Items in the SW, can be recovered",
            "travel": "Travel: Smooth travel, favorable winds, help available",
            "lawsuit":"Lawsuit: Legal matters settle peacefully",
        }
    },
    "空亡": {
        "en": "Kong Wang", "trigram": "☶",
        "wuxing_zh": "土 (Earth)", "wuxing_en": "Earth",
        "meaning_zh": "虚空、失败、消散、疾病",
        "meaning_en": "Empty, Failure, Dispersed, Illness",
        "advice_zh": "此卦象显示事情落空，需要重新规划。\n求财无利，出行有灾，宜守不宜进。",
        "advice_en": "This hexagram indicates matters falling through, need to replan.\nWealth seeking unfavorable, travel has disasters.",
        "detail_zh": "空亡事不祥，阴人多乖张，求财无利益，行人有灾殃",
        "detail_en": "Kong Wang: Matters inauspicious; people stubborn; wealth no benefit.",
        "aspect_zh": {
            "career": "事业：事情落空，谋划无成，需重新规划",
            "wealth": "财运：求财无利，且有破财之虞，不宜投资",
            "love":  "感情：感情空虚，有分离之象",
            "health": "健康：病者加重，需防不治之症",
            "lost":  "失物：失物难寻，多已消散或被人拿走",
            "travel": "出行：出行有灾，不宜远行",
            "lawsuit":"官非：官事凶险，有牢狱之灾",
        },
        "aspect_en": {
            "career": "Career: Matters fall through, plans fail, need replanning",
            "wealth": "Wealth: Wealth seeking no benefit, risk of losing money",
            "love":  "Love: Relationship feels empty, signs of separation",
            "health": "Health: Illness worsens, prevent incurable disease",
            "lost":  "Lost: Items hard to find, mostly dispersed or taken",
            "travel": "Travel: Travel has disasters, not good for long trips",
            "lawsuit":"Lawsuit: Legal matters dangerous, risk of imprisonment",
        }
    },
}


# ============================================================
# 占卜核心逻辑类 | Divination Core Logic Class
# ============================================================
class XiaoLiuRen:
    """小六壬占卜类 | Xiao Liu Ren Divination Class"""

    def __init__(self):
        self.positions = list(SPIRITS.keys())
        self.month_map = {1:"大安", 2:"留连", 3:"速喜",
                         4:"赤口", 5:"小吉", 6:"空亡"}

    def get_month_position(self, month):
        """月起始 | Month Start"""
        key = (month - 1) % 6 + 1
        pos = self.month_map[key]
        return {"step": "月起始", "month": month, "position": pos}

    def get_day_position(self, start_pos, day):
        """日走位 | Day Walk"""
        start_index = self.positions.index(start_pos)
        current_index = start_index
        process = [f"起点：{start_pos}（位置{start_index+1}）"]
        for i in range(day - 1):
            old_index = current_index
            current_index = (current_index + 1) % 6
            process.append(
                f"第{i+1}步：{self.positions[old_index]} → {self.positions[current_index]}"
            )
        return {
            "step": "日走位",
            "start_position": start_pos,
            "day": day,
            "result_position": self.positions[current_index],
            "process": process,
        }

    def get_hour_shichen(self, hour):
        """获取时辰名称和对应六神 | Get shichen name and corresponding spirit"""
        # 时辰对照表 | Shichen lookup table
        shichen_list_zh = [
            "子时", "丑时", "寅时", "卯时", "辰时", "巳时",
            "午时", "未时", "申时", "酉时", "戌时", "亥时"
        ]
        shichen_list_en = [
            "Zi (23-1)", "Chou (1-3)", "Yin (3-5)", "Mao (5-7)",
            "Chen (7-9)", "Si (9-11)", "Wu (11-13)", "Wei (13-15)",
            "Shen (15-17)", "You (17-19)", "Xu (19-21)", "Hai (21-23)"
        ]
        # 时辰对应六神（12时辰 → 6神循环2圈）
        # 子→大安，丑→留连，寅→速喜，卯→赤口，辰→小吉，巳→空亡
        # 午→大安，未→留连，申→速喜，酉→赤口，戌→小吉，亥→空亡
        hour_to_spirit = [
            "大安", "留连", "速喜", "赤口", "小吉", "空亡",
            "大安", "留连", "速喜", "赤口", "小吉", "空亡"
        ]
        idx = min(hour // 2, 11) if hour < 23 else 0
        shichen_zh = shichen_list_zh[idx]
        shichen_en = shichen_list_en[idx]
        spirit = hour_to_spirit[idx]
        return shichen_zh, shichen_en, spirit

    def get_hour_position(self, day_pos, hour):
        """时落位 | Hour Land"""
        _, _, hour_spirit = self.get_hour_shichen(hour)
        day_index = self.positions.index(day_pos)
        hour_index = self.positions.index(hour_spirit)
        final_index = (day_index + hour_index) % 6

        process = [
            f"日期位置：{day_pos}（位置{day_index+1}）",
            f"时辰对应：{hour}时 → {hour_spirit}（位置{hour_index+1}）",
            f"推算：{day_pos}（{day_index+1}）+ {hour_spirit}（{hour_index+1}）→ {self.positions[final_index]}（{final_index+1}）"
        ]

        shichen_zh, shichen_en, _ = self.get_hour_shichen(hour)

        return {
            "step": "时落位",
            "day_position": day_pos,
            "hour": hour,
            "hour_position": hour_spirit,
            "final_position": self.positions[final_index],
            "process": process,
            "shichen_zh": shichen_zh,
            "shichen_en": shichen_en,
        }

    def divine_with_steps(self, question, lang="zh", month=None, day=None, hour=None):
        """完整分步占卜 | Full step-by-step divination"""
        now = datetime.now()
        month = month if month is not None else now.month
        day = day if day is not None else now.day
        hour = hour if hour is not None else now.hour

        step1 = self.get_month_position(month)
        step2 = self.get_day_position(step1["position"], day)
        step3 = self.get_hour_position(step2["result_position"], hour)

        shichen_zh, shichen_en, _ = self.get_hour_shichen(hour)

        return {
            "question": question,
            "lang": lang,
            "divination_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "lunar_month": month,
            "lunar_day": day,
            "hour": hour,
            "shichen_zh": shichen_zh,
            "shichen_en": shichen_en,
            "steps": {"step1": step1, "step2": step2, "step3": step3},
            "final_result": step3["final_position"],
            "result_info": SPIRITS[step3["final_position"]],
        }

    def random_divine(self, question, lang="zh"):
        """随机占卜 | Random divination"""
        result = random.choice(self.positions)
        return {
            "question": question,
            "lang": lang,
            "divination_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "method": "random",
            "final_result": result,
            "result_info": SPIRITS[result],
        }

# ============================================================
# GUI 界面类 | GUI Interface Class
# ============================================================

class DivinationGUI:
    """双语GUI界面 | Bilingual GUI Interface"""

    ASPECT_KEYS = ['career', 'wealth', 'love', 'health', 'lost', 'travel', 'lawsuit']

    def __init__(self, root):
        self.root = root
        self.lang = 'zh'
        self.diviner = XiaoLiuRen()
        self.current_result = None
        self.setup_ui()
        self.update_time()

    def t(self, key):
        return TEXTS[self.lang][key]

    def setup_ui(self):
        self.root.title(self.t('title'))
        self.root.geometry('1050x950')
        self.root.configure(bg='#f0f0f0')

        # Title
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=20)
        self.title_label = tk.Label(title_frame, font=('Microsoft YaHei', 22, 'bold'),
                                    bg='#f0f0f0', fg='#2c3e50')
        self.title_label.pack()
        self.subtitle_label = tk.Label(title_frame, font=('Microsoft YaHei', 11),
                                        bg='#f0f0f0', fg='#7f8c8d')
        self.subtitle_label.pack(pady=(5, 0))

        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=40, pady=20, fill='both', expand=True)

        # Input frame
        self.input_frame = ttk.LabelFrame(main_frame, padding=20)
        self.input_frame.pack(fill='x', pady=(0, 20))

        self.input_label = ttk.Label(self.input_frame, font=('Microsoft YaHei', 10))
        self.input_label.pack(anchor='w')

        self.question_entry = ttk.Entry(self.input_frame, font=('Microsoft YaHei', 11), width=60)
        self.question_entry.pack(fill='x', pady=(5, 15))

        # Time display
        time_frame = ttk.Frame(self.input_frame)
        time_frame.pack(fill='x', pady=(0, 15))
        self.time_label = ttk.Label(time_frame, font=('Microsoft YaHei', 10, 'bold'), foreground='#2980b9')
        self.time_label.pack(side='left')
        self.shichen_label = ttk.Label(time_frame, font=('Microsoft YaHei', 10), foreground='#8e44ad')
        self.shichen_label.pack(side='left', padx=(20, 0))

        # Buttons
        btn_frame = ttk.Frame(self.input_frame)
        btn_frame.pack(fill='x')
        self.divine_btn = ttk.Button(btn_frame, command=self.perform_divination)
        self.divine_btn.pack(side='left', padx=(0, 10))
        self.random_btn = ttk.Button(btn_frame, command=self.random_divination)
        self.random_btn.pack(side='left', padx=(0, 10))
        self.detail_btn = ttk.Button(btn_frame, command=self.show_detail)
        self.detail_btn.pack(side='left', padx=(0, 10))
        self.clear_btn = ttk.Button(btn_frame, command=self.clear_result)
        self.clear_btn.pack(side='left', padx=(0, 10))
        self.lang_btn = ttk.Button(btn_frame, command=self.toggle_lang)
        self.lang_btn.pack(side='right')

        # Notebook
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True)

        self.process_text = self._make_tab(self.notebook, ('Consolas', 10), '#ffffff')
        self.judgment_text = self._make_tab(self.notebook, ('Microsoft YaHei', 10), '#fafafa')

        # Footer
        self.footer_label = tk.Label(self.root, font=('Microsoft YaHei', 9),
                                     bg='#f0f0f0', fg='#95a5a6')
        self.footer_label.pack(pady=20)

        self.update_ui_text()

    def _make_tab(self, parent, font, bg):
        frame = ttk.Frame(parent)
        parent.add(frame, text='')
        txt = scrolledtext.ScrolledText(frame, font=font, wrap=tk.WORD, height=25, bg=bg)
        txt.pack(fill='both', expand=True, padx=10, pady=10)
        return txt

    def update_ui_text(self):
        self.root.title(self.t('title'))
        self.title_label.config(text=self.t('title'))
        self.subtitle_label.config(text=self.t('subtitle'))
        hint = '占卜输入 / Divination Input' if self.lang == 'zh' else 'Divination Input / 占卜输入'
        self.input_frame.config(text=hint)
        self.input_label.config(text=self.t('input_label'))
        self.divine_btn.config(text=self.t('btn_divine'))
        self.random_btn.config(text=self.t('btn_random'))
        self.detail_btn.config(text=self.t('btn_detail'))
        self.clear_btn.config(text=self.t('btn_clear'))
        self.lang_btn.config(text=self.t('btn_lang'))
        self.notebook.tab(0, text=self.t('tab_process'))
        self.notebook.tab(1, text=self.t('tab_judgment'))
        self.footer_label.config(text=self.t('footer'))
        if self.current_result:
            self._display_result(self.current_result)

    def toggle_lang(self):
        self.lang = 'en' if self.lang == 'zh' else 'zh'
        self.update_ui_text()

    def update_time(self):
        now = datetime.now()
        self.time_label.config(text=self.t('time_prefix') + now.strftime('%Y-%m-%d %H:%M:%S'))
        shi_zh = ['子时','丑时','寅时','卯时','辰时','巳时','午时','未时','申时','酉时','戌时','亥时']
        idx = min(now.hour // 2, 11) if now.hour < 23 else 0
        self.shichen_label.config(text=self.t('shichen_prefix') + shi_zh[idx])
        self.root.after(1000, self.update_time)

    def perform_divination(self):
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showwarning('Tip', self.t('warn_no_question'))
            return
        result = self.diviner.divine_with_steps(question, self.lang)
        self.current_result = result
        self._display_result(result)

    def random_divination(self):
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showwarning('Tip', self.t('warn_no_question'))
            return
        result = self.diviner.random_divine(question, self.lang)
        self.current_result = result
        self._display_result(result)

    def _display_result(self, r):
        self.process_text.delete(1.0, tk.END)
        self.judgment_text.delete(1.0, tk.END)
        T = self.t
        lang = r['lang']
        info = r['result_info']
        name = info['en'] if lang == 'en' else r['final_result']
        trigram = info['trigram']

        lines = []
        lines.append('=' * 60)
        lines.append(T('question') + r['question'])
        lines.append(T('divination_time') + r['divination_time'])
        lines.append('Lunar: {}月{}日  {} {}'.format(r['lunar_month'], r['lunar_day'], r.get('shichen_zh',''), r.get('shichen_en','')))
        lines.append('=' * 60)
        lines.append('')

        s = r.get('steps', {})
        if s:
            lines.append(T('step1'))
            lines.append('-' * 40)
            lines.append('Month {} -> [{}]'.format(r['lunar_month'], s['step1']['position']))
            lines.append('')
            lines.append(T('step2'))
            lines.append('-' * 40)
            lines.append('From [{}] walk {} steps:'.format(s['step2']['start_position'], r['lunar_day']))
            for p in s['step2']['process']:
                lines.append('  ' + p)
            lines.append('')
            lines.append(T('step3'))
            lines.append('-' * 40)
            for p in s['step3']['process']:
                lines.append('  ' + p)
            lines.append('')

        lines.append('=' * 60)
        lines.append(T('final_result'))
        lines.append('=' * 60)
        lines.append('')
        result_label = T('result') if 'result' in TEXTS[lang] else 'Result'
        lines.append('{} [{}] {}'.format(result_label, name, trigram))
        wuxing = info['wuxing_en'] if lang == 'en' else info['wuxing_zh']
        lines.append(T('wuxing').format(wuxing))
        meaning = info['meaning_en'] if lang == 'en' else info['meaning_zh']
        lines.append(T('meaning').format(meaning))
        advice = info['advice_en'] if lang == 'en' else info['advice_zh']
        lines.append('')
        lines.append(advice)

        self.process_text.insert(1.0, '\n'.join(lines))

        jlines = []
        jlines.append(T('overall'))
        jlines.append('=' * 60)
        jlines.append('')
        aspect_key = 'aspect_en' if lang == 'en' else 'aspect_zh'
        for k in self.ASPECT_KEYS:
            val = info[aspect_key][k]
            jlines.append(val)
        self.judgment_text.insert(1.0, '\n'.join(jlines))

    def show_detail(self):
        if not self.current_result:
            messagebox.showinfo('Tip', self.t('warn_no_result'))
            return
        r = self.current_result
        info = r['result_info']
        title = info['en'] + ' - Detailed Interpretation' if r['lang'] == 'en' else r['final_result'] + ' - 详细解读'
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry('750x650')
        txt = scrolledtext.ScrolledText(win, font=('Microsoft YaHei', 10), wrap=tk.WORD, bg='#fafafa')
        txt.pack(fill='both', expand=True, padx=20, pady=20)
        advice = info['advice_en'] if r['lang'] == 'en' else info['advice_zh']
        detail = info['detail_en'] if r['lang'] == 'en' else info['detail_zh']
        txt.insert(1.0, advice + '\n\n' + detail)
        txt.config(state='disabled')

    def clear_result(self):
        self.process_text.delete(1.0, tk.END)
        self.judgment_text.delete(1.0, tk.END)
        self.question_entry.delete(0, tk.END)
        self.current_result = None


def main():
    root = tk.Tk()
    app = DivinationGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
