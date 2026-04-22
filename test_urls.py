# Test if server is accessible
import requests

urls_to_test = [
    ('Home', 'http://127.0.0.1:8000/'),
    ('Admin', 'http://127.0.0.1:8000/admin/'),
    ('Services', 'http://127.0.0.1:8000/service/'),
    ('About', 'http://127.0.0.1:8000/about/'),
    ('Contact', 'http://127.0.0.1:8000/contact/'),
]

print("Testing URLs...")
for name, url in urls_to_test:
    try:
        r = requests.get(url, timeout=5)
        print(f"{name}: {r.status_code}")
    except Exception as e:
        print(f"{name}: ERROR - {e}")