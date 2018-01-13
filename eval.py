#!/usr/bin/env python3

import os,string,sys
import numpy as np
import matplotlib.pyplot as plt
import collections

def readFile(filePath):
	if(os.path.isfile(filePath)):
		f = open(filePath, 'r')
		content = f.read()
		f.close()
		return content
	else:
		return False

def writeFile(path,content):
	f = open(path,'w')
	f.write(content)
	f.close()

def autolabel(rects, plt):
	"""
	Attach a text label above each bar displaying its height
	"""
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x() + rect.get_width()/2., height,
				'%d' % int(height),
				ha='center', va='bottom')


def main():
	stats = {}
	cwd = os.getcwd()+"/data/"
	for dataFile in os.listdir(cwd):
		data = readFile(cwd+dataFile)
		month = (dataFile[7:9])
		year = (dataFile[9:13])
		stats[year+'-'+month] = {}
		
	cities = {}
	citiesApi = {}
	for dataFile in os.listdir(cwd):
		data = readFile(cwd+dataFile)
		month = (dataFile[7:9])
		year = (dataFile[9:13])
		data = data.split("BEGIN_SIDER ")
		data = data[1].split("\n")
		data = data[2:-1]
		for line in data:
			fields = line.split(" ")
			url = fields[0].split("/")
			if(len(url) > 5 and url[1] == "wordpress"):
				excludes = ['.git','',]
				city = url[2]
				lang = url[3]
				# check sanity with language flag, for example  en in .../en/..., always has length 2
				if(len(lang)!=2):
					continue
				# add city to result array if it appears for the first time
				if city not in citiesApi:
					citiesApi[city] = {}
				# lang appears for first time, initialize with 0
				if lang not in citiesApi[city]:
					citiesApi[city][lang] = {}
				if int(month) not in citiesApi[city][lang]:
					citiesApi[city][lang][int(month)] = 0
				#if(url[4] == "wp-json" and url[-1]=="pages"): #is api call
				path =  "/wordpress/%s/%s/wp-json/extensions/v0/modified_content/pages"%(city,lang)
				print(path)
				if(fields[0] == path):
					citiesApi[city][lang][int(month)] = citiesApi[city][lang][int(month)] + int(fields[1])
				elif(not fields[0].endswith(".php")):
					pass
	colors = {0:'red', 1:'lightblue',  2:'lightgreen', 3:'magenta', 4:'gold', 5:'darkred', 6:'darkblue', 7:'darkgreen',8:'lightgrey',9:'cyan'}
	print(citiesApi)
	for city in citiesApi:
		coordsApi = citiesApi[city]
		label = "API Aufrufe - %s" % city
		print(label)
		print(coordsApi)
		plt.title(label)
		counter = 0
		color = colors[counter]
		for lang in coordsApi:
			yApi = []
			xApi = []
			xlabel=[]
			for month in coordsApi[lang]:
				yApi.append(coordsApi[lang][month])
				xApi.append(float(month + counter * 0.1))
				xlabel.append(str(month))
			app = plt.bar(xApi, yApi,width=0.1,color=colors[counter],align='center',label=lang)
			counter = counter + 1
			if len(sys.argv) > 1 and sys.argv[1] == "1":
				autolabel(app, plt)
		plt.xticks(xApi, xlabel, rotation='horizontal')
		plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
		plt.savefig("images/%s.png"%city)
		plt.clf()
if __name__ == "__main__":
    main()
