import requests
import re


def redrect_url(target_url):
    responce = requests.get(target_url,allow_redirects=True)
    
    final_url = responce.url
    
    product_id = extract_product_id(final_url)
    
    return  final_url , product_id
    

def extract_product_id(target_url):
    match = re.search(r'/item/(\d+)\.html', target_url)
    return match.group(1) if match else None



