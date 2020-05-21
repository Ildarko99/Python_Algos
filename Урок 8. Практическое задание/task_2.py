"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "come to me"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

def before(s):
    return {ch: ch for ch in s}

def hfmnn_code():
    s = input()
    code = before(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in code:
        print(f'{ch}: {code[ch]}')
    return encoded

print(hfmnn_code())