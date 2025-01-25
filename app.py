def parse_and_print_lisp_list(lst: str) -> None:

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

    parsed_list = parse_lisp_string(lst)
    recursive_print(parsed_list)
    print()


if __name__ == "__main__":

    lisp_list = "(1 . (2 . (3 . (5 . (7 . (9 . ())))))"
    parse_and_print_lisp_list(lisp_list)
