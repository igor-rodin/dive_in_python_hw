from enum import Enum
import decimal
import os

DEPOSIT_AMOUNT_UNIT = 50
WITHDRAWAL_INTEREST = 1.5
MIN_WITHDRAWAL_AMOUNT = 30
MAX_WITHDRAWAL_AMOUNT = 600
WEALTH_TRESHOLD_AMOUNT = 5_000_000
WEALTH_TAX = 10
GIFT_INTEREST = 3


class Operation(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    EXIT = 3


atm_operations: dict[Operation, list[int]] = {
    Operation.DEPOSIT: [], Operation.WITHDRAW: []}
total_amount: decimal.Decimal = 0


def show_total_sum():
    '''
    Выводит на консоль остаток на счете
    '''
    print(f"На счету: {total_amount:0.2f} у.е.\n")


def print_actions() -> None:
    '''
    Выводит на консоль доступные действия в ATM
    '''
    print("Доступные действия:")
    print(f"{Operation.DEPOSIT.value}. - Пополнить")
    print(f"{Operation.WITHDRAW.value}. - Снять")
    print(f"{Operation.EXIT.value}. - Выйти")


def clear_console() -> None:
    '''
    Очищает сонсоль
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_menu() -> Operation:
    '''
    Выводит на консоль меню ATM
    '''
    print("---------ATM------------\n")
    show_total_sum()
    print_actions()
    code = int(input("Ваше действие > "))
    codes = [val.value for val in Operation]
    while code not in codes:
        print_actions()
        code = int(input("Ваше действие > "))
    clear_console()
    return Operation(code)


def charge_gift_interest(operation: Operation) -> decimal.Decimal:
    '''
    Вычисляет процент за каждую третью операцию снятия или начисления
    '''
    global atm_operations
    global total_amount
    interest = 0
    if len(atm_operations[operation]) > 0 and len(atm_operations[operation]) % 3 == 0:
        interest = decimal.Decimal(0.01 * GIFT_INTEREST) * total_amount
        print(f"Начислено {GIFT_INTEREST}% за каждую третью операцию")
    return interest


def charge_withdraw_interest(amount: decimal.Decimal) -> decimal.Decimal:
    '''
    Вычисляет процент за операцию снятия со счета
    '''
    interest = amount * decimal.Decimal(WITHDRAWAL_INTEREST * 0.01)
    if interest > MAX_WITHDRAWAL_AMOUNT:
        return MAX_WITHDRAWAL_AMOUNT
    if interest < MIN_WITHDRAWAL_AMOUNT:
        return MIN_WITHDRAWAL_AMOUNT
    return interest


def deduct_wealth_tax(amount: decimal.Decimal) -> decimal.Decimal:
    '''
    Вычисляет налог на богатство
    '''
    if amount < WEALTH_TRESHOLD_AMOUNT:
        return 0
    print(f"Вычтено {WEALTH_TAX}% за богатство")
    return amount * decimal.Decimal(WEALTH_TAX * 0.01)


def deposit() -> decimal.Decimal:
    '''
    Возвращает сумму пополнения и сохраняет операцию
    '''
    deposit_amount = int(input("Введите сумму пополнения: "))
    while deposit_amount % DEPOSIT_AMOUNT_UNIT != 0:
        print(f"Сумма пополнеия должна быть кратна {DEPOSIT_AMOUNT_UNIT}")
        deposit_amount = int(input("Введите сумму пополнения: "))
    else:
        atm_operations[Operation.DEPOSIT].append(deposit_amount)
        return deposit_amount


def withdraw() -> decimal.Decimal:
    '''
    Возвращает сумму списания и сохраняет операцию
    '''
    global total_amount
    withdraw_amount = int(input("Введите сумму списания: "))
    while withdraw_amount % DEPOSIT_AMOUNT_UNIT != 0:
        print(f"Сумма пополнеия должна быть кратна {DEPOSIT_AMOUNT_UNIT}")
        withdraw_amount = int(input("Введите сумму списания: "))
    else:
        if withdraw_amount > total_amount:
            print(f"Сумма снятия превышает остаток на счете.")
            return 0
        atm_operations[Operation.WITHDRAW].append(withdraw_amount)
        return withdraw_amount


def do_deposit(total_amount: decimal.Decimal) -> decimal.Decimal:
    '''
    Возвращает общую сумму начисления с учетом процентов и налога
    '''
    wealth_tax = deduct_wealth_tax(total_amount)
    oper_amount = deposit()
    gift_interest = charge_gift_interest(Operation.DEPOSIT)

    return oper_amount + gift_interest - wealth_tax


def do_withdraw(total_amount: decimal.Decimal) -> decimal.Decimal:
    '''
    Возвращает общую сумму снятия с учетом процентов и налога
    '''
    wealth_tax = deduct_wealth_tax(total_amount)
    oper_amount = withdraw()
    interest_amount = charge_withdraw_interest(oper_amount)
    gift_interest = charge_gift_interest(Operation.DEPOSIT)

    return oper_amount + wealth_tax + interest_amount - gift_interest


def main():
    '''
    Основной цикл работы
    '''
    global total_amount
    while True:
        operation = show_menu()
        match operation:
            case Operation.DEPOSIT:
                total_amount += do_deposit(total_amount)
            case Operation.WITHDRAW:
                total_amount -= do_withdraw(total_amount)
            case Operation.EXIT:
                print("Выход...")
                break


main()
