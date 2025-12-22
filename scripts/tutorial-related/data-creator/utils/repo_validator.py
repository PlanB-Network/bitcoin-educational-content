import os
from utils.path_utils import normalize_base_path

REQUIRED_ITEMS = [
    ("docs/50-planb-tags.md", "file", "Required tag file"),
    ("resources/projects", "dir", "Projects directory"),
    ("professors", "dir", "Professors directory"),
    ("tutorials", "dir", "Tutorials directory"),
]

def validate_repo_root(base_path: str) -> dict:
    """
    Validate that base_path is the root of the cloned repository
    and that the app can access required folders/files.
    """
    normalized = normalize_base_path(base_path)
    issues = []

    if not normalized:
        issues.append("No repository path selected.")
        return {"ok": False, "path": normalized, "issues": issues}

    if not os.path.exists(normalized):
        issues.append("The selected path does not exist.")
        return {"ok": False, "path": normalized, "issues": issues}

    if not os.path.isdir(normalized):
        issues.append("The selected path is not a directory.")
        return {"ok": False, "path": normalized, "issues": issues}

    # Check required items
    for rel, kind, _label in REQUIRED_ITEMS:
        parts = rel.split("/")
        target = os.path.join(normalized, *parts)

        if kind == "file":
            if not os.path.isfile(target):
                issues.append(f"Missing required file: {rel}")
            elif not os.access(target, os.R_OK):
                issues.append(f"Cannot read required file: {rel}")

        elif kind == "dir":
            if not os.path.isdir(target):
                issues.append(f"Missing required directory: {rel}/")
            else:
                if not os.access(target, os.R_OK | os.X_OK):
                    issues.append(f"Cannot access required directory: {rel}/")
                # The app must write here (create files/folders)
                if not os.access(target, os.W_OK):
                    issues.append(f"No write permission in: {rel}/")

    return {"ok": len(issues) == 0, "path": normalized, "issues": issues}
