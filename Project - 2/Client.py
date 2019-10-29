class Client:
    _clientId = 0  # int
    _name = ''  # str
    _address = ''  # str
    _balance = 0.0  # float

    def __init__(self, clientId, name, address):  # ini functions is to set default values
        self._clientId = clientId
        self._name = name
        self._address = address

    def clientId(self):  # self INT
        return self._clientId

    def name(self):  # get _name
        return self._name

    def address(self):  # get _address
        return self._address

    def address1(self):  # get _address
        return self._address

    def address(self, newValue):  # set new address
        self._address = newValue

    def balance(self):  # get _balance
        return self._balance

    def addPayment(self, amt):
        return amt  # return true if positive else negative

    def makePayment(self, amt):  # return true if addpayment is positive and subtract
        if addPayment(self, amt):  # true only
            self._balance -= amt
            return True
        # client is allowed to owe the company thus negative values is allowed.
        return False

    def __str__(self):
        # Id 123 Name: Janet Teo Address: 21 Tampines west Road Payment due: $0
        print('Id {:d} Name: {:s} Address: {:s} due: ${:.2f}'.format(
            self._clientId, self._name, self._address, self._balance))
        pass


test = Client(123, 'Janet Teo', '21 Tampines west Road')
test.__str__()
