# ===============
check = lambda n: True if n > 10 else False
print(check(11))
# ===============

latter_a = lambda x: 'bor' if 'a' in x.lower() else 'yoq'
print(latter_a('chukalak'))
# ===============

to_upper = lambda s: s.upper()
print(to_upper('salom'))
# ===============

modul = lambda a, b: abs(a - b)
print(modul(10, 3))
# ===============

tengmi = lambda a, b: True if a == b else False
print(tengmi(5, 6))
# ===============

bolish = lambda n: n // 2
print(bolish(17))
# ===============

yil_ol = lambda s: s.split('-')[0]
print(yil_ol('2025-07-02'))
# ===============

count_items = lambda lst: len(lst)
print(count_items([1, 2, 3, 4]))
# ===============

capitalize_name = lambda s: s.capitalize()
print(capitalize_name("alisher"))
# ===============

eng_kichik = lambda a, b, c: min(a, b, c)
print(eng_kichik(4, 9, 2))
# ===============

plus_one = lambda n: n + 1
print(plus_one(7))
# ===============
