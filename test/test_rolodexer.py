#!/usr/bin/env python

import unittest
import rolodexer

sample_input = """
Booker T., Washington, 87360, 373 781 7380, yellow
Chandler, Kerri, (623)-668-9293, pink, 123123121
James Murphy, yellow, 83880, 018 154 6474
asdfawefawea
""".strip()

sample_output = u"""
{
  "entries": [
    {
      "color": "yellow",
      "firstname": "James",
      "lastname": "Murphy",
      "phonenumber": "018-154-6474",
      "zipcode": "83880"
    },
    {
      "color": "yellow",
      "firstname": "Booker T.",
      "lastname": "Washington",
      "phonenumber": "373-781-7380",
      "zipcode": "87360"
    }
  ],
  "errors": [
    1,
    3
  ]
}
""".strip()

class RolodexerTests(unittest.TestCase):
    
    def test_tokenize(self):
        # all of these should tokenize (even with invalid individual terms)
        line0 = 'Booker T., Washington, 87360, 373 781 7380, yellow'
        line1 = 'Chandler, Kerri, (623)-668-9293, pink, 123123121'
        line2 = 'James Murphy, yellow, 83880, 018 154 6474'
        
        terms0 = rolodexer.tokenize(line0)
        terms1 = rolodexer.tokenize(line1)
        terms2 = rolodexer.tokenize(line2)
        
        self.assertEqual(len(terms0), 5)
        self.assertEqual(len(terms1), 5)
        self.assertEqual(len(terms2), 4) # first/last are single term
    
    def test_identify_color(self):
        self.assertTrue(rolodexer.is_color('yellow'))
        self.assertTrue(rolodexer.is_color('pink'))
        self.assertTrue(rolodexer.is_color('aqua marine'))
        
        self.assertFalse(rolodexer.is_color('Booker T.'))
        self.assertFalse(rolodexer.is_color('Washington'))
        self.assertFalse(rolodexer.is_color('Chandler'))
        self.assertFalse(rolodexer.is_color('Kerri'))
        self.assertFalse(rolodexer.is_color('James'))
        self.assertFalse(rolodexer.is_color('Murphy'))
        self.assertFalse(rolodexer.is_color('87360'))
        self.assertFalse(rolodexer.is_color('373 781 7380'))
        self.assertFalse(rolodexer.is_color('(623)-668-9293'))
        self.assertFalse(rolodexer.is_color('123123121'))
        self.assertFalse(rolodexer.is_color('83880'))
        self.assertFalse(rolodexer.is_color('018 154 6474'))
    
    def test_identify_phone(self):
        self.assertTrue(rolodexer.is_phone('373 781 7380'))
        self.assertTrue(rolodexer.is_phone('(623)-668-9293'))
        self.assertTrue(rolodexer.is_phone('018 154 6474'))
        
        # this should (problematically) read as a phone number
        # self.assertTrue(rolodexer.is_phone('123123121'))
        
        self.assertFalse(rolodexer.is_phone('Booker T.'))
        self.assertFalse(rolodexer.is_phone('Washington'))
        self.assertFalse(rolodexer.is_phone('Chandler'))
        self.assertFalse(rolodexer.is_phone('Kerri'))
        self.assertFalse(rolodexer.is_phone('James'))
        self.assertFalse(rolodexer.is_phone('Murphy'))
        self.assertFalse(rolodexer.is_phone('87360'))
        self.assertFalse(rolodexer.is_phone('83880'))
        self.assertFalse(rolodexer.is_phone('yellow'))
        self.assertFalse(rolodexer.is_phone('pink'))
        self.assertFalse(rolodexer.is_phone('aqua marine'))
    
    def test_identify_zip(self):
        self.assertTrue(rolodexer.is_zip('83880'))
        self.assertTrue(rolodexer.is_zip('87360'))
        # self.assertTrue(rolodexer.is_zip('02459-1234'))
        
        self.assertFalse(rolodexer.is_zip('Booker T.'))
        self.assertFalse(rolodexer.is_zip('Washington'))
        self.assertFalse(rolodexer.is_zip('Chandler'))
        self.assertFalse(rolodexer.is_zip('Kerri'))
        self.assertFalse(rolodexer.is_zip('James'))
        self.assertFalse(rolodexer.is_zip('Murphy'))
        self.assertFalse(rolodexer.is_zip('pink'))
        self.assertFalse(rolodexer.is_zip('aqua marine'))
        self.assertFalse(rolodexer.is_zip('373 781 7380'))
        self.assertFalse(rolodexer.is_zip('(623)-668-9293'))
        self.assertFalse(rolodexer.is_zip('123123121'))
        self.assertFalse(rolodexer.is_zip('yellow'))
        self.assertFalse(rolodexer.is_zip('018 154 6474'))
    
    def test_classify(self):
        terms = [
            'yellow', '373 781 7380', '87360',
            'Washington', 'Booker T.']
        
        out = rolodexer.classify(terms)
        keys = out.keys()
        
        self.assertTrue('phonenumber' in keys)
        self.assertTrue('firstname' in keys)
        self.assertTrue('lastname' in keys)
        self.assertTrue('color' in keys)
        self.assertTrue('zipcode' in keys)
        
        self.assertEqual(out['color'],          terms[0])
        self.assertEqual(out['phonenumber'],    rolodexer.phone_format(terms[1]))
        self.assertEqual(out['zipcode'],        terms[2])
        self.assertEqual(out['lastname'],       terms[3])
        self.assertEqual(out['firstname'],      terms[4])
    
    def test_tokenize_classify(self):
        pass
    
    def test_json_format(self):
        pass

if __name__ == '__main__':
    unittest.main()

if __name__ == '__yodogg__':
    line = sample_input.splitlines()[0]
    
    while True:
        partition   = line.rpartition(',')
        first       = partition[:-2][0].strip()
        last        = partition[-1:][0].strip()
        if not first and not last:
            break
        line = first
        print last
