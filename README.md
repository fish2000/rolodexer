Rolodexer
=========

A parser for “rolodex” data, in the following form:

    Booker T., Washington, 87360, 373 781 7380, yellow
    Chandler, Kerri, (623)-668-9293, pink, 123123121
    James Murphy, yellow, 83880, 018 154 6474

The `rolodexer INFILE.in` command will transform contact data
thusly formatted into normalized JSON output, á la:

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

By default, Rolodexer’s output goes to STDOUT; specify an output file like so:

    $ rolodexer INFILE.in -o result.out

Install
-------

Install with Pip, via PyPI:

    $ pip install -U rolodexer

… Or via GitHub:

    $ git clone https://github.com/fish2000/rolodexer.git
    $ cd rolodexer
    $ pip install -U -r requirements.txt
    $ pip install -U .

Questions?
----------

Contact me, I welcome all inquiries: fish2000, at the geemail, etc etc. I am also available for hire!
