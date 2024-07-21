from __future__ import annotations

class Network:
    IPV4_LENGTH = 4

    def __init__(self, *ip: int) -> None:
        self.ip = ip
        if not self.is_valid_ip():
            raise NewtworkError('Not valid IP')

    @staticmethod
    def msg_can_be_send(method):
        def wrapper(self, *args, **kwargs):
            all_args = list(args) + list(kwargs.values()) 
            for arg in all_args:
                if not isinstance(arg, str):
                    raise NewtworkError('''This message can't be send''')
            return method(self, *args, **kwargs)
        return wrapper

    def is_valid_ip(self) -> bool:
        return len([part for part in self if part >= 0 and part <= 255]) == Network.IPV4_LENGTH
    
    @msg_can_be_send
    def hello_world(self, msg: str) -> str:
        return f'Hello world {self}: {msg}'
    
    def __str__(self) -> str:
        return '.'.join(str(part) for part in self)

    def __len__(self) -> int:
        return len(self.ip)
    
    def __getitem__(self, idx: int):
        return self.ip[idx]
    
    def __iter__(self):
        return NetworkIterator(self)

class NetworkIterator:
    def __init__(self, network: Network) -> None:
        self.network = network
        self.pointer = 0

    def __next__(self):
        if self.pointer >= len(self.network):
            raise StopIteration
        else:
            item = self.network[self.pointer]
            self.pointer += 1
            return item
        
class NewtworkError(Exception):
    def __init__(self, msg: str='Newtwork Error') -> None:
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self) -> str:
        return f'There is an ERROR in Network: {self.msg}'
        
if __name__ == '__main__':
    network1 = Network(10, 5, 190, 132)
    print(network1[1])
    print(network1)
    print('Here are your parts')
    for item in network1:
        print(item)
    print(len(network1))
    print(network1.is_valid_ip())
    print(network1.hello_world('Matracazo'))

    network2 = Network(300, 40, 23, 18)