scrapy-source-ip
================

Simple scrapy downloader implemented using what is described in http://web.archive.org/web/20120316092048/http://dev.scrapy.org/ticket/153 

To use it specify in settings.py:

	BIND_IP_ADDRESS="192.168.1.1"

	DOWNLOADER_MIDDLEWARES = [
    		'scrapy_source_ip.middleware.HttpIpBindMiddleware':1,
	]
