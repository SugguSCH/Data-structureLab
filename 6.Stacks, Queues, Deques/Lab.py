from ArrayStackClass import ArrayStackclass

S = ArrayStackclass()
exprssions = [
    "()",
    "(",
    "}",
    "]",
    "(a + b) * (c + d)",
    "({[a + b]} - c)",
    "((a + b)",
    "{[()]}"
]
print("\nTesting balanced Parentheses:")
for expr in exprssions:
    S.push(expr)
    print(f"Expression: {expr} --> Balanced: {S.is_balanced(expr)}")
    S.pop()