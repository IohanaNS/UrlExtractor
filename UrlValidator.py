import re

class UrlValidator:
    def __init__(self,
                 value):
        self.value = value

    def url_pattern(self):
        pattern = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/convert'
        )
        return pattern.match(self.value)[0] if not None else "Not a valid base url was found"

    def parameter_pattern(self, param):
        return re.search(f'({param})+', self.value)[0] if not None else "Given parameter was not found"

    def value_pattern(self, param):
        return re.search(f'(?<={param}=).*?(?=[&|.])',
                         self.value)[0] if not None else "Given parameter was not found"
