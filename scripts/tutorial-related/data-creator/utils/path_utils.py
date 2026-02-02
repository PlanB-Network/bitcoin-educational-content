import os

def normalize_base_path(raw) -> str:
    if raw is None:
        return ""

    s = str(raw).strip()
    if not s:
        return ""

    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        s = s[1:-1].strip()

    s = os.path.expanduser(os.path.expandvars(s))

    s = os.path.normpath(s)

    try:
        s = os.path.abspath(s)
    except Exception:
        pass

    return s
