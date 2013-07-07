from scrapy import log

class HttpIpBindMiddleware(object):
    def __init__(self, ip_bind, **kwargs):
        self.ip_bind = ip_bind

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get(
            	'BIND_IP_ADDRESS',
		None
	    ),
            logger=lambda message: log.msg(message),
        )

    def process_request(self, request, spider):
	request.meta['bind_address'] = self.ip_bind
