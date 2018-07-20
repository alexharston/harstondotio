import unittest
import os
import time

class NewVisitorTest(LiveServerTestCase):

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        