from langchain_core.tools import tool

@tool
def soma(a: int, b: int) -> int:
    """
    Soma dois números inteiros.
    """
    return a + b

print(soma.name)
print(soma.description)
print(type(soma))
print(soma.invoke({'a': 25, 'b': 27}))