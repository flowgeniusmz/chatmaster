import requests

def make_request(vType, vURL, vHeaders: object = None, vBody: object = None):

    if vType == "Get":
        response = requests.get(
            url=vURL,
            headers=vHeaders
        )
        text = response.text
    elif vType == "Post": 
        response = requests.post(
            url=vURL,
            headers=vHeaders,
            json=vBody
        )
        text = response.text
    else:
        text = "Error"
    
    return text