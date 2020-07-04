#!/usr/bin/env pyton
#_*_ conding: utf8 _*_
#Author: Pedro Estévez

import requests
import sys
import json
import time

siteID = sys.argv[1]
url= "https://api.mercadolibre.com/sites/"+siteID+"/search?seller_id="
clientsID = []
sellers = len(sys.argv)-1
position = 2
archive = open("log-"+time.strftime("%d%m%Y-%H_%M")+".txt","w")
while (sellers >= position):
	fullUrl = url + sys.argv[position]
	position = position + 1 
	request = requests.get(fullUrl)
	result = json.loads(request.text)
	archive.write("*******************************************************************************\n")
	archive.write("Seller ID: {}\n".format(result['seller']['id']))
	archive.write("*******************************************************************************\n")
	for item in result['results']:
		archive.write("Item ID: {}\n".format(item['id']))
		archive.write("Item Title: {}\n".format(item['title']))
		archive.write("Category ID: {}\n".format(item['category_id']))
		archive.write("Category ID: {}\n".format(item['domain_id']))
		archive.write("---------------------------------------------------------------------------\n")
archive.close()
