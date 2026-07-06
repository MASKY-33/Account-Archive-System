import json


account_holder = {"client_name" : "Zack,", "account_type" : "Saving"}

with open("account.json", "w") as file:
    json.dump(account_holder, file)