from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/pakddo/Development/tool/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://127.0.0.1:8000')

        # title & header
        self.assertIn ('Project', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Project', header_text)

        #add something
        inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a project item'
        # )

        inputbox.send_keys('Recommend Model Making')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Recommend Model Making' for row in rows),
        #     "No new item in table -- TEST TEXT:\n%s" % (
        #         table.text,
        #     )
        # )
        self.assertIn('1: Recommend Model Making', [row.text for row in rows])


        #add something
        inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a project item'
        # )

        inputbox.send_keys('Making service using Recommend Model')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Recommend Model Making', [row.text for row in rows])
        self.assertIn('2: Making service using Recommend Model', [row.text for row in rows])

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
