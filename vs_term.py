def get_input(text):
    return input(text)


def get_terms(count, total, tl):
    if count < int(total):
        new_list = tl + [(get_input('Enter term date\n'))]
        return get_terms((count + 1), total, new_list)
    elif count >= int(total):
        new_list = tl
        return new_list


def split_term_date(term):
    return term[0:4], term[4:6]


def make_term_list(tl):
    stl = map(split_term_date, tl)
    return stl


def print_all(stl):
    list(map(print, stl))


def vs_term():
    print_all(
        make_term_list(
            get_terms(0, get_input('How many terms total?\n'), [])))


vs_term()
