import hashlib
import datetime


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash1(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )

        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash1()) + "\nBlock: " + str(self.blockNo)


class BlockChain:
    diff = 20
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    block = Block('Genesis')
    dummy = head = block

    def add(self, block):
        # adds the blocks and links them together

        block.previous_hash = self.block.hash1()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        # mines the blocks that were created

        for n in range(self.maxNonce):
            if int(block.hash1(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


block_chain = BlockChain()

for i in range(5):
    block_chain.mine(Block('Block' + str(i + 1)))

while block_chain.head is not None:
    print(block_chain.head)
    block_chain.head = block_chain.head.next
