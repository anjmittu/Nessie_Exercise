import requests
import json

#Training criteria 2: Customer endpoint
print "Creating a new customer: Jimmy Page"
#Parameter body
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
#POST request
r = requests.post('http://api.reimaginebanking.com/customers?key=0f35e6aabd46897e9b0185a67a566d65', json=jimmy, headers={'content-type':'application/json'})
#Show the result of the POST
print "Result of the POST: " + str(r.status_code)
if r.status_code == 201:
    #Result is good
    jimmy_body = r.json()
    jimmy_id = jimmy_body[u'objectCreated'][u'_id']
    #Show Jimmy's id
    print "Jimmy's id is: " + jimmy_id +'\n'
else:
    #Result is not good
    print "Could not create customer" +'\n'



#Training criteria 2: Account endpoint
print "Creating a new account for Jimmy"
#Parameter body
jimmy_account_info = {
                        "type": "Savings",
                        "nickname": "Touring Cash",
                        "rewards": 400,
                        "balance": 9562
                    }
#POST request
r = requests.post('http://api.reimaginebanking.com/customers/'+jimmy_id+'/accounts?key=0f35e6aabd46897e9b0185a67a566d65', json=jimmy_account_info, headers={'content-type':'application/json'})
#Show the result of the POST
print "Result of the POST: " + str(r.status_code)
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    jimmy_account_id = account_body[u'objectCreated'][u'_id']
    print "Jimmy's account id is: " + jimmy_account_id +'\n'
else:
    #Result is not good
    print "Could not create account"  +'\n'



#Training criteria 2: Bills endpoint
print "Checking to see if Jimmy has any bills"
#GET request
r = requests.get('http://api.reimaginebanking.com/accounts/'+jimmy_account_id+'/bills?key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
#Show the result of the GET
print "Result of the GET: " + str(r.status_code)
if r.status_code == 200:
    #Result is good
    print "Jimmy has " + str(len(r.json())) + " bills" +'\n'
else:
    #Result is not good
    print "Could not get bills" +'\n'



#Training criteria 3: Purchase endpoint
print "Adding Jimmy's guitar purchase to his account"
#Need to make merchant POST first to get merchant ID
#Parameter body
guitar_store = {
                    "name": "Guitar Shop",
                    "category": [
                        "Music"
                    ]
                }
#POST request
r = requests.post('http://api.reimaginebanking.com/merchants?key=0f35e6aabd46897e9b0185a67a566d65', json=guitar_store, headers={'content-type':'application/json'})
if r.status_code == 201:
    #Result is good
    store_body = r.json()
    store_id = store_body[u'objectCreated'][u'_id']
    #Parameter body
    guitar_purchase = {
                        "merchant_id": store_id,
                        "medium": "balance",
                        "purchase_date": "2017-10-01",
                        "amount": 1234,
                        "description": "New guitar"
                    }
    #POST request
    r = requests.post('http://api.reimaginebanking.com/accounts/'+jimmy_account_id+'/purchases?key=0f35e6aabd46897e9b0185a67a566d65', json=guitar_purchase, headers={'content-type':'application/json'})
    #Show the result of the POST
    print "Result of the POST: " + str(r.status_code)
    if r.status_code == 201:
        #Result is good
        purchase_body = r.json()
        print purchase_body["message"]+'\n'
    else:
        #Result is not good
        print "Could not add the purchase" +'\n'
else:
    #Result is not good
    print "Could not add the purchase" +'\n'



#Training criteria 4: Money movement endpoint (deposit)
print "Depositing money into Jimmy's account"
#Parameter body
jimmy_deposit = {
                    "medium": "balance",
                    "transaction_date": "2017-09-23",
                    "amount": 674
                }
#POST request
r = requests.post('http://api.reimaginebanking.com/accounts/'+jimmy_account_id+'/deposits?key=0f35e6aabd46897e9b0185a67a566d65', json=jimmy_deposit, headers={'content-type':'application/json'})
#Show the result of the POST
print "Result of the POST: " + str(r.status_code)
if r.status_code == 201:
    #Result is good
    deposit_body = r.json()
    print deposit_body["message"]+'\n'
else:
    #Result is not good
    print "Could not add the deposit" +'\n'



#Training criteria 1: ATMs endpoint
print "Finding atms near by"
#GET request
r = requests.get('http://api.reimaginebanking.com/atms?lat=38.9283&lng=-77.1753&rad=10&key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
#Show the result of the GET
print "Result of the GET: " + str(r.status_code)
if r.status_code == 200:
    #result is good
    atm_body = r.json()
    print "Found " + str(len(atm_body["data"])) + " ATMs"
    print "Getting more ATMs ..."
    #next ATM GET request
    r = requests.get('http://api.reimaginebanking.com' + atm_body["paging"]["next"], headers={'content-type':'application/json'})
    #Show the result of the GET
    print "Result of the GET: " + str(r.status_code)
    if r.status_code == 200:
        #Result is good
        atm_body = r.json()
        print "Found " + str(len(atm_body["data"])) + " more ATMs"
        print "Getting more ATMs ..."
        #next ATM GET request
        r = requests.get('http://api.reimaginebanking.com' + atm_body["paging"]["next"], headers={'content-type':'application/json'})
        #Show the result of the GET
        print "Result of the GET: " + str(r.status_code)
        if r.status_code == 200:
            #Result is good
            atm_body = r.json()
            print "Found " + str(len(atm_body["data"])) + " more ATMs" +'\n'
        else:
            #Result is not good
            print "Could not get atms" +'\n'
    else:
        #Result is not good
        print "Could not get atms" +'\n'
else:
    #Result is not good
    print "Could not get atms" +'\n'



#Training criteria 5: Enterprise endpoint
print "Getting all accounts in the database"
#GET request
r = requests.get('http://api.reimaginebanking.com/enterprise/customers?key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
#Show the result of the GET
print "Result of the GET: " + str(r.status_code)
if r.status_code == 200:
    #Result is good
    customer_body = r.json()
    print "There are: " + str(len(customer_body["results"])) +' accounts\n'
else:
    #Result is not good
    print "Could not get customers" +'\n'



#Training criteria 6: DELETE request
print "Deleting all accounts"
#DELETE request
r = requests.delete('http://api.reimaginebanking.com/data?type=Accounts&key=0f35e6aabd46897e9b0185a67a566d65', headers={'content-type':'application/json'})
#Show the result of the DELETE
print "Result of the DELETE: " + str(r.status_code)
if r.status_code == 204:
    #Result is good
    print "Accounts deleted"
else:
    #Result is not good
    print "Could not delete" +'\n'
