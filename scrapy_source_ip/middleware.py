class HttpIpBindMiddleware(object):
    def __init__(self, ip_bind, **kwargs):
        self.ip_bind = ip_bind

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get(
            	'BIND_IP_ADDRESS',
		('0.0.0.0', 0)
	    ),
        )

    def process_request(self, request, spider):
	request.meta['bindaddress'] = self.ip_bind
