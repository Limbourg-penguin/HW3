# -*- coding: utf-8 -*-
"""
Python 課堂練習與作業完整整合檔案
包含：
1. 課堂練習 1 - 基礎 Queue 操作
2. 課堂練習 2 - Overflow 與 Underflow 防護
3. HW3-1 - 智能派單 (Smart Enqueue)
4. HW3-2 - Two Sum (暴力解 & 效率解)
"""

from collections import deque

def run_in_class_exercise_1():
    print("="*40)
    print(" 課堂練習 1：基礎 Queue 操作 ")
    print("="*40)
    
    # 1. 建立一個名為 barracks 的 Queue
    barracks = deque()

    # 2. 玩家依序點擊生產：劍士、弓手、騎士
    barracks.append("劍士")
    barracks.append("弓手")
    barracks.append("騎士")
    print(f"目前排隊名單：{list(barracks)}")

    # 3. 兵營生產完畢，請將排在最前面的單位拿出來
    finished_unit = barracks.popleft()
    print(f"生產完成：{finished_unit} 出列！")
    print(f"剩下的排隊名單：{list(barracks)}
")


def run_in_class_exercise_2():
    print("="*40)
    print(" 課堂練習 2：Overflow 與 Underflow 防護 ")
    print("="*40)
    
    barracks = deque(["劍士", "弓手"])
    print(f"初始狀態：{list(barracks)}")

    print("
--- 測試 1：玩家想再塞一個『騎士』進來 (防爆測試) ---")
    # 任務 1：請檢查 barracks 長度。如果小於 2 才能加進去
    if len(barracks) < 2:
        barracks.append("騎士")
        print("騎士排隊成功！")
    else:
        print("產線全滿，拒絕騎士！")

    print("
--- 測試 2：系統瘋狂加速，連續出列 3 次 (防呆測試) ---")
    # 任務 2：我們手動複製貼上 3 次出列動作。請加上防呆機制，避免第 3 次 Error
    # (第 1 次出列)
    if len(barracks) > 0:
        print(f"{barracks.popleft()} 生產完成！")
    else:
        print("兵營閒置中，無法出列")

    # (第 2 次出列)
    if len(barracks) > 0:
        print(f"{barracks.popleft()} 生產完成！")
    else:
        print("兵營閒置中，無法出列")

    # (第 3 次出列 - 這裡會觸發防呆)
    if len(barracks) > 0:
        print(f"{barracks.popleft()} 生產完成！")
    else:
        print("兵營閒置中，無法出列
")


def run_hw3_1_smart_enqueue():
    print("="*40)
    print(" HW3-1：智能派單 (Smart Enqueue) ")
    print("="*40)
    
    player_gold = 150
    barracks_A = deque()
    barracks_B = deque()

    # 玩家送來的一批訂單 (包含單位名稱與花費)
    orders = [
        {"unit": "劍士", "cost": 20},
        {"unit": "弓手", "cost": 30},
        {"unit": "騎士", "cost": 50},
        {"unit": "投石車", "cost": 40}
    ]

    for round_num, order in enumerate(orders):
        print(f"--- 第 {round_num} 回合 ---")
        
        # 系統邏輯順序判定：
        # 1. Dequeue 階段：每當偶數回合 (0, 2, ...)，系統自動觸發 Dequeue 出列
        if round_num % 2 == 0:
            # Underflow 防呆：出列前必須檢查產線是否有單位
            if len(barracks_A) > 0:
                print(f"A 廠生產完成：{barracks_A.popleft()} 出列！")
            else:
                print("A 廠沒東西可做 (Underflow 防護成功)")
                
            if len(barracks_B) > 0:
                print(f"B 廠生產完成：{barracks_B.popleft()} 出列！")
            else:
                print("B 廠沒東西可做 (Underflow 防護成功)")

        # 2. Enqueue 階段：處理訂單進佇列
        unit = order["unit"]
        cost = order["cost"]
        
        # 資源檢核
        if player_gold < cost:
            print(f"黃金不足，無法生產 {unit}")
        else:
            # Overflow 防禦：A 和 B 的產線上限都是 2 個。如果兩個兵營都滿了，拒絕生產
            if len(barracks_A) >= 2 and len(barracks_B) >= 2:
                print(f"產線全滿！ {unit} 訂單拒絕")
            else:
                # 負載平衡：若買得起，將訂單放進排隊人數較少的 Queue（一樣長則優先放 A）
                if len(barracks_A) <= len(barracks_B):
                    barracks_A.append(unit)
                    player_gold -= cost
                    print(f"{unit} 分派至 A 廠 (剩餘黃金: {player_gold})")
                else:
                    barracks_B.append(unit)
                    player_gold -= cost
                    print(f"{unit} 分派至 B 廠 (剩餘黃金: {player_gold})")

        print(f"A: {list(barracks_A)} | B: {list(barracks_B)}
")


def run_hw3_2_two_sum():
    print("="*40)
    print(" HW3-2：Two Sum (初級) ")
    print("="*40)
    
    nums = [2, 7, 11, 15]
    target = 9
    
    # 解法一：接受暴力解
    def two_sum_brute_force(nums_list, target_val):
        for i in range(len(nums_list)):
            for j in range(i + 1, len(nums_list)):
                if nums_list[i] + nums_list[j] == target_val:
                    return [i, j]
        return []

    # 解法二：效率解
    def two_sum_efficient(nums_list, target_val):
        seen = {}
        for index, num in enumerate(nums_list):
            complement = target_val - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return []

    print(f"輸入陣列: {nums}, 目標值: {target}")
    print("1. 暴力解輸出結果:", two_sum_brute_force(nums, target))
    print("2. 效率解輸出結果:", two_sum_efficient(nums, target))
    print()


if __name__ == "__main__":
    print("開始執行所有練習與作業題目：
")
    run_in_class_exercise_1()
    run_in_class_exercise_2()
    run_hw3_1_smart_enqueue()
    run_hw3_2_two_sum()
