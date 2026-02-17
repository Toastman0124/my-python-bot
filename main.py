from datetime import datetime

# 取得目前的日期與時間
now = datetime.now()

# 格式化成「時:分」
current_time = now.strftime("%H:%M")

print(f"現在的時間是 {current_time}")
