#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小六壬占卜程序 - 图形界面版
基于传统小六壬法开发，带GUI界面
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import random
import sys
import os

class XiaoLiuRen:
    """小六壬占卜类"""
    
    # 六神方位及其含义
    LIU_SHEN = {
        "大安": {
            "wuxing": "木",
            "description": "身未动时，属木青龙，凡谋事主一、五、七",
            "meaning": "安稳、吉祥、静止、守成",
            "detail": "大安事事昌，求财在坤方，失物去不远，宅舍保安康",
            "advice": "此卦象显示事情平稳安定，适合守成等待。\n求财可往西南方，失物不远可自行找回。"
        },
        "留连": {
            "wuxing": "土",
            "description": "卒未归时，属土玄武，凡谋事主二、八、十",
            "meaning": "纠缠、拖延、犹豫、反复",
            "detail": "留连事难成，求谋日未明，官事只宜缓，去者未回程",
            "advice": "此卦象显示事情有拖延，需要耐心等待。\n不宜急于求成，官事应缓处理。"
        },
        "速喜": {
            "wuxing": "火",
            "description": "人便至时，属火朱雀，凡谋事主三、六、九",
            "meaning": "喜庆、快速、成功、光明",
            "detail": "速喜喜来临，求财向南行，失物申未午，逢人路上寻",
            "advice": "此卦象显示喜事临近，事情会快速解决。\n求财可往南方，失物可在午时找到。"
        },
        "赤口": {
            "wuxing": "金",
            "description": "官事凶时，属金白虎，凡谋事主四、七、十",
            "meaning": "口舌、凶险、争执、疾病",
            "detail": "赤口主口伤，官事且紧防，失物急去寻，行人有惊慌",
            "advice": "此卦象显示有口舌是非，需防官非疾病。\n失物应尽快寻找，出行小心谨慎。"
        },
        "小吉": {
            "wuxing": "水",
            "description": "人来喜时，属水六合，凡谋事主一、五、七",
            "meaning": "和合、顺利、喜悦、婚姻",
            "detail": "小吉最吉昌，路上好商量，阴人来报喜，失物在坤方",
            "advice": "此卦象显示和合顺利，有喜事临门。\n婚姻和合，求财有利，失物在西南方。"
        },
        "空亡": {
            "wuxing": "土",
            "description": "音信稀时，属土勾陈，凡谋事主三、六、九",
            "meaning": "虚空、失败、消散、疾病",
            "detail": "空亡事不祥，阴人多乖张，求财无利益，行人有灾殃",
            "advice": "此卦象显示事情落空，需要重新规划。\n求财无利，出行有灾，宜守不宜进。"
        }
    }
    
    def __init__(self):
        self.positions = list(self.LIU_SHEN.keys())
    
    def get_lunar_month(self, date=None):
        """获取农历月份（简化版）"""
        if date is None:
            date = datetime.now()
        return date.month
    
    def get_lunar_day(self, date=None):
        """获取农历日期（简化版）"""
        if date is None:
            date = datetime.now()
        return date.day
    
    def get_hour_position(self, hour=None):
        """根据时辰确定起始位置"""
        if hour is None:
            hour = datetime.now().hour
        
        # 时辰对应表
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
        计算小六壬占卜结果
        方法：月起始，日走位，时落位
        """
        # 月份对应六神（1-6循环）
        month_map = {
            1: "大安", 2: "留连", 3: "速喜",
            4: "赤口", 5: "小吉", 6: "空亡"
        }
        
        # 1. 以月份为起点
        start_pos = month_map[(month - 1) % 6 + 1]
        start_index = self.positions.index(start_pos)
        current_index = start_index
        
        # 2. 从月份位置开始，按日期数推算
        for i in range(day - 1):
            current_index = (current_index + 1) % 6
        current = self.positions[current_index]
        
        # 3. 从日期位置开始，按时辰数推算
        if hour is not None:
            hour_pos = self.get_hour_position(hour)
            hour_index = self.positions.index(hour_pos)
            current_index = (current_index + hour_index) % 6
            current = self.positions[current_index]
        
        return current
    
    def divine(self, question, month=None, day=None, hour=None):
        """
        进行占卜
        
        Args:
            question: 占卜问题
            month: 农历月份
            day: 农历日期
            hour: 时辰
        
        Returns:
            dict: 占卜结果
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
        
        return {
            "question": question,
            "divination_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "lunar_month": month,
            "lunar_day": day,
            "hour": hour,
            "result": result,
            "wuxing": info["wuxing"],
            "description": info["description"],
            "meaning": info["meaning"],
            "detail": info["detail"],
            "advice": info["advice"]
        }
    
    def random_divine(self, question):
        """随机占卜（简化版）"""
        result = random.choice(self.positions)
        info = self.LIU_SHEN[result]
        
        return {
            "question": question,
            "divination_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "method": "随机占卜",
            "result": result,
            "wuxing": info["wuxing"],
            "description": info["description"],
            "meaning": info["meaning"],
            "detail": info["detail"],
            "advice": info["advice"]
        }


class DivinationGUI:
    """小六壬占卜GUI类"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("小六壬占卜程序")
        self.root.geometry("800x700")
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
            text="— 传统六壬掐指算法 —",
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
            text="声明：本程序仅供参考娱乐，不构成任何建议",
            font=("微软雅黑", 9),
            bg='#f0f0f0',
            fg='#95a5a6'
        )
        footer_label.pack()
        
        # 初始化时间显示
        self.update_time()
    
    def update_time(self):
        """更新时间显示"""
        now = datetime.now()
        time_str = now.strftime("%Y年%m月%d日 %H:%M:%S")
        self.time_label.config(text=time_str)
        
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
        
        # 显示结果
        self.display_result(result)
    
    def display_result(self, result):
        """显示占卜结果"""
        self.result_text.delete(1.0, tk.END)
        
        # 构建结果文本
        output = f"""
{'='*60}
                    小六壬占卜结果
{'='*60}

【问题】{result['question']}
【占卜时间】{result['divination_time']}
"""
        
        if 'lunar_month' in result:
            output += f"""【农历月份】{result['lunar_month']}
【农历日期】{result['lunar_day']}
【时辰】{result['hour']}时
"""
        
        if 'method' in result:
            output += f"【占卜方式】{result['method']}\n"
        
        output += f"""
{'-'*60}
【占卜结果】{result['result']}
【五行属性】{result['wuxing']}
【基本含义】{result['meaning']}
【详细解说】{result['description']}

【口诀】
    {result['detail']}
{'-'*60}

【解读建议】
{result['advice']}

{'='*60}
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


def main():
    """主程序"""
    root = tk.Tk()
    app = DivinationGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
