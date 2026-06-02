#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小六壬占卜程序 - 完整增强版
基于传统小六壬法，补充详细解读和完整测算逻辑
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import random

class XiaoLiuRen:
    """小六壬占卜类 - 完整增强版"""
    
    # 六神完整信息（增强版）
    LIU_SHEN = {
        "大安": {
            "wuxing": "木",
            "jiazi": "寅",
            "description": "身未动时，属木青龙，凡谋事主一、五、七",
            "meaning": "安稳、吉祥、静止、守成",
            "detail": "大安事事昌，求财在坤方，失物去不远，宅舍保安康",
            "advice": "此卦象显示事情平稳安定，适合守成等待。\n求财可往西南方，失物不远可自行找回。",
            "full_interpretation": """
【大安卦详解】
大安者，身未动也。五行属木，颜色青，方位东，临青龙，凡谋事主一、五、七。

◎ 断曰：
大安事事昌，求财在坤方，
失物去不远，宅舍保安康。

◎ 曰：
行人身未动，病者主无妨，
将军回田野，仔细更推详。

◎ 解释：
大安事业运：平稳发展，适合守成，不宜冒进
大安财运：求财在坤方（西南方），正财稳定
大安感情：感情稳定，适合维系现有关系
大安健康：身体安康，无大碍
大安失物：失物不远，多在家中或常去之处
大安出行：出行平安，无阻碍
大安官非：官事平缓，无大碍

◎ 数字：1、5、7
◎ 季节：春季
◎ 时辰：寅时（3-5点）
◎ 方向：东方、东南方
◎ 颜色：青、绿
◎ 人物：长男、君子、贵人
""",
            "trigram": "☳",
            "nature": "阳",
            "element_detail": "甲木青龙，主仁慈、生长、起始"
        },
        
        "留连": {
            "wuxing": "土",
            "jiazi": "戌",
            "description": "卒未归时，属土玄武，凡谋事主二、八、十",
            "meaning": "纠缠、拖延、犹豫、反复",
            "detail": "留连事难成，求谋日未明，官事只宜缓，去者未回程",
            "advice": "此卦象显示事情有拖延，需要耐心等待。\n不宜急于求成，官事应缓处理。",
            "full_interpretation": """
【留连卦详解】
留连者，卒未归也。五行属土，颜色黄，方位中，临玄武，凡谋事主二、八、十。

◎ 断曰：
留连事难成，求谋日未明，
官事只宜缓，去者未回程。

◎ 曰：
事有留连意，谋为未便通，
漫语君且住，仔细好推穷。

◎ 解释：
留连事业运：事情拖延，难以速成，需耐心等待
留连财运：求财不成，财运平平，不宜投资
留连感情：感情纠缠，有阻碍，需时间化解
留连健康：病者拖延，恢复缓慢
留连失物：失物难寻，多在暗处或被人误拿
留连出行：出行有阻，不宜远行
留连官非：官事拖延，宜缓不宜急

◎ 数字：2、8、10
◎ 季节：季夏（长夏）
◎ 时辰：戌时（19-21点）
◎ 方向：中央、西南方
◎ 颜色：黄、棕
◎ 人物：小人、盗贼、阴人
""",
            "trigram": "☷",
            "nature": "阴",
            "element_detail": "戊土玄武，主诚信、承载、阻滞"
        },
        
        "速喜": {
            "wuxing": "火",
            "jiazi": "午",
            "description": "人便至时，属火朱雀，凡谋事主三、六、九",
            "meaning": "喜庆、快速、成功、光明",
            "detail": "速喜喜来临，求财向南行，失物申未午，逢人路上寻",
            "advice": "此卦象显示喜事临近，事情会快速解决。\n求财可往南方，失物可在午时找到。",
            "full_interpretation": """
【速喜卦详解】
速喜者，人便至也。五行属火，颜色红，方位南，临朱雀，凡谋事主三、六、九。

◎ 断曰：
速喜喜来临，求财向南行，
失物申未午，逢人路上寻。

◎ 曰：
速喜令人喜，交易成且长，
行人在半路，贵人到厅堂。

◎ 解释：
速喜事业运：喜事临近，事业快速成功，有贵人相助
速喜财运：求财向南行（南方），财运亨通
速喜感情：感情喜庆，有喜讯传来
速喜健康：病者快速康复，身体健康
速喜失物：失物在南方，午时（11-13点）可寻回
速喜出行：出行顺利，有喜事
速喜官非：官事快速解决，有贵人相助

◎ 数字：3、6、9
◎ 季节：夏季
◎ 时辰：午时（11-13点）
◎ 方向：南方
◎ 颜色：红、紫
◎ 人物：中女、贵人、客人
""",
            "trigram": "☲",
            "nature": "阳",
            "element_detail": "丙火朱雀，主礼、光明、急速"
        },
        
        "赤口": {
            "wuxing": "金",
            "jiazi": "酉",
            "description": "官事凶时，属金白虎，凡谋事主四、七、十",
            "meaning": "口舌、凶险、争执、疾病",
            "detail": "赤口主口伤，官事且紧防，失物急去寻，行人有惊慌",
            "advice": "此卦象显示有口舌是非，需防官非疾病。\n失物应尽快寻找，出行小心谨慎。",
            "full_interpretation": """
【赤口卦详解】
赤口者，官事凶也。五行属金，颜色白，方位西，临白虎，凡谋事主四、七、十。

◎ 断曰：
赤口主口伤，官事且紧防，
失物急去寻，行人有惊慌。

◎ 曰：
赤口主口舌，官非且紧防，
失物急去寻，行人有惊慌。

◎ 解释：
赤口事业运：有口舌是非，需防小人，不宜妄动
赤口财运：求财无利，且有破财之虞
赤口感情：感情有口舌，争执多，需忍让
赤口健康：病者有险，需防病情加重
赤口失物：失物在西方，需急寻，否则难找回
赤口出行：出行有险，需小心谨慎
赤口官非：官事凶险，需紧防，宜和解

◎ 数字：4、7、10
◎ 季节：秋季
◎ 时辰：酉时（17-19点）
◎ 方向：西方、西北方
◎ 颜色：白、金
◎ 人物：少女、仇人、恶人
""",
            "trigram": "☱",
            "nature": "阴",
            "element_detail": "庚金白虎，主义、决断、凶险"
        },
        
        "小吉": {
            "wuxing": "水",
            "jiazi": "子",
            "description": "人来喜时，属水六合，凡谋事主一、五、七",
            "meaning": "和合、顺利、喜悦、婚姻",
            "detail": "小吉最吉昌，路上好商量，阴人来报喜，失物在坤方",
            "advice": "此卦象显示和合顺利，有喜事临门。\n婚姻和合，求财有利，失物在西南方。",
            "full_interpretation": """
【小吉卦详解】
小吉者，人来喜也。五行属水，颜色黑，方位北，临六合，凡谋事主一、五、七。

◎ 断曰：
小吉最吉昌，路上好商量，
阴人来报喜，失物在坤方。

◎ 曰：
小吉最吉昌，婚姻有人帮，
出行得顺风，失物不出方。

◎ 解释：
小吉事业运：和合顺利，有人相助，事业吉昌
小吉财运：求财有利，财运亨通，多有意外之财
小吉感情：婚姻和合，感情顺利，有喜事
小吉健康：身体康健，病者易愈
小吉失物：失物在坤方（西南方），可寻回
小吉出行：出行顺利，得顺风，有贵人相助
小吉官非：官事和解，无大碍

◎ 数字：1、5、7
◎ 季节：冬季
◎ 时辰：子时（23-1点）
◎ 方向：北方、东北方
◎ 颜色：黑、蓝
◎ 人物：中男、阴人、媒人
""",
            "trigram": "☵",
            "nature": "阳",
            "element_detail": "壬水六合，主智、和合、喜悦"
        },
        
        "空亡": {
            "wuxing": "土",
            "jiazi": "辰戌丑未",
            "description": "音信稀时，属土勾陈，凡谋事主三、六、九",
            "meaning": "虚空、失败、消散、疾病",
            "detail": "空亡事不祥，阴人多乖张，求财无利益，行人有灾殃",
            "advice": "此卦象显示事情落空，需要重新规划。\n求财无利，出行有灾，宜守不宜进。",
            "full_interpretation": """
【空亡卦详解】
空亡者，音信稀也。五行属土，颜色黄，方位中，临勾陈，凡谋事主三、六、九。

◎ 断曰：
空亡事不祥，阴人多乖张，
求财无利益，行人有灾殃。

◎ 曰：
空亡事不祥，阴人多乖张，
求财无利益，行人有灾殃。

◎ 解释：
空亡事业运：事情落空，谋划无成，需重新规划
空亡财运：求财无利，且有破财之虞，不宜投资
空亡感情：感情空虚，有分离之象
空亡健康：病者加重，需防不治之症
空亡失物：失物难寻，多已消散或被人拿走
空亡出行：出行有灾，不宜远行
空亡官非：官事凶险，有牢狱之灾

◎ 数字：3、6、9
◎ 季节：四季末
◎ 时辰：辰戌丑未时
◎ 方向：中央、四库方
◎ 颜色：黄、褐
◎ 人物：小人、阴人、僧道
""",
            "trigram": "☶",
            "nature": "阴",
            "element_detail": "戊己土勾陈，主诚信、空亡、消散"
        }
    }
    
    def __init__(self):
        self.positions = list(self.LIU_SHEN.keys())
    
    def get_lunar_month(self, date=None):
        """获取农历月份（简化版，实际需要农历转换）"""
        if date is None:
            date = datetime.now()
        # 这里简化为直接使用公历月份
        # 实际应该使用农历转换库如 lunardate
        return date.month
    
    def get_lunar_day(self, date=None):
        """获取农历日期（简化版）"""
        if date is None:
            date = datetime.now()
        # 简化为使用公历日期
        return date.day
    
    def get_hour_position(self, hour=None):
        """根据时辰确定起始位置"""
        if hour is None:
            hour = datetime.now().hour
        
        # 时辰对应表（12时辰对应六神）
        # 子时(23-1)→大安, 丑时(1-3)→留连, 寅时(3-5)→速喜
        # 卯时(5-7)→赤口, 辰时(7-9)→小吉, 巳时(9-11)→空亡
        # 午时(11-13)→大安, 未时(13-15)→留连, 申时(15-17)→速喜
        # 酉时(17-19)→赤口, 戌时(19-21)→小吉, 亥时(21-23)→空亡
        
        if 23 <= hour or hour < 1:
            return "大安"  # 子时
        elif 1 <= hour < 3:
            return "留连"  # 丑时
        elif 3 <= hour < 5:
            return "速喜"  # 寅时
        elif 5 <= hour < 7:
            return "赤口"  # 卯时
        elif 7 <= hour < 9:
            return "小吉"  # 辰时
        elif 9 <= hour < 11:
            return "空亡"  # 巳时
        elif 11 <= hour < 13:
            return "大安"  # 午时
        elif 13 <= hour < 15:
            return "留连"  # 未时
        elif 15 <= hour < 17:
            return "速喜"  # 申时
        elif 17 <= hour < 19:
            return "赤口"  # 酉时
        elif 19 <= hour < 21:
            return "小吉"  # 戌时
        elif 21 <= hour < 23:
            return "空亡"  # 亥时
    
    def calculate_position(self, month, day, hour=None):
        """
        计算小六壬占卜结果（完整算法）
        方法：月起始，日走位，时落位
        """
        # 月份对应六神（1-6循环）
        month_map = {
            1: "大安", 2: "留连", 3: "速喜",
            4: "赤口", 5: "小吉", 6: "空亡"
        }
        
        # 1. 以月份为起点
        # 如果月份大于6，则循环计算
        month_key = (month - 1) % 6 + 1
        start_pos = month_map[month_key]
        start_index = self.positions.index(start_pos)
        current_index = start_index
        
        # 2. 从月份位置开始，按日期数推算
        # 日期数 = 日期 - 1（因为起点已经算第1天）
        for i in range(day - 1):
            current_index = (current_index + 1) % 6
        current = self.positions[current_index]
        
        # 3. 从日期位置开始，按时辰数推算
        if hour is not None:
            hour_pos = self.get_hour_position(hour)
            hour_index = self.positions.index(hour_pos)
            # 时辰数 = 时辰索引（已经考虑了12时辰对应6神）
            current_index = (current_index + hour_index) % 6
            current = self.positions[current_index]
        
        return current
    
    def divine(self, question, month=None, day=None, hour=None):
        """
        进行占卜（完整版）
        
        Args:
            question: 占卜问题
            month: 农历月份（可选，默认当前月）
            day: 农历日期（可选，默认当前日）
            hour: 时辰（可选，默认当前时辰）
        
        Returns:
            dict: 占卜结果（包含完整解读）
        """
        # 如果没有提供时间，使用当前时间
        now = datetime.now()
        if month is None:
            month = self.get_lunar_month(now)
        if day is None:
            day = self.get_lunar_day(now)
        if hour is None:
            hour = now.hour
        
        # 计算占卜结果
        result = self.calculate_position(month, day, hour)
        
        # 获取详细信息
        info = self.LIU_SHEN[result]
        
        # 获取时辰名称
        shichen_name = self.get_shichen_name(hour)
        
        return {
            "question": question,
            "divination_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "lunar_month": month,
            "lunar_day": day,
            "hour": hour,
            "shichen": shichen_name,
            "result": result,
            "wuxing": info["wuxing"],
            "jiazi": info["jiazi"],
            "description": info["description"],
            "meaning": info["meaning"],
            "detail": info["detail"],
            "advice": info["advice"],
            "full_interpretation": info["full_interpretation"],
            "trigram": info["trigram"],
            "nature": info["nature"],
            "element_detail": info["element_detail"]
        }
    
    def random_divine(self, question):
        """随机占卜（简化版，用于快速占卜）"""
        result = random.choice(self.positions)
        info = self.LIU_SHEN[result]
        
        return {
            "question": question,
            "divination_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "method": "随机占卜",
            "result": result,
            "wuxing": info["wuxing"],
            "jiazi": info["jiazi"],
            "description": info["description"],
            "meaning": info["meaning"],
            "detail": info["detail"],
            "advice": info["advice"],
            "full_interpretation": info["full_interpretation"],
            "trigram": info["trigram"],
            "nature": info["nature"],
            "element_detail": info["element_detail"]
        }
    
    def get_shichen_name(self, hour):
        """获取时辰名称"""
        if 23 <= hour or hour < 1:
            return "子时"
        elif 1 <= hour < 3:
            return "丑时"
        elif 3 <= hour < 5:
            return "寅时"
        elif 5 <= hour < 7:
            return "卯时"
        elif 7 <= hour < 9:
            return "辰时"
        elif 9 <= hour < 11:
            return "巳时"
        elif 11 <= hour < 13:
            return "午时"
        elif 13 <= hour < 15:
            return "未时"
        elif 15 <= hour < 17:
            return "申时"
        elif 17 <= hour < 19:
            return "酉时"
        elif 19 <= hour < 21:
            return "戌时"
        elif 21 <= hour < 23:
            return "亥时"


class DivinationGUI:
    """小六壬占卜GUI类 - 增强版"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("小六壬占卜程序 - 完整增强版")
        self.root.geometry("900x800")
        self.root.configure(bg='#f0f0f0')
        
        # 设置窗口图标（如果有的话）
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
        
        self.diviner = XiaoLiuRen()
        
        self.setup_ui()
    
    def setup_ui(self):
        """设置UI界面"""
        # 标题
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🔮 小六壬占卜程序",
            font=("微软雅黑", 24, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="— 传统六壬掐指算法 · 完整增强版 —",
            font=("微软雅黑", 12),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        subtitle_label.pack(pady=(5, 0))
        
        # 主容器
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=40, pady=20, fill='both', expand=True)
        
        # 输入区域
        input_frame = ttk.LabelFrame(main_frame, text="占卜输入", padding=20)
        input_frame.pack(fill='x', pady=(0, 20))
        
        # 问题输入
        ttk.Label(input_frame, text="请输入要占卜的事情：", font=("微软雅黑", 10)).pack(anchor='w')
        self.question_entry = ttk.Entry(input_frame, font=("微软雅黑", 11), width=60)
        self.question_entry.pack(fill='x', pady=(5, 15))
        self.question_entry.insert(0, "")
        
        # 时间显示
        time_frame = ttk.Frame(input_frame)
        time_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Label(time_frame, text="当前时间：", font=("微软雅黑", 10)).pack(side='left')
        self.time_label = ttk.Label(
            time_frame,
            text="",
            font=("微软雅黑", 10, "bold"),
            foreground='#2980b9'
        )
        self.time_label.pack(side='left', padx=(10, 0))
        
        # 时辰显示
        self.shichen_label = ttk.Label(
            time_frame,
            text="",
            font=("微软雅黑", 10),
            foreground='#8e44ad'
        )
        self.shichen_label.pack(side='left', padx=(20, 0))
        
        # 按钮区域
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill='x')
        
        self.divine_btn = ttk.Button(
            button_frame,
            text="开始占卜",
            command=self.perform_divination
        )
        self.divine_btn.pack(side='left', padx=(0, 10))
        
        self.random_btn = ttk.Button(
            button_frame,
            text="随机占卜",
            command=self.random_divination
        )
        self.random_btn.pack(side='left', padx=(0, 10))
        
        self.detail_btn = ttk.Button(
            button_frame,
            text="查看详解",
            command=self.show_detail
        )
        self.detail_btn.pack(side='left', padx=(0, 10))
        
        self.clear_btn = ttk.Button(
            button_frame,
            text="清空结果",
            command=self.clear_result
        )
        self.clear_btn.pack(side='left')
        
        # 结果区域
        result_frame = ttk.LabelFrame(main_frame, text="占卜结果", padding=20)
        result_frame.pack(fill='both', expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            font=("微软雅黑", 10),
            wrap=tk.WORD,
            height=20,
            bg='#ffffff',
            fg='#2c3e50'
        )
        self.result_text.pack(fill='both', expand=True)
        
        # 底部声明
        footer_frame = tk.Frame(self.root, bg='#f0f0f0')
        footer_frame.pack(pady=20)
        
        footer_label = tk.Label(
            footer_frame,
            text="声明：本程序仅供参考娱乐，不构成任何建议 | 基于传统小六壬法",
            font=("微软雅黑", 9),
            bg='#f0f0f0',
            fg='#95a5a6'
        )
        footer_label.pack()
        
        # 初始化时间显示
        self.update_time()
        
        # 存储当前结果
        self.current_result = None
    
    def update_time(self):
        """更新时间显示"""
        now = datetime.now()
        time_str = now.strftime("%Y年%m月%d日 %H:%M:%S")
        self.time_label.config(text=time_str)
        
        # 更新时辰显示
        shichen = self.diviner.get_shichen_name(now.hour)
        self.shichen_label.config(text=f"时辰：{shichen}")
        
        # 每秒更新一次
        self.root.after(1000, self.update_time)
    
    def perform_divination(self):
        """执行占卜"""
        question = self.question_entry.get().strip()
        
        if not question:
            messagebox.showwarning("提示", "请输入要占卜的事情！")
            return
        
        # 获取当前时间
        now = datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        
        # 执行占卜
        result = self.diviner.divine(question, month, day, hour)
        
        # 保存当前结果
        self.current_result = result
        
        # 显示结果
        self.display_result(result)
    
    def random_divination(self):
        """随机占卜"""
        question = self.question_entry.get().strip()
        
        if not question:
            messagebox.showwarning("提示", "请输入要占卜的事情！")
            return
        
        # 执行随机占卜
        result = self.diviner.random_divine(question)
        
        # 保存当前结果
        self.current_result = result
        
        # 显示结果
        self.display_result(result)
    
    def show_detail(self):
        """显示详细解读"""
        if self.current_result is None:
            messagebox.showinfo("提示", "请先进行占卜")
            return
        
        # 创建详解窗口
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"{self.current_result['result']} - 详细解读")
        detail_window.geometry("700x600")
        
        # 详解文本
        detail_text = scrolledtext.ScrolledText(
            detail_window,
            font=("微软雅黑", 10),
            wrap=tk.WORD,
            bg='#fafafa'
        )
        detail_text.pack(fill='both', expand=True, padx=20, pady=20)
        
        # 插入详细解读
        detail_text.insert(1.0, self.current_result['full_interpretation'])
        detail_text.config(state='disabled')  # 只读
    
    def display_result(self, result):
        """显示占卜结果"""
        self.result_text.delete(1.0, tk.END)
        
        # 构建结果文本
        output = f"""
{'='*70}
                    小六壬占卜结果
{'='*70}

【问题】{result['question']}
【占卜时间】{result['divination_time']}
"""
        
        if 'lunar_month' in result:
            output += f"""【农历月份】{result['lunar_month']}月
【农历日期】{result['lunar_day']}日
【时辰】{result['hour']}时（{result['shichen']}）
"""
        
        if 'method' in result:
            output += f"【占卜方式】{result['method']}\n"
        
        output += f"""
{'-'*70}
【占卜结果】{result['result']} {result['trigram']}
【五行属性】{result['wuxing']}（{result['element_detail']}）
【天干地支】{result['jiazi']}
【阴阳属性】{result['nature']}
【基本含义】{result['meaning']}
【详细解说】{result['description']}

【口诀】
    {result['detail']}
{'-'*70}

【解读建议】
{result['advice']}

💡 提示：点击"查看详解"按钮查看完整卦象解读

{'='*70}
"""
        
        self.result_text.insert(1.0, output)
        
        # 根据结果设置不同的颜色
        result_color = self.get_result_color(result['result'])
        self.result_text.tag_add("result", "8.0", "8.end")
        self.result_text.tag_config("result", foreground=result_color, font=("微软雅黑", 12, "bold"))
    
    def get_result_color(self, result):
        """根据占卜结果返回对应颜色"""
        color_map = {
            "大安": "#27ae60",  # 绿色
            "留连": "#f39c12",  # 橙色
            "速喜": "#e74c3c",  # 红色
            "赤口": "#c0392b",  # 深红
            "小吉": "#2980b9",  # 蓝色
            "空亡": "#7f8c8d"   # 灰色
        }
        return color_map.get(result, "#2c3e50")
    
    def clear_result(self):
        """清空结果"""
        self.result_text.delete(1.0, tk.END)
        self.question_entry.delete(0, tk.END)
        self.current_result = None


def main():
    """主程序"""
    root = tk.Tk()
    app = DivinationGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
