def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def parse_list(s, delim, to_float=False):
    s = s.strip()
    if s.startswith("["):
        s = s[1:]
    if s.endswith("]"):
        s = s[:-1]
    lst = [t.strip() for t in s.split(delim)]
    if to_float:
        for i in range(0, len(lst)):
            if is_number(lst[i]):
                lst[i] = float(lst[i])
    return lst
