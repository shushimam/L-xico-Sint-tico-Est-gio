from Lexico import lex  
from Sintatico import parser  

class Node:
    def __init__(self, token):
        self.token = token
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, token):
        if self.head is None:
            self.head = Node(token)
        else:
            current = self.head
            while current.next:
                if current.token.value == token.value:
                    return
                current = current.next
            if current.token.value != token.value:
                current.next = Node(token)

    def __iter__(self):
        current = self.head
        while current:
            yield current.token
            current = current.next

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def _hash(self, token_value):
        hash_value = hash(token_value)
        return hash_value % self.size

    def add_token(self, token):
        token_value = token.value
        hash_index = self._hash(token_value)
        self.table[hash_index].add(token)

    def print_tokens(self):
        print("Tokens armazenados na tabela hash:")
        for bucket in self.table:
            for token in bucket:
                print(token)

filename = "teste.txt"

with open(filename, 'r') as file:
    input_data = file.read()

lex.input(input_data)
tokens = []
hash_table = HashTable()

while True:
    token = lex.token()
    if not token:
        break
    tokens.append(token)
    hash_table.add_token(token)

token_string = " ".join([str(token.value) for token in tokens])

result = parser.parse(token_string)

print("Tokens reconhecidos:")
for token in tokens:
    print(token)

print("Resultado da análise sintática:", result)
