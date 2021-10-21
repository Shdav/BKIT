import json
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1


path = "../data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(Unique(field(arg, "job-name"), True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda mean: mean + " c опытом Python", arg))


@print_result
def f4(arg):
    return dict(zip(arg, ['зарплата {} руб.'.format(x) for x in gen_random(len(arg), 1000000, 2000000)]))

if __name__ == "__main__": 
    with cm_timer_1():
        f4(f3(f2(f1(data))))