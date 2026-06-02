#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小六壬占卜程序
基于传统小六壬法开发
"""

import random
from datetime import datetime

class XiaoLiuRen:
    """小六壬占卜类"""
    
    # 六神方位及其含义
    LIU_SHEN = {
        "大安": {
            "wuxing": "木",
            "description": "身未动时，属木青龙，凡谋事主一、五、七",
            "meaning": "安稳、吉祥、静止、守成",
            "detail": "大安事事昌，求财在坤方，失物去不远，宅舍保安康"
        },
        "留连": {
            "wuxing": "土",
            "description": "卒未归时，属土玄武，凡谋事主二、八、十",
            "meaning": "纠缠、拖延、犹豫、反复",
            "detail": "留连事难成，求谋日未明，官事只宜缓，去者未回程"
        },
        "速喜": {
            "wuxing": "火",
            "description": "人便至时，属火朱雀，凡谋事主三、六、九",
            "meaning": "喜庆、快速、成功、光明",
            "detail": "速喜喜来临，求财向南行，失物申未午，逢人路上寻"
        },
        "赤口": {
            "wuxing": "金",
            "description": "官事凶时，属金白虎，凡谋事主四、七、十",
            "meaning": "口舌、凶险、争执、疾病",
            "detail": "赤口主口伤，官事且紧防，失物急去寻，行人有惊慌"
        },
        "小吉": {
            "wuxing": "水",
            "description": "人来喜时，属水六合，凡谋事主一、五、七",
            "meaning": "和合、顺利、喜悦、婚姻",
            "detail": "小吉最吉昌，路上好商量，阴人来报喜，失物在坤方"
        },
        "空亡": {
            "wuxing": "土",
            "description": "音信稀时，属土勾陈，凡谋事主三、六、九",
            "meaning": "虚空、失败、消散、疾病",
            "detail": "空亡事不祥，阴人多乖张，求财无利益，行人有灾殃"
        }
    }
    
    # 月份对应数字
    MONTH_MAP = {
        1: "大安", 2: "留连", 3: "速喜",
        4: "赤口", 5: "小吉", 6: "空亡"
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
        
        # 时辰对应表（简化）
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
        # 1. 以月份为起点
        start_index = list(self.MONTH_MAP.keys()).index(month % 6 or 6) if month > 6 else month - 1
        current = self.positions[start_index]
        
        # 2. 从月份位置开始，按日期数推算
        current_index = start_index
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
            month: 农历月份（可选，默认当前月）
            day: 农历日期（可选，默认当前日）
            hour: 时辰（可选，默认当前时辰）
        
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
            "detail": info["detail"]
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
            "description": info["description"],
            "meaning": info["meaning"],
            "detail": info["detail"]
        }

def print_result(result):
    """美化输出占卜结果"""
    print("\n" + "="*60)
    print(" " * 20 + "小六壬占卜结果")
    print("="*60)
    print(f"\n【问题】{result['question']}")
    print(f"【占卜时间】{result['divination_time']}")
    
    if 'lunar_month' in result:
        print(f"【农历月份】{result['lunar_month']}")
        print(f"【农历日期】{result['lunar_day']}")
        print(f"【时辰】{result['hour']}")
    
    print("\n" + "-"*60)
    print(f"【占卜结果】{result['result']}")
    print(f"【五行属性】{result['wuxing']}")
    print(f"【基本含义】{result['meaning']}")
    print(f"【详细解说】{result['description']}")
    print(f"\n【口诀】{result['detail']}")
    print("-"*60)
    
    # 解读建议
    print("\n【解读建议】")
    if result['result'] == "大安":
        print("  ► 此卦象显示事情平稳安定，适合守成等待。")
        print("  ► 求财可往西南方，失物不远可自行找回。")
    elif result['result'] == "留连":
        print("  ► 此卦象显示事情有拖延，需要耐心等待。")
        print("  ► 不宜急于求成，官事应缓处理。")
    elif result['result'] == "速喜":
        print("  ► 此卦象显示喜事临近，事情会快速解决。")
        print("  ► 求财可往南方，失物可在午时找到。")
    elif result['result'] == "赤口":
        print("  ► 此卦象显示有口舌是非，需防官非疾病。")
        print("  ► 失物应尽快寻找，出行小心谨慎。")
    elif result['result'] == "小吉":
        print("  ► 此卦象显示和合顺利，有喜事临门。")
        print("  ► 婚姻和合，求财有利，失物在西南方。")
    elif result['result'] == "空亡":
        print("  ► 此卦象显示事情落空，需要重新规划。")
        print("  ► 求财无利，出行有灾，宜守不宜进。")
    
    print("\n" + "="*60)
    print("【声明】本程序仅供参考娱乐，不构成任何建议。")
    print("="*60 + "\n")

def main():
    """主程序"""
    print("\n欢迎使用小六壬占卜程序！")
    print("-"*60)
    
    while True:
        print("\n请选择占卜方式：")
        print("1. 时间占卜（根据当前/指定时间）")
        print("2. 随机占卜（快速占卜）")
        print("3. 退出程序")
        
        choice = input("\n请输入选项(1/2/3): ").strip()
        
        if choice == "1":
            question = input("请输入您要占卜的问题: ").strip()
            if not question:
                question = "未知问题"
            
            use_current = input("是否使用当前时间？(y/n): ").strip().lower()
            
            if use_current == 'y':
                diviner = XiaoLiuRen()
                result = diviner.divine(question)
            else:
                try:
                    month = int(input("请输入农历月份(1-12): "))
                    day = int(input("请输入农历日期(1-30): "))
                    hour = int(input("请输入时辰(0-23): "))
                    diviner = XiaoLiuRen()
                    result = diviner.divine(question, month, day, hour)
                except ValueError:
                    print("输入错误，将使用当前时间进行占卜。")
                    diviner = XiaoLiuRen()
                    result = diviner.divine(question)
            
            print_result(result)
            
        elif choice == "2":
            question = input("请输入您要占卜的问题: ").strip()
            if not question:
                question = "未知问题"
            
            diviner = XiaoLiuRen()
            result = diviner.random_divine(question)
            print_result(result)
            
        elif choice == "3":
            print("\n感谢使用小六壬占卜程序，再见！\n")
            break
        else:
            print("\n无效选项，请重新选择。")

if __name__ == "__main__":
    main()
