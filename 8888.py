import requests
import threading

url = "https://earnmore.space/"  # استبدله برابط موقعك الحقيقي
threads = 1500  # عدد الاتصالات المتزامنة

def send_request():
    try:
        response = requests.get(url)
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

for i in range(threads):
    t = threading.Thread(target=send_request)
    t.start()
