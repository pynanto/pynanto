def removeprefix(s: str, prefix: str) -> str:
    if s.startswith(prefix):
        s = s[len(prefix):]
    return s
