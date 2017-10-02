import requests
import json

print "Creating a new customer: Jimmy Page"
jimmy = {
        "first_name": "Jimmy",
        "last_name": "Page",
        "address": {
            "street_number": "123",
            "street_name": "Zeppelin Street",
            "city": "Misty Mountain",
            "state": "CA",
            "zip": "22102"
            }
        }
r = requests.post('http://api.reimaginebanking.com/customers?key=0f35e6aabd46897e9b0185a67a566d65', data=jimmy, headers={'content-type':'application/json'})
print "Result of the POST: " + str(r.status_code)
