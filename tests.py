import unittest, apiconsume

url = "http://api.axfrcheck.com/api/domain/openssl.org"

class Test(unittest.TestCase):

    def test_raises_error_on_invalid_method(self):
        with self.assertRaises(ValueError):
            apiconsume.send_get(url, "invalid_method")

    def test_returns_error_on_invalid_url(self):
        result = apiconsume.send_get("url")
        self.assertTrue('error_code' in result)

    def test_returns_dict(self):
        result = apiconsume.send_get(url)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(apiconsume.send_get("url"), dict))
