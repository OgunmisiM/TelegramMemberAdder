# main.py
import sys
import os
from telethon.tl.types import InputPeerChannel
from scrape import scrape_users
from telegram_client import authenticate_client, fetch_dialogs
from add_members import add_members
import csv

API_ID = 1234567
API_HASH = 'XXXXXXXXXXXX'
PHONE = '+23481XXXXXXX'
SLEEP_INTERVAL_MIN = 60
SLEEP_INTERVAL_MAX = 180

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py members.csv")
        sys.exit(1)

    input_file = sys.argv[1]

    users = scrape_users(input_file)

    # Check if the output_file is provided as a command-line argument
    output_file = sys.argv[2] if len(sys.argv) >= 3 else 'output.csv'

    # If the output_file doesn't exist, create it and write headers
    if not os.path.isfile(output_file):
        with open(output_file, 'w', newline='', encoding='UTF-8') as csvfile:
            fieldnames = ['username', 'id', 'access_hash', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    client = authenticate_client(API_ID, API_HASH, PHONE)
    chats = fetch_dialogs(client)

    print('Choose a group to add members:')
    for i, group in enumerate(chats):
        print(f"{i} - {group.title}")

    g_index = input("Enter a Number: ")
    target_group = chats[int(g_index)]
    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    mode = int(input("Enter 1 to add by username or 2 to add by ID: "))

    add_members(client, target_group_entity, users, mode, SLEEP_INTERVAL_MIN, SLEEP_INTERVAL_MAX)

if __name__ == "__main__":
    main()
