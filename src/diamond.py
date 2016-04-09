import requests, json

GET_PRICE_ENDPOINT = "https://technet.rapaport.com:449/HTTP/JSON/Prices/GetPrice.aspx"

class Diamond(object):
	"""
	Represents a type of diamond, for which price information is to
	be retrieved from the TechNet API.
	"""

	def __init__(self):
		self.shape = None
		self.size = None
		self.color = None
		self.clarity = None

	def set_shape(self, shape):
		self.shape = shape

	def set_size(self, size):
		self.size = size

	def set_color(self, color):
		self.color = color

	def set_clarity(self, clarity):
		self.clarity = clarity

	def _get_body(self):
		attributes = {}
		if (self.shape): attributes["shape"] = self.shape
		if (self.size): attributes["size"] = self.size
		if (self.color): attributes["color"] = self.color
		if (self.clarity): attributes["clarity"] = self.clarity
		return attributes

	def get_carat_price(self, username, password):
		header_json = {"username": username, "password": password}
		request_json = {
			"request": {
				"header": header_json,
				"body": self._get_body()
			}
		} 

		headers = {
			"Content-Type": "application/x-www-form-urlencoded"
		}

		r = requests.post(GET_PRICE_ENDPOINT, headers=headers, data=json.dumps(request_json))

		return r.json()["response"]["body"]["caratprice"]





