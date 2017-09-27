#!/opt/opensvc/bin/python

import xml.etree.ElementTree as xmllib
import re
import urllib2
import logging
import zipfile
import os.path
import os
from pprint import pprint

def get_rame_number_from_zip(zip_file) :
	# creating tmp dir to uncompress zip file
	if not os.path.exists(DIR_TMP):
		os.makedirs(DIR_TMP)
	zfile = zipfile.ZipFile(zip_file)
	for name in zfile.namelist():
		(dirname, filename) = os.path.split(name)
		print "Decompressing " + filename + " on " + dirname
		zfile.extract(name, DIR_TMP)
		rame_num = get_rame_number_from_xml(DIR_TMP + '/' + name)
		os.remove(DIR_TMP + '/' + name)
		return rame_num

def get_rame_number_from_xml(xml_file) :
	root = xmllib.parse(xml_file).getroot()
	# for child in root:
	str = root[0].get('message')
	rame_num = re.findall(r'\d+', str)[0]
	return rame_num;

def read_webpage(url):
	response = urllib2.urlopen(url)
	html = response.read()
        links = re.findall(r'href=[\'"]?([^\'" >]+)', html)
        good_links = []
        for link in links :
                if  (link.lower().startswith('vb2n') or link.lower().startswith('z2n')) and link.lower().endswith('.zip'):
                        good_links.append(link)
       
        return good_links



# variables
# SERVER_URL = "https://pscs-wi-prd.dsit.sncf.fr/cluster/pscs/files/"
SERVER_URL = "http://127.0.0.1/webpage.html"


# logging.basicConfig(filename='recup_2n.log',level=logging.DEBUG)
# logging.info("START")
DIR_IN =  "/home/moesoe/scripts/test"
DIR_TMP = '/home/moesoe/scripts/test/tmp'
# ZIP_FILE = 'vb2n_sive_jdb_151118-205407_7604.xml.zip'
ZIP_FILE = 'z2n_sive_jdb_151117-131306_186.xml.zip'

links = read_webpage(SERVER_URL)
# rame_num = get_rame_number_from_zip(DIR_IN  + '/' + ZIP_FILE)
# print rame_num
# logging.info("END")
