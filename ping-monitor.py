# ping-monitor.py
import requests, time, sys
url = sys.argv[1] if len(sys.argv)>1 else "https://example.com"
for i in range(3):
    try:
        r = requests.get(url, timeout=5)
        print(f"{url} -> {r.status_code}")
    except Exception as e:
        print("Error:", e)
    time.sleep(1)
