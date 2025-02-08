def lisp_sum(lst):
    if lst == ():
        return 0
    if isinstance(lst, tuple) and len(lst) == 2:
        return lst[0] + lisp_sum(lst[1])