# Rapaport-Python-API
This is a simple Python library for using the Rapaport TechNet API to retrieve prices of diamonds.

### Installation
To install, run the setup script:
```
python setup.py install
```

### Usage
To use the library, create an instance of the Diamond class and populate it appropriate attributes for your query.

```
from Rapaport.diamond import Diamond

d = Diamond()
d.set_shape("round")
d.set_size(2.10)
d.set_color("E")
d.set_clarity("VS2")
```

Then, invoke the `get_carat_price` method to obtain the carat price, passing in your username and password.

```
carat_price = d.get_carat_price(MY_USERNAME, MY_PASSWORD) 
```