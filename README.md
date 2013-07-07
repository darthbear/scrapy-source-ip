scrapy-source-ip
================

Simple scrapy downloader implemented using what is described in http://web.archive.org/web/20120316092048/http://dev.scrapy.org/ticket/153 

To use it specify in settings.py:

	BIND_IP_ADDRESS="192.168.1.1"

	ITEM_PIPELINES = [
	    'scrapy_ip_source.middleware.HttpIpBindMiddleware',
	]
