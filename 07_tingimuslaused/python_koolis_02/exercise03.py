"""
Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning
 seejärel kuvatakse tehe koos vastusega. Näiteks:

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5
"""

def calculate(num1: float, num2: float, operation: str) -> str:
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2

    if result == "":
        return f"tundmatu tehe: {operation}"
    return f"{num1}{operation}{num2}={result}"


def dog_calculate(num1: float, num2: float, operation: str) -> str:
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2

    if result == "":
        return f"URRRRRRR GRRRR"
    return f"{round(result)*"auh "}"


if __name__ == '__main__':
    first = float(input("Sisestage esimene arv: "))
    second = float(input("Sisestage teine arv: "))
    op = input("Sisestage tehe: ")
    print(f"Tulemus: {dog_calculate(first, second, op)}")








