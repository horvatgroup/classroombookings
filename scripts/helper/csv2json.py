#!/usr/bin/python3

import csv
from dataclasses import dataclass
import json

@dataclass
class User:
    username: str
    firstname: str
    lastname: str
    email: str
    password: str


if __name__ == "__main__":
    users = []
    with open('accounts.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            name, username, password, _, _, _, mail = row
            splited_name = name.split(" ")
            if len(splited_name) == 1:
                users.append(User(username, splited_name[0], "", mail, password))
            elif len(splited_name) == 2:
                users.append(User(username, splited_name[1], splited_name[0], mail, password))
            else:
                print(splited_name)
                first_name = input("first name: ")
                last_name = input("last name: ")
                users.append(User(username, first_name, last_name, mail, password))
    #with open("accounts.json", "w") as outfile: 
    #    json.dump([user.__dict__ for user in users], outfile)
    print(" ")
    for user in users:
        print(", ".join([user.username, user.firstname, user.lastname, user.email, user.password]))

