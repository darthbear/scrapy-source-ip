scrapy-source-ip
================

Simple scrapy downloader that implements what is described in http://web.archive.org/web/20120316092048/http://dev.scrapy.org/ticket/153 

It allows to bind a specific ip to requests used to crawl websites. So
for instance if you have 2 network interfaces you can specify a particular
one to use.

In settings.py:

	BIND_IP_ADDRESS=("192.168.1.1", 0)

	DOWNLOADER_MIDDLEWARES = {
    		'scrapy_source_ip.middleware.HttpIpBindMiddleware':1,
	}

The modified scrapy core files are in files, copy them to:

	$SCRAPY_HOME/core/downloader/handlers/http.py
	$SCRAPY_HOME/core/downloader/webclient.py

