from functional_tests import FunctionalTest, ROOT

class TestHomePage (FunctionalTest):

    def setUp(self):
      # Open browser and go to home page 
      self.url = ROOT + '/pitch/'
      get_browser = self.browser.get(self.url)
      
    def test_can_view_home_page(self):
        # Check if site loaded OK
        response_code = self.get_response_code(self.url)
        self.assertEqual(response_code, 200)

    def test_has_right_title(self):
        # Title has 'Microposts on Steriods'
        title = self.browser.find_element_by_tag_name('title')
        self.assertEqual('Microposts on Steroids', str(title.text))
        
