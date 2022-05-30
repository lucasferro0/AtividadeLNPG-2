class Conta():
    def __init__(self, titular, banco, agencia):
        self.banco = banco
        self.ag = agencia
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print(f"Não é possível depositar um valor negativo na conta do {self.titular}.")
    
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saldo restante do {self.titular} é de: {self.saldo}.")
                return True
            else:
                print(f"Saldo de {self.titular} insuficiente.")
                return False
        else:
            print("Digite um valor positivo para sacar da conta.")
    
    def transferir(self, conta, valor):
        if self.sacar(valor):
            conta.depositar(valor)


Conta1 = Conta("Lucas", "Nubank", "001")

Conta2 = Conta("Sônia", "Caixa", "0055")

Conta1.depositar(200)
Conta2.depositar(700)


Conta2.transferir(Conta1, 200)

Conta1.sacar(400)

print(Conta1.saldo)
print(Conta2.saldo)