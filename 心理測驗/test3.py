def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("請選擇一個選項 (1-4): "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("請輸入有效的選項號碼。")
        except ValueError:
            print("請輸入有效的選項號碼。")

# 問題與對應的選項
questions = [
    ("如果你可以選擇一種超能力，你會選哪個？", 
     ["超音速奔跑，就像飛毛腿一樣", "在水中呼吸，像人魚一樣", "瞬間學會一本書的內容，變身智慧大師", "瞬間完成遊戲，成為全服第一高手"]),
    
    ("如果你可以挑選一種娛樂活動來打發時間，你會選？", 
     ["戶外露營，在星空下講鬼故事", "深夜看電影，連續劇馬拉松", "鑽進書堆，學點冷門知識", "玩遊戲，拯救世界和打爆怪物"]),
    
    ("假如你要參加一場派對，你會怎麼打扮？", 
     ["穿上運動裝，隨時準備來場比賽", "穿著浴袍來，帶點幽默風", "帶上眼鏡和筆記本，隨時學習派對生存指南", "穿成動漫角色，讓大家刮目相看"]),
    
    ("週末你最想做的事是什麼？", 
     ["早上起來去跑步，像風一樣自由", "睡到自然醒，再來個長時間泡澡", "窩在沙發上看書，讓腦袋充電", "挑戰遊戲新關卡，不斷刷新紀錄"]),
    
    ("如果可以變成一種樂器，你會是哪一種？", 
     ["鼓，咚咚響不停", "大提琴，低沉又深情", "小提琴，優雅又智慧", "電子吉他，狂野和熱血"])
]

# 計分系統
scores = {
    "狗": 0,
    "貓": 0,
    "兔子": 0,
    "烏龜": 0
}

# 根據回答計算分數
for question, options in questions:
    answer = ask_question(question, options)
    if answer == 1:
        scores["狗"] += 1
    elif answer == 2:
        scores["貓"] += 1
    elif answer == 3:
        scores["兔子"] += 1
    elif answer == 4:
        scores["烏龜"] += 1

# 判斷結果
result = max(scores, key=scores.get)
print(f"你測驗的結果是：{result}！")
