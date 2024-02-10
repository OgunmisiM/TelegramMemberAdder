# scrape.py
import csv

def scrape_users(input_file):
    users = []
    
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        
        for row in rows:
            user = {
                'username': row[0],
                'id': int(row[1]),
                'access_hash': int(row[2]),
                'name': row[3]
            }
            users.append(user)
    
    return users
