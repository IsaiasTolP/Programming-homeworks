from __future__ import annotations

"""Manipulación de IPs en hosts sobre redes de ordenadores"""


class Host:
    IPV4_BITS = 32
    # ↓ Contiene: [0, 8, 16, 24, 32]
    IPV4_SLICES = list(range(0, IPV4_BITS + 1, 8))
    IPV4_BYTES = 4
    DEFAULT_IP_BYTE = 0
    MAX_SLICE_SIZE = 255
    IP_CLASSES = ('A', 'B', 'C')

    def __init__(self, *args: str | int, mask: int):
        """
        Constructor de un Host
        ======================
        - Si el primer argumento de args es un string, se supondrá que es una IP en formato
          de cadena de texto. Ejemplo: '192.168.1.5'
        - Si args es una tupla indica que vienen una serie de octetos de la dirección. Se
          rellenarán los octetos faltantes (si es que faltan) con ceros.
            + Ejemplo completo: (192, 168, 1, 5)
            + Ejemplo incompleto: (192, 168) habrá que rellenar → (192, 168, 0, 0)
        - Si la máscara está fuera de rango habrá que elevar una excepción de dirección IP
          indicando en el mensaje: "Mask is out of range". Ejemplo: mask=33
        - Si nos pasan un número de octetos distinto de 4, habrá que elevar una excepción de
          dirección IP con el mensaje: "Only 4 octets are allowed"
        - Hay que crear los atributos "ip_octets" (tupla) y mask (entero).
          Ejemplo:
            - ip_octets = (192, 168, 1, 5)
            - mask = 24
        """
        if isinstance(args[0], str):
            args = tuple(int(arg) for arg in args[0].split('.'))
        if isinstance(args, tuple):
            args_length = len(args)
            if args_length == Host.IPV4_BYTES:
                ip_octets = args
            elif args_length < Host.IPV4_BYTES:
                blank_spaces = Host.IPV4_BYTES - args_length
                new_args = list(args) + [Host.DEFAULT_IP_BYTE for _ in range(blank_spaces)]
                ip_octets = tuple(new_args)
            else:
                raise IPAddressError('Only 4 octets are allowed')
        self.ip_octets = ip_octets

        if mask >= 0 and mask <= Host.IPV4_BITS:
            self.mask = mask
        else:
            raise IPAddressError('Mask is out of range')

    @property
    def ip(self) -> str:
        '''Devuelve la IP del host en formato string.
        Ejemplo: "192.168.1.5"'''
        return '.'.join(str(octet) for octet in self.ip_octets)

    @property
    def bip(self) -> str:
        '''Devuelve la IP en formato binario. Ojo que cada octeto debe tener 8 bits.
        Ejemplo: "11000000101010000000000100000101"'''
        return ''.join(f'{octet:08b}' for octet in self.ip_octets)

    @property
    def addr_bmask(self) -> str:
        """Devuelve la parte de la dirección que representa la máscara (en binario).
        Ejemplo: "110000001010100000000001"
        Haz uso de la property "bip" definida anteriormente."""
        return self.bip[: self.mask]

    @property
    def addr_bhost(self) -> str:
        """Devuelve la parte de la dirección que representa el host (en binario).
        Ejemplo: "00000101"
        Haz uso de la property "bip" definida anteriormente."""
        return self.bip[self.mask :]

    @property
    def has_network_addr(self) -> bool:
        """Indica si la dirección IP corresponde con la dirección de red.
        En una dirección de red, la parte de host de la IP tiene todos los bits a 0.
        Ejemplo: "192.168.1.0"
        Haz uso de la property "addr_bhost" definida anteriormente."""
        return self.addr_bhost == '0' * len(self.addr_bhost)

    @property
    def has_broadcast_addr(self) -> bool:
        """Indica si la dirección IP corresponde con la dirección de broadcast.
        En una dirección de broadcast, la parte de host de la IP tiene todos los bits a 1.
        Ejemplo: "192.168.1.255"
        Haz uso de la property "addr_bhost" definida anteriormente."""
        return self.addr_bhost == '1' * len(self.addr_bhost)

    @property
    def nclass(self) -> str:
        """Devuelve la clase de la red: A, B o C.
        → Ver https://bit.ly/42Pgm2k
        Haz uso de IPV4_SLICES definido anteriormente."""
        for idx in range(len(Host.IP_CLASSES)):
            if len(self.addr_bmask) <= Host.IPV4_SLICES[idx + 1]:
                return Host.IP_CLASSES[idx]
        return Host.IP_CLASSES[-1]

    @property
    def addr_host_size(self) -> int:
        """Devuelve el número de bits que ocupa la parte de host en la dirección"""
        return len(self.addr_bhost)

    @property
    def num_hosts(self) -> int:
        """Devuelve el número de hosts que pueden haber en la red.
        Para calcular la cantidad de hosts por red, se usa la fórmula 2^n - 2
        donde n corresponde a la cantidad de bits para hosts."""
        return 2**self.addr_host_size - 2

    def ping(self, host: Host) -> bool:
        """Indica si un host puede hacer ping a otro host.
        Para que dos hosts puedan hacer ping deben estar en la misma red."""
        return self.addr_bmask == host.addr_bmask

    def __repr__(self):
        '''Devuelve la representación del host en formato IP/Máscara.
        Ejemplo: "192.168.1.5/24"'''
        return f'{self.ip}/{self.mask}'

    @classmethod
    def from_bip(cls, bip: str, mask: int) -> Host:
        """Crea un host a partir de una dirección IP binaria y una máscara.
        - Por ejemplo: bip='10010100101000111101010101110101' y mask=8 debería crear el host:
          148.163.213.117/8
        - Si se pasan más de 32 bits hay que lanzar una excepción de dirección incorrecta
          indicando en el mensaje: "Binary address is too long"
        """
        if len(bip) > cls.IPV4_BITS:
            raise IPAddressError('Binary address is too long')
        new_ip = [
            int(bip[cls.IPV4_SLICES[idx] : cls.IPV4_SLICES[idx + 1]], base=2)
            for idx in range(len(cls.IPV4_SLICES) - 1)
        ]
        return cls(*new_ip, mask=mask)

    def __iter__(self):
        """Iterador del Host COMO FUNCIÓN GENERADORA.
        Debe devolver todos los hosts de la subred especificada por el propio host.
        Por ejemplo, para 192.168.1.45/24, habría que devolver OBJETOS DE TIPO HOST tal que:
            192.168.1.1/24
            192.168.1.2/24
            ...
            192.168.1.254/25
        Se debe hacer uso del método from_bip() definido anteriormente."""
        for i in range(1, self.num_hosts + 1):
            addr_bhost = f'{i:0{self.addr_host_size}b}'
            bip = self.addr_bmask + addr_bhost
            yield Host.from_bip(bip, self.mask)

    def __add__(self, other: Host) -> Host:
        """Suma dos objetos de tipo Host.
        El host resultante tendrá:
        - Como "IP" la suma de cada octeto correspondiente (primero con primero, segundo con segundo, etc.).
        Si la suma del octeto sobrepasa 255 se pondrá 255.
        - Como "máscara" la suma de las máscaras. Si la máscara sobrepasa 32 se pondrá 32."""
        new_ip_octects = []
        for octet1, octet2 in zip(self.ip_octets, other.ip_octets):
            new_octect = octet1 + octet2
            if new_octect > Host.MAX_SLICE_SIZE:
                new_octect = Host.MAX_SLICE_SIZE
            new_ip_octects.append(new_octect)

        new_mask = self.mask + other.mask
        if new_mask > Host.IPV4_BITS:
            new_mask = 32
        return Host(*new_ip_octects, mask=new_mask)


class IPAddressError(Exception):
    """Clase que representa un error en la dirección IP.
    - Mensaje por defecto: IP address is invalid
    - Si pasamos un mensaje: IP address is invalid: <message>"""

    BASE_MSG = 'IP address is invalid'

    def __init__(self, message: str = ''):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        if self.message:
            return f'{IPAddressError.BASE_MSG}: {self.message}'
        else:
            return IPAddressError.BASE_MSG
