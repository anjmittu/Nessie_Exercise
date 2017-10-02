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
if r.status_code == 201:
    jimmy_body = r.json()
    jimmy_id = jimmy_body[u'objectCreated'][u'_id']
    print "Jimmy's id is: " + jimmy_id +'\n'
else:
    print "Could not create customer" +'\n'

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
if r.status_code == 201:
    account_body = r.json()
    jimmy_account_id = account_body[u'objectCreated'][u'_id']
    print "Jimmy's account id is: " + jimmy_account_id +'\n'
else:
    print "Could not create account"  +'\n'

#GET to bills
print "Checking to see if Jimmy has any bills"
r = requests.get('http://api.reimaginebanking.com/accounts/'+jimmy_account_id+'/bills?key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
print "Result of the GET: " + str(r.status_code)
if r.status_code == 200:
    print "Jimmy has " + str(len(r.json())) + " bills" +'\n'
else:
    print "Could not get bills" +'\n'



#POST to merchants and purchases
print "Adding Jimmy's guitar purchase to his account"
guitar_store = {
                    "name": "Guitar Shop",
                    "category": [
                        "Music"
                    ]
                }
r = requests.post('http://api.reimaginebanking.com/merchants?key=0f35e6aabd46897e9b0185a67a566d65', json=guitar_store, headers={'content-type':'application/json'})
if r.status_code == 201:
    store_body = r.json()
    store_id = store_body[u'objectCreated'][u'_id']

    guitar_purchase = {
                        "merchant_id": store_id,
                        "medium": "balance",
                        "purchase_date": "2017-10-01",
                        "amount": 1234,
                        "description": "New guitar"
                    }
    r = requests.post('http://api.reimaginebanking.com/accounts/'+jimmy_account_id+'/purchases?key=0f35e6aabd46897e9b0185a67a566d65', json=guitar_purchase, headers={'content-type':'application/json'})
    print "Result of the POST: " + str(r.status_code)
    if r.status_code == 201:
        purchase_body = r.json()
        print purchase_body["message"]+'\n'
    else:
        print "Could not add the purchase" +'\n'
else:
    print "Could not add the purchase" +'\n'

#POST to deposit
print "Depositing money into Jimmy's account"
jimmy_deposit = {
                    "medium": "balance",
                    "transaction_date": "2017-09-23",
                    "amount": 674
                }
r = requests.post('http://api.reimaginebanking.com/accounts/'+jimmy_account_id+'/deposits?key=0f35e6aabd46897e9b0185a67a566d65', json=jimmy_deposit, headers={'content-type':'application/json'})
print "Result of the POST: " + str(r.status_code)
if r.status_code == 201:
    deposit_body = r.json()
    print deposit_body["message"]+'\n'
else:
    print "Could not add the deposit" +'\n'

#GET to enterprise customers
print "Getting all accounts in the database"
r = requests.get('http://api.reimaginebanking.com/enterprise/customers?key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
print "Result of the GET: " + str(r.status_code)
if r.status_code == 200:
    customer_body = r.json()
    print "There are: " + str(len(customer_body["results"])) +' accounts\n'
else:
    print "Could not get customers" +'\n'

#DELETE all accounts
print "Deleting all accounts"
r = requests.delete('http://api.reimaginebanking.com/data?type=Accounts&key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
print "Result of the DELETE: " + str(r.status_code)
if r.status_code == 204:
    print "Deleted"
else:
    print "Could not delete" +'\n'
