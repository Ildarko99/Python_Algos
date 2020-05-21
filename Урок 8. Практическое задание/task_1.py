"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""

import hashlib
s = "welcome"

def podstrok(s):
    res = []
    hres = []
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            a = s[j:j + i]
            h = hashlib.sha1(a.encode('utf-8')).hexdigest()
            if not h in hres:
                hres.append(h)
                res.append(a)
    return res
print(podstrok(s))