import os
import requests
sckey = os.getenv("MY_API_KEY")

def get_detailed_weather():
    # 定義城市字典：{ '英文名稱': '顯示名稱' }
    cities = {
        "Shanghai": "上海",
        "Taipei": "台灣/台北",
        "Tainan": "台灣/台南",
        "Pingtung": "台灣/屏東",
        "Dongying": "東營"
    }
    
    weather_reports = []
    
    for en_name, cn_name in cities.items():
        try:
            # 加入 lang=zh-tw 參數以獲取中文描述
            url = f"https://wttr.in/{en_name}?format=j1&lang=zh-tw"
            response = requests.get(url)
            data = response.json()
            
            # 獲取明天的預報 (Index 1)
            tomorrow = data['weather'][1]
            max_temp = tomorrow['maxtempC']
            min_temp = tomorrow['mintempC']
            
            # 獲取中文天氣狀況描述
            # 優先從天氣描述列表中抓取中文
            condition = tomorrow['hourly'][4]['lang_zh-tw'][0]['value']
            
            report = f"📍 【{cn_name}】\n🌡️ 氣溫：{min_temp}°C ~ {max_temp}°C\n☁️ 狀況：{condition}"
            weather_reports.append(report)
            
        except Exception as e:
            weather_reports.append(f"❌ 【{cn_name}】 數據抓取失敗")
            
    # 組合最終推播內容
    header = "📅 明日氣溫預報 (2026-02-18)\n"
    footer = "\n---\n系統自動發送"
    return header + "\n\n" + "\n\n".join(weather_reports) + footer

def send_server_chan(content):
    api_key = "SCT314665THD71aeZjNXfG77gIwE8oKyii"
    url = f"https://sctapi.ftqq.com/{api_key}.send"
    params = {
        "title": "明日各地氣溫預報",
        "desp": content
    }
    response = requests.post(url, data=params)
    return response.json()

if __name__ == "__main__":
    content = get_detailed_weather()
    print(content)
    result = send_server_chan(content)
    print(f"發送結果：{result}")
