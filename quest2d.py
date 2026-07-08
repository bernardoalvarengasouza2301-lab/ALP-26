def calculadora(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero."
    else:
        return "Operador inválido."