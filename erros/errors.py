# Exceções da API
class FinanceException(Exception):
    def __init__(self, message_error,status_code):
        self.message_error = message_error
        self.status_code = status_code

class InsufficientFunds(FinanceException):
    def __init__(self,balance_ammout:float, withdrawal_amount:float):
       message = f"Saldo insuficiente. Seu saldo atual:{balance_ammout} é indiferente com o valor do seu saque :{withdrawal_amount}"
       super().__init__(message_error=message,status_code=400)

class IdNonExists(FinanceException):
    def __init__(self):
        message="Erro, o id não existe!!"
        super().__init__(message_error=message,status_code=404)

class NegativeBalance(FinanceException):
    def __init__(self,balance_value):
        message = f'Erro, o saldo está no vermelho: {balance_value}, logo a transação não pode ser realizada!!'
        super().__init__(message_error=message, status_code=400)

class CategoryNonExists(FinanceException):
    def __init__(self):
        message = "A categoria não está cadastrada!"
        super().__init__(message_error=message,status_code=404)

class AccountBlocked(FinanceException):
    def __init__(self):
        message = 'Conta bloqeuada! Não é possível utilizá-la no momento.'
        super().__init__(message_error=message,status_code=400)

class InvalidEmailLogin(FinanceException):
    def __init__(self):
        message = 'Credencial email inválido!! Verifique-o novamente'
        super().__init__(message_error=message, status_code=400)

class InvalidPassword(FinanceException):
    def __init__(self):
        message = 'Senha inválida!! Verifique o tamanho da senha e digite novamente'
        super().__init__(message_error=message, status_code=400)

class UserNotFound(FinanceException):
    def __init__(self):
        message = 'Usuário não encontrado'
        super().__init__(message_error=message, status_code=404)

class AccountNotFound(FinanceException):
    def __init__(self):
        message = 'Conta não encontrada!!'
        super().__init__(message_error=message, status_code=404)

class TransactionNotAccepted(FinanceException):
    def __init__(self):
        message = 'Transação rejeitada! Não são aceitas transações com valor maior que R$ 1000,00'
        super().__init__(message_error=message, status_code=403)