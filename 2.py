class bankAccount:

    def __init__(self, numberOfAccount, ownerName, balance):
        self.numberOfAccount = numberOfAccount
        self.ownerName = ownerName
        self.balance = balance

    def withdrawMoney(currentBalance, ammountMoney):
        return (currentBalance-ammountMoney)

    def putMoney(currentBalance, ammountMoney):
        return (currentBalance + ammountMoney)

Client1 = bankAccount(numberOfAccount=1589632,ownerName="Tomas",balance=110.58)
Client2 = bankAccount(numberOfAccount=9586214,ownerName="Alex",balance=1158.63)
Client3 = bankAccount(numberOfAccount=8365147,ownerName="Bob",balance=598.41)

print(f"Client name: {Client1.ownerName}; account number: {Client1.numberOfAccount}; balance: {Client1.balance}")
print(f"{Client1.ownerName} withdraw 50$ from his account and now his account: {bankAccount.withdrawMoney(Client1.balance, 50)}")
print(f"{Client1.ownerName} put 800$ from his account and now his account: {bankAccount.putMoney(Client1.balance, 800)}")