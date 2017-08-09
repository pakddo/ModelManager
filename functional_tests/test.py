from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/pakddo/Development/tool/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get(self.live_server_url)

        # title & header
        self.assertIn ('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #add something
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Recommend Model Making')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1. Recommend Model Making')

        #add something
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Making service using Recommend Model')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('2. Making service using Recommend Model')
        self.check_for_row_in_list_table('1. Recommend Model Making')

        self.fail('Finish the test!')
