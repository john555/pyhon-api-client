import argparse, requests

def send_get(url, method="GET"):
    """makes http request and returns a json string"""
    
    method = method.strip().lower()

    if not hasattr(requests, method):
        raise ValueError("invalid request method")

    try:
        response = getattr(requests, method)(url)
        return response.json()
    except:
        return {"error_code":"X04C", "message":"No internet connection"}

def main():

    parser = argparse.ArgumentParser()
    
    # add required argument
    parser.add_argument("url", help="The url you wish to connect to.", type=str)
    
    # add optional argument
    parser.add_argument("-m", "--method", help="The request method you wish to use. The default is 'GET'", type=str)
    
    args = parser.parse_args()
    url = args.url
    method = args.method if args.method else 'GET'
    result = send_get(url, method)

    print(result)


if __name__ == "__main__":
    main()