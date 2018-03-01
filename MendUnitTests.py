import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_MendUnitTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        path = os.getcwd()
        self.driver.get(path + "/Login.html")

    def tearDown(self):
        self.driver.close()

    def testGivenAStaticHTMLForm_WhenLandingOnThePageAndSearchingForElements_ThenAUsernamePasswordAndLoginButtonCanBeFound(self):
        driver = self.driver
        elemUser = driver.find_element_by_id("user")
        elemPass = driver.find_element_by_id("pass")
        btnLogin = driver.find_element_by_id("login")

    def testGivenAStaticHTMLForm_WhenLandingOnThePageAndSearchingForElements_ThenAExceptionIsThrown(self):
        with self.assertRaises(Exception) as context:
            driver = self.driver
            elemUser = driver.find_element_by_id("notFound")
            elemPass = driver.find_element_by_id("doesNotExist")
            btnLogin = driver.find_element_by_id("hiding")

    def testGivenAStaticHtmlForm_WhenLoggingInToLoginPage_ThenANewPageIsNavigatedToo(self):
        driver = self.driver
        elemUser = driver.find_element_by_id("user")
        elemPass = driver.find_element_by_id("pass")
        btnLogin = driver.find_element_by_id("login")
        elemUser.send_keys("Username")
        elemPass.send_keys("password")
        elemPass.send_keys(Keys.RETURN)
        newPage = driver.find_element_by_tag_name("html")
        assert newpage is not None

if __name__ == '__main__':
    unittest.main()
