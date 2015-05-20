#!/usr/bin/env python

import unittest

from rolodexer import tokenize, classify

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
        pass
    
    def test_classify(self):
        terms = ['yellow', '373 781 7380', '87360', 'Washington', 'Booker T.']
    
    def test_json_format(self):
        pass

if __name__ == '__main__':
    line = sample_input.splitlines()[0]
    
    while True:
        partition   = line.rpartition(',')
        first       = partition[:-2][0].strip()
        last        = partition[-1:][0].strip()
        if not first and not last:
            break
        line = first
        print last
