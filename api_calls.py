import requests
import json

#POST to customers
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
r = requests.post('http://api.reimaginebanking.com/customers?key=0f35e6aabd46897e9b0185a67a566d65', json=jimmy, headers={'content-type':'application/json'})
print "Result of the POST: " + str(r.status_code)
customer_body = r.json()
jimmy_id = customer_body[u'objectCreated'][u'_id']
print "Jimmy's id is: " + jimmy_id +'\n'

#POST to account
print "Creating a new account for Jimmy"
jimmy_account_info = {
                        "type": "Savings",
                        "nickname": "Touring Cash",
                        "rewards": 400,
                        "balance": 9562
                    }
r = requests.post('http://api.reimaginebanking.com/customers/'+jimmy_id+'/accounts?key=0f35e6aabd46897e9b0185a67a566d65', json=jimmy_account_info, headers={'content-type':'application/json'})
print "Result of the POST: " + str(r.status_code)
account_body = r.json()
jimmy_account_id = account_body[u'objectCreated'][u'_id']
print "Jimmy's account id is: " + jimmy_account_id +'\n'
