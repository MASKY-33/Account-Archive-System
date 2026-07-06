import json


with open("account.json", "r") as file:
    loaded_data = json.load(file)

del loaded_data["account_type"]

with open("account.json", "w") as file:
    json.dump(loaded_data, file)



with open("archive.txt", "a") as file:
    file.write("Account-item successfully deleted. \n")

with open("archive.txt", "r") as file:
    content = file.read()
print(content)