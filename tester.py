# coding: utf-8

import unittest
import converter

class El2enTester(unittest.TestCase):
  def setUp(self):
    self.converter = converter.Converter()
    
  def tearDown(self):
    pass
    
  def test_el_to_en_simple(self):
    self.assertEqual(u'this is my game', self.converter.toggle_layout(u'τηισ ισ μυ γαμε'), 'wrong convertion to small english')
    
  def test_el_to_en_caps_simple(self):
    self.assertEqual(u'THIS is MY game', self.converter.toggle_layout(u'ΤΗΙΣ ισ ΜΥ γαμε'), 'wrong convertion to caps/small english')
  
  def test_en_to_el_simple(self):
    self.assertEqual(u'αυτο ειναι το παιχνιδι μου', self.converter.toggle_layout(u'ayto einai to paixnidi moy'), 'wrong convertion small to greek')
    
  def test_en_to_el_simple(self):
    self.assertEqual(u'ΑΥΤΟ ειναι ΤΟ παιχνιδι ΜΟΥ', self.converter.toggle_layout(u'AYTO einai TO paixnidi MOY'), 'wrong convertion small to greek')
  
  def test_el_and_en_complex(self):
     self.assertEqual(u'this is my game, και αυτο ειναι το δικο σου', self.converter.toggle_layout(u'τηισ ισ μυ γαμε, kai ayto einai to diko soy'), 'wrong convertion to english/greek')
     
  def test_el_with_accent(self):
    self.assertEqual(u'αυτό είναι το παιχνίδι μου', self.converter.toggle_layout(u'ayt;o e;inai to paixn;idi moy'), 'wrong convertion to small english')
    
  #def test_en_to_el_complex(self):
  #  self.assertEqual('to_layout2', self.converter.toggle_layout("test"), 'complex wrong convertion to greek')
    
if __name__=='__main__':
  unittest.main()
