import requests
import json
from optparse import OptionParser
import time

parser=OptionParser()
parser.add_option("--test",action="store_true",default=False,help="Run local tests")
(opts,args)=parser.parse_args()

if (opts.test):
    host = "localhost:8080"
    api_key = "09303c29b8b78bb7a77ea74086fc4604"
else:
    host = "api.reimaginebanking.com"
    api_key = "0f35e6aabd46897e9b0185a67a566d65"

print("Creating a new customer for testing")
#Parameter body
customer_call = {
    "first_name": "Jane",
    "last_name": "Doe",
    "address": {
        "street_number": "123",
        "street_name": "Made Up Street",
        "city": "SmallTown",
        "state": "MD",
        "zip": "22837"
    }
}
#POST request
r = requests.post('http://'+host+'/customers?key='+api_key, json=customer_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    customer_body = r.json()
    customer_id = customer_body[u'objectCreated'][u'_id']
    #Show customer's id
    print(json.dumps(customer_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not create customer" +'\n')



print("Creating a new account for the customer")
#Parameter body
customer_account_call = {
    "type": "Credit Card",
    "nickname": "For Saving",
    "rewards": 0,
    "balance": 100
}
#POST request
r = requests.post('http://'+host+'/customers/'+customer_id+'/accounts?key='+api_key, json=customer_account_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    customer_account_id = account_body[u'objectCreated'][u'_id']
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not create account"  +'\n')



print("Depositing money to account")
#Parameter body
deposit_call = {
    "medium": "balance",
    "transaction_date": "2017-11-06",
    "amount": 100
}
#POST request
r = requests.post('http://'+host+'/accounts/'+customer_account_id+'/deposits?key='+api_key, json=deposit_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not deposit money"  +'\n')


#Wait for deposit to go through
time.sleep(70)



print("Checking the credit card")
#GET request
r = requests.get('http://'+host+'/accounts/'+customer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')


print("Withdrawaling money from account")
#Parameter body
withdrawal_call = {
    "medium": "balance",
    "transaction_date": "2017-11-02",
    "amount": 12
}
#POST request
r = requests.post('http://'+host+'/accounts/'+customer_account_id+'/withdrawals?key='+api_key, json=withdrawal_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not withdrawal money"  +'\n')


#Wait for withdrawal to go through
time.sleep(70)


print("Checking the credit card")
#GET request
r = requests.get('http://'+host+'/accounts/'+customer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')



print("Creating a new account for a transfer")
#Parameter body
customer_account_call = {
    "type": "Savings",
    "nickname": "For transfers",
    "rewards": 0,
    "balance": 0
}
#POST request
r = requests.post('http://'+host+'/customers/'+customer_id+'/accounts?key='+api_key, json=customer_account_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    transfer_account_id = account_body[u'objectCreated'][u'_id']
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not create account"  +'\n')



print("Transferring money from account")
#Parameter body
transfer_call = {
    "medium": "balance",
    "payee_id": transfer_account_id,
    "amount": 30,
    "transaction_date": "2017-11-02"
}
#POST request
r = requests.post('http://'+host+'/accounts/'+customer_account_id+'/transfers?key='+api_key, json=transfer_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not transfer money"  +'\n')


#Wait for transfer to go through
time.sleep(70)


print("Checking the credit card")
#GET request
r = requests.get('http://'+host+'/accounts/'+customer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')


print("Checking the account the money went to")
#GET request
r = requests.get('http://'+host+'/accounts/'+transfer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')



print("Posting a bill money to the credit card")
#Parameter body
bill_call = {
    "status": "completed",
    "payee": "Spotify",
    "payment_date": "2017-11-09",
    "payment_amount": 15
}
#POST request
r = requests.post('http://'+host+'/accounts/'+customer_account_id+'/bills?key='+api_key, json=bill_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not post the bill"  +'\n')


#Wait for withdrawal to go through
time.sleep(70)


print("Checking the credit card")
#GET request
r = requests.get('http://'+host+'/accounts/'+customer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')



print("Making a purchase")
#Parameter body
purchase_call = {
    "merchant_id": "57cf75cea73e494d8675efa4",
    "medium": "balance",
    "purchase_date": "2017-11-09",
    "amount": 6
}
#POST request
r = requests.post('http://'+host+'/accounts/'+customer_account_id+'/purchases?key='+api_key, json=purchase_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not make the purchase"  +'\n')


#Wait for withdrawal to go through
time.sleep(70)


print("Checking the credit card")
#GET request
r = requests.get('http://'+host+'/accounts/'+customer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')



print("Making a loan on the account")
#Parameter body
loan_call = {
    "type": "home",
    "status": "approved",
    "credit_score": 687,
    "monthly_payment": 25,
    "amount": 100
}
#POST request
r = requests.post('http://'+host+'/accounts/'+customer_account_id+'/loans?key='+api_key, json=loan_call, headers={'content-type':'application/json'})
#Show the result of the POST
print("Result of the POST: " + str(r.status_code))
if r.status_code == 201:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not make the loan"  +'\n')


#Wait for withdrawal to go through
time.sleep(70)


print("Checking the credit card")
#GET request
r = requests.get('http://'+host+'/accounts/'+customer_account_id+'?key='+api_key, headers={'content-type':'application/json'})
#Show the result of the GET
print("Result of the GET: " + str(r.status_code))
if r.status_code == 200:
    #Result is good
    account_body = r.json()
    print(json.dumps(account_body, indent=4) + '\n')
else:
    #Result is not good
    print("Could not get the account"  +'\n')
