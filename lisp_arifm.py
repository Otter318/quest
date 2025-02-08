def parse_lisp_string(s: str):
    s = s.strip()
    if s == "()":
        return None

    s = s[1:-1].strip()
    if " . " in s:
        fst, snd = s.split(" . ", 1)
        fst = parse_lisp_string(fst) if fst.startswith("(") else int(fst)
        snd = (
            parse_lisp_string(snd)
            if snd.startswith("(")
            else int(snd) if snd != "()" else None
        )
        return (fst, snd)


def recursive_print(pair):
    print("(", end="")
    if pair is None:
        print(")", end="")
        return

    head, tail = pair
    if isinstance(head, tuple):
        recursive_print(head)
    else:
        print(head, end="")
    print(" . ", end="")
    if tail is None:
        print("()", end="")
    elif isinstance(tail, tuple):
        recursive_print(tail)
    else:
        print(tail, end="")
    print(")", end="")


def apply_operation(pair, operation):
    if pair is None:
        return 0 if operation in ("+", "-") else 1

    head, tail = pair
    head_value = apply_operation(head, operation) if isinstance(head, tuple) else head
    tail_value = (
        apply_operation(tail, operation)
        if isinstance(tail, tuple)
        else (tail if tail is not None else 0 if operation in ("+", "-") else 1)
    )

    if operation == "+":
        return head_value + tail_value
    elif operation == "-":
        return head_value - tail_value
    elif operation == "*":
        return head_value * tail_value
    elif operation == "/":
        return head_value / tail_value if tail_value != 0 else float("inf")


def parse_and_compute_lisp_expression(lst: str, operation: str) -> None:
    parsed_list = parse_lisp_string(lst)
    result = apply_operation(parsed_list, operation)
    print(f"Result ({operation}):", result)


if __name__ == "__main__":
    lisp_list = "(10 . (2 . (3 . (5 . ()))))"
    parse_and_compute_lisp_expression(lisp_list, "+")
    parse_and_compute_lisp_expression(lisp_list, "-")
    parse_and_compute_lisp_expression(lisp_list, "*")
    parse_and_compute_lisp_expression(lisp_list, "/")
