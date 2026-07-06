# Account Archive System
This system manages a simple account record using a JSON file and logs deleted items into a text archive.
It demonstrates reading, updating, deleting JSON data, and writing logs to a file.

## Features
- Creates an account record in account.json
- Reads the JSON file and loads the stored data
- Deletes the account_type field from the JSON database
- Saves the updated data back to disk
- Logs the deletion action in archive.txt
- Reads and displays the archive log

## How to use
The system performs the following steps automatically:
- Create the JSON file with initial account data
- Load the data from the file
- Delete the account_type field
- Save the updated JSON
- Write a log entry to archive.txt
- Display the archive contents


## Learning Purpose
Practice with:
- JSON file handling (dump, load)
- deleting fields from a JSON database
- writing logs to a text file
- simple data‑management workflow
