import argparse, requests

url = "http://api.axfrcheck.com/api/domain/openssl.org"

def send_get(url, method="GET"):
    """makes http request and returns a json string"""
    
    method = method.strip().lower()

    if not hasattr(requests, method):
        raise ValueError("invalid request method")
    try:
        response = getattr(requests, method)(url)
        return response.json()
    except:
        return "{\"error_code\":\"X04C\",\"message\":\"No internet connection\"}"

print(send_get(url, 'options'))
