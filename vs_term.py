from datetime import date
from itertools import repeat


def get_input(text):
    return input(text)


def print_all(lst):
    list(map(print, lst))


def create_date(tup, d):
    new_date = date(int(tup[0]), int(tup[1]), d)
    return new_date


def get_terms(count, total, lst):
    if count < int(total):
        new_list = lst + [(get_input('Enter term date\n'))]
        return get_terms((count + 1), total, new_list)
    else:
        return lst


def split_term_date(term):
    return term[0:4], term[4:6]


def make_term_list(lst):
    lst2 = map(split_term_date, lst)
    return lst2


def make_date_list(lst):
    lst2 = map(create_date, lst, repeat(1))
    return lst2


def vs_term():
    print_all(
        make_date_list(
            make_term_list(
                get_terms(0, get_input('How many terms total?\n'), []))))


if __name__ == "__main__":
    vs_term()
