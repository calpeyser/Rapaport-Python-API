from diamond import Diamond
import json, os

def _get_simple_diamond():
	d = Diamond()
	d.set_shape("round")
	d.set_size(2.10)
	d.set_color("E")
	d.set_clarity("VS2")
	return d

# To run this test, set USERNAME and PASSWORD as environment variables.
def test_simple_diamond():
	d = _get_simple_diamond()
	username = os.environ["USERNAME"]
	password = os.environ["PASSWORD"]
	price = d.get_carat_price(username, password)
	if isinstance(price, int): return True
	return False

if __name__ == "__main__":
	print "test_simple_diamond: " + str(test_simple_diamond())