"""Canvas links for the "Submit in Canvas" buttons.

The Business Suite Canvas course is not created yet. Until it is, every button opens the Canvas dashboard.
When it exists: set COURSE to its number, fill in IDS from the assignment URLs, and run build_site.py.
Keys: M1, M2, M3 (module projects), CAP (capstone portfolio), PRE, POST (assessments), D1..D20 (exit tickets).
"""
BASE = "https://thechartacademy.instructure.com"
COURSE = None
IDS = {}


def link(key):
    if COURSE and key in IDS:
        return f"{BASE}/courses/{COURSE}/assignments/{IDS[key]}"
    if COURSE:
        return f"{BASE}/courses/{COURSE}"
    return BASE
