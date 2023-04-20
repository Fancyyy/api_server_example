# server.py

from flask import Flask, jsonify
from flask import Response

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Light',
        'description': u'One of the most underrated prose writers demonstrates the literary firepower of science fiction at its best.'
    },
    {
        'id': 2,
        'title': u'The Siege',
        'description': u'The Levin family battle against starvation in this novel set during the German siege of Leningrad.'
    },
    {
        'id': 3,
        'title': u'A little Life',
        'description': u'This operatically harrowing American gay melodrama became an unlikely bestseller, and one of the most divisive novels of the century so far.'
    },
    {
        'id': 4,
        'title': u'Darkmans',
        'description': u'British fictions most anarchic author is as prolific as she is playful, but this freewheeling, visionary epic set around the Thames Gateway is her magnum opus.'
    }
]

book_soap = """
<?xml version="1.0"?>
<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
<soapenv:Header/>
<soapenv:Body>
   <book>
       <name>A little Life</name>
   </book>
   <book>
       <name>Darkmans</name>
   </book>
</cal:easter_date>
</soapenv:Body>
</soapenv:Envelope>
"""

book_xml = """
<?xml version="1.0"?>
<books>
  <book>
    <name>A little Life</name>
  </book>
  <book>
    <name>Darkmans</name>
  </book>
</books>
"""


@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id=None):
    if id < 5:
        return jsonify(books[id - 1])
    return jsonify(books)

@app.route('/api/books_soap', methods=['POST'])
def get_book_soap():
    return Response(book_soap, mimetype='application/soap+xml')

@app.route('/api/books_xml', methods=['GET'])
def get_book_xml():
    return Response(book_xml, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5000)
