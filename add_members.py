# add_members.py
import time
import random
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.types import InputPeerChannel, InputPeerUser
import sys
import traceback

def add_members(client, target_group_entity, users, mode, sleep_min, sleep_max):
    n = 0
    for user in users:
        n += 1
        if n % 50 == 0:
            time.sleep(random.randrange(sleep_min, sleep_max))

        try:
            print(f"Adding {user['id']}")
            user_to_add = (
                client.get_input_entity(user['username'])
                if mode == 1 and user['username']
                else InputPeerUser(user['id'], user['access_hash']) if mode == 2
                else sys.exit("Invalid Mode Selected. Please Try Again.")
            )
            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            print("Waiting for 60-180 Seconds...")
            time.sleep(random.randrange(sleep_min, sleep_max))

        except PeerFloodError:
            print("Getting Flood Error from Telegram. Script is stopping now. Please try again after some time.")
        except UserPrivacyRestrictedError:
            print("The user's privacy settings do not allow you to do this. Skipping.")
        except Exception as e:
            traceback.print_exc()
            print(f"Unexpected Error: {e}")
            continue
