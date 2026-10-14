from task4 import Stack


def rpn_calc(expr):
    stack = Stack()
    for token in expr.split():
        if token in ("+", "-", "*", "/"):
            if stack.size() < 2:
                return "Некорректное выражение"
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                if b == 0:
                    return "Деление на ноль"
                stack.push(a / b)
        else:
            try:
                stack.push(float(token) if "." in token else int(token))
            except ValueError:
                return f"Некорректный токен: {token}"
    if stack.size() != 1:
        return "Некорректное выражение"
    return stack.pop()


def run_tests():
    print("3 4 +            ->", rpn_calc("3 4 +"))
    print("5 1 2 + 4 * + 3 - ->", rpn_calc("5 1 2 + 4 * + 3 -"))
    print("7 2 /            ->", rpn_calc("7 2 /"))
    print("3 +              ->", rpn_calc("3 +"))
    print("3 4              ->", rpn_calc("3 4"))
    print("1 0 /            ->", rpn_calc("1 0 /"))
    print("2 x +            ->", rpn_calc("2 x +"))


if __name__ == "__main__":
    run_tests()