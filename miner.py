import crypto_miner
from time import sleep

# Create a new crypto miner instance
miner = crypto_miner()

# Set the mining difficulty

miner.set_difficulty(10)

# Set the wallet address

miner.set_wallet_address("your_wallet_address")

# Generate a random block header

block_header = miner.generate_block_header()

block_header()

def find_block():
    nonce = 0
    while True:
        block = miner.create_block(block_header, nonce)
        if miner.validate_block(block):
            print(f"Block found: {block}")
            break
        nonce += 1
    return block

def mine():
    while True:
        block = find_block()
        miner.mine_block(block)
        print("Block mined!")
        block_header = miner.generate_block_header()
        print("New block header generated...")
        miner.update_block_reward(block)
        print("Block reward updated...")
        print("Waiting for next block...")
        sleep(1)
        block_header.update_block_reward(block)
        
if __name__ == "__main__":

    # Find and mine the block

    find_block()

    mine()
