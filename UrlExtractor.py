from UrlValidator import UrlValidator


class UrlExtractor(UrlValidator):
    def __init__(self,
                 url):
        self.url = self.__sanitize(url)
        self.__validate()
        super().__init__(self.url)

    @staticmethod
    def __sanitize(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def __validate(self):
        if not self.url:
            raise ValueError("Invalid URL")

    @property
    def base_url(self):
        return self.url_pattern()

    def url_parameter(self,
                      value):
        return self.parameter_pattern(value)

    def url_value(self, value):
        return self.value_pattern(value)

    def __str__(self):
        return str(self.url)
