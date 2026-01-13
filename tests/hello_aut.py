import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        browser = sys.argv[2] if len(sys.argv) > 2 else "firefox"   #(ambil browser dari matrix)
        server = "http://localhost:4444"                            #(alamat Selenium Hub)

        options = None
        if browser == "chrome":
            options = webdriver.ChromeOptions()
        elif browser == "edge":
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)                          #(tutup browser setelah test)

    def test_homepage(self):
        url = sys.argv[1] if len(sys.argv) > 1 else "http://docker-apache"  #(alamat AUT)
        self.browser.get(url)                                         #(buka AUT)
        expected = "Welcome back, Guest!"                             #(teks yang diharapkan)
        actual = self.browser.find_element(By.TAG_NAME, 'p').text     #(ambil isi <p>)
        self.browser.save_screenshot('ss.png')                #(ambil screenshot)
        self.assertIn(expected, actual)                               #(validasi hasil)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')
