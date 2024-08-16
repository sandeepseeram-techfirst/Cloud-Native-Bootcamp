import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash
        self.nonce = nonce
 
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
 
def calculate_hash(block):
    value = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.transactions) + str(block.nonce)
    return hashlib.sha256(value.encode(’utf-8’)).hexdigest()
 
def create_genesis_block():
    transactions = [Transaction("genesis", "genesis", 0)]
    return Block(0, “0”, int(time.time()), transactions, calculate_hash(Block(0, "0", int(time.time()), transactions, 0, 0)), 0)
  
def proof_of_work(previous_block, transactions):
    nonce = 0
    while True:
        new_block = Block(previous_block.index + 1,
                          previous_block.hash,
                          int(time.time()),
                          transactions,
                          calculate_hash(Block(previous_block.index + 1, previous_block.hash, int(time.time()), transactions, previous_block.hash, nonce)),
                          nonce)
        if new_block.hash[:4] == "0000":  # Adjust the number of leading zeros for different difficulty
            return new_block
        nonce += 1
 
def is_valid_transaction(transaction):
    # Simplified validation: amount should be positive
    return transaction.amount> 0
 
# Create blockchain and add genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
 
# Dummy transactions
transactions = [Transaction("Alice", "Bob", 50), Transaction("Bob", "Charlie", 25)]
 
# Add blocks to the chain
for i in range(10):
    if all([is_valid_transaction(tx) for tx in transactions]):
        new_block = proof_of_work(previous_block, transactions)
        blockchain.append(new_block) 
        previous_block = new_block 
        print(f"Block #{new_block.index} has been added to the blockchain!")
        print(f"Hash: {new_block.hash}\n")
    else:
        print("Invalid transactions")
