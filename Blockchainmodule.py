import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset current data
        self.current_data = []
        self.chain.append(block)
        return block

    def new_data(self, sender, recipient, data):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'data': data,
        })

    @staticmethod
    def hash(block):
        # Hash a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]
