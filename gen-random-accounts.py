import base58
import os
import json

# Make 100k random addresses, they should never see any write
data = [base58.b58encode(os.urandom(32)).decode("utf8") for _ in range(100_000)]

with open("random-accounts.json", "w+") as f:
    json.dump(data, f)
