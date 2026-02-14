import requests

from ss import *
import iop
import urls
from iop import IopClient, IopRequest
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()

appkey = os.getenv("Appkey")
appSecret = os.getenv("AppSecret")

endpoint =urls.url



def link_generate(target_url):
    
    client = iop.IopClient(endpoint, appkey ,appSecret)
    request = iop.IopRequest('aliexpress.affiliate.link.generate')
    request.add_api_param('ship_to_country', 'FR')
    request.add_api_param('app_signature', 'asdasdas')
    request.add_api_param('promotion_link_type', '0')
    request.add_api_param('source_values', target_url)
    request.add_api_param('tracking_id', 'default')
    request.add_api_param('v', '2.0')

    response = client.execute(request)
    data = response.body
    promotion_url = data["aliexpress_affiliate_link_generate_response"]["resp_result"]["result"]["promotion_links"]["promotion_link"][0]["promotion_link"]
    return promotion_url
    

    
    



def get_product_summary(product_id):
    client = iop.IopClient(endpoint, appkey ,appSecret)
    request = iop.IopRequest('aliexpress.affiliate.productdetail.get')
    request.add_api_param('app_signature', 'aaaaa')
    request.add_api_param('fields', 'commission_rate,sale_price')
    request.add_api_param('product_ids', product_id)
    request.add_api_param('target_currency', 'USD')
    request.add_api_param('target_language', 'EN')
    request.add_api_param('tracking_id', 'default')
    request.add_api_param('country', 'DZ')
    response = client.execute(request)
    #print(response.type)
    #print(response.body)
    data = response.body 
    products = data.get('aliexpress_affiliate_productdetail_get_response', {}) \
                       .get('resp_result', {}) \
                       .get('result', {}) \
                       .get('products', {}) \
                       .get('product', [])
    
    if products:
            item = products[0]
            
            # Extracting specific info
            title = item.get('product_title')
            commission = item.get('commission_rate')

            rating = item.get('evaluate_rate')
            promotion_link = item.get('promotion_link')
            target_price = item.get('target_app_sale_price')

            main_image = item.get('product_main_image_url')

             
            return title ,commission , rating, main_image,target_price,promotion_link
            



