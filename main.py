from UrlExtractor import UrlExtractor
import re
url = "https://bytebank.com/convert?" \
      "currencyOrigin=real&" \
      "currencyDestiny=dollar&" \
      "quantity=100"
urlExtractor = UrlExtractor(url)
base_url = urlExtractor.base_url
currencyOrigin = urlExtractor.url_parameter("currencyOrigin")
value_given_parameter = urlExtractor.url_value(currencyOrigin)

print(base_url)
print(currencyOrigin)
print(value_given_parameter)
