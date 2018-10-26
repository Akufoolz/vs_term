import calendar
from datetime import date
from itertools import repeat


def get_input(text):
    return input(text)


def print_all(lst):
    list(map(print, lst))


def create_date(tup, d):
    new_date = date(int(tup[0]), int(tup[1]), d)
    return new_date


def add_months(in_date, months):
    months_count = in_date.month + months

    year = in_date.year + int(months_count / 12)

    month = (months_count % 12)
    if month == 0:
        month = 12

    day = in_date.day
    last_day_of_month = calendar.monthrange(year, month)[1]
    if day > last_day_of_month:
        day = last_day_of_month

    new_date = date(year, month, day)
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
    lst2 = list(map(split_term_date, lst))
    return lst2


def make_date_list(lst):
    lst2 = list(map(create_date, lst, repeat(1)))
    return lst2


def make_span_list(count, lst, lst2):
    if count < len(lst) - 1:
        date1 = lst[count]
        date2 = lst[count + 1]
        print(add_months(date1, 6))
        if add_months(date1, 6) != date2:
            new_list = lst2 + [(date2 - date1)]
            print('not equal')
            return make_span_list((count + 1), lst, new_list)
        elif add_months(date1, 6) == date2:
            new_list = lst2
            print('equal')
            return make_span_list((count + 1), lst, new_list)
    else:
        return lst2


def vs_term():
    date_list = make_date_list(
        make_term_list(
            get_terms(0, get_input('How many terms total?\n'), [])))
    print_all(make_span_list(0, date_list, []))


if __name__ == "__main__":
    vs_term()
