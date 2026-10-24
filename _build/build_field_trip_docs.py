"""Builds the Day 4 DLCP licensing field trip documents from curriculum.FIELD_TRIP.

Run: .venv/bin/python _build/build_field_trip_docs.py
  files/Licensing-Visit-Prep-Sheet.docx      participant handout (published on the site, printed for Day 3)
  docs/DLCP-Field-Trip-Planning-Guide.docx   staff planning guide (not published)
"""
from pathlib import Path

import curriculum as C
from docx_kit import Kit

ROOT = Path(__file__).resolve().parent.parent
LOGO = str(ROOT / "images" / "chart-logo-icon.png")
T = C.FIELD_TRIP
DAY = next(d for d in C.DAYS if d["n"] == T["day"])


def checklist(k, items):
    for x in items:
        k.para("☐  " + x, after=3)


def bullets(k, items):
    k.bullets([("", x) for x in items])


def visit_table(k):
    t = k.grid(["Visit", "Details"], [1.6, 5.1], 4, height=0.3, first_col=["Where", "Getting there", "How long", "Wear"])
    for row, text in enumerate([f"{T['host']}, {T['address']}", T["transit"], T["length"], T["wear"]], start=1):
        k.cell_text(t, row, 1, text)


def prep_sheet():
    k = Kit(LOGO)
    k.header(f"{C.PROGRAM['title']} · Day {T['day']} Field Trip", "Licensing Visit Prep Sheet")
    k.name_date()
    k.para(f"On Day {T['day']} we visit the {T['host']}, the agency that registers and licenses DC businesses. "
           "You'll hear from licensing staff, then look up the license for your own business. Fill this in on Day 3.")
    visit_table(k)
    k.h2("Bring with you")
    checklist(k, T["bring"])
    k.h2("Know before you go")
    for item in T["know"]:
        k.answer_box(item, height=0.45)
    k.h2("Questions to ask a licensing specialist")
    k.para("Circle the ones you'll ask, and add your own. Write the answers while you're there.", muted=True, size=9.5)
    t = k.grid(["Question", "Answer"], [3.3, 3.4], len(T["questions"]) + 2, height=0.55)
    for i, q in enumerate(T["questions"] + ["My question:", "My question:"], start=1):
        k.cell_text(t, i, 0, q)
    k.h2("During the visit")
    bullets(k, T["conduct"])
    k.h2("After the visit")
    bullets(k, T["after"])
    k.callout("Your story, your terms.", "You never have to share personal information at DLCP. If you have a question about "
              "how a record could affect your license, ask your case manager or a specialist privately.", "EEF1F6", "3A56A6")
    k.footer(f"{C.PROGRAM['title']} · Chart Academy · Licensing Visit Prep Sheet")
    out = ROOT / "files" / "Licensing-Visit-Prep-Sheet.docx"
    out.parent.mkdir(exist_ok=True)
    k.save(str(out))
    return out


def planning_guide():
    k = Kit(LOGO)
    k.header(f"{C.PROGRAM['title']} · Staff only", "DLCP Licensing Field Trip: Planning Guide")
    k.para(f"Day {T['day']} of every cohort is a field trip to the {T['host']}. This guide covers booking, logistics, "
           "the day's agenda, and follow-up. Confirm the address, visitor ID rules, and contacts with DLCP each time you book.")
    visit_table(k)
    k.h2("Planning timeline")
    for when, tasks in T["staff_timeline"]:
        k.para(when, bold=True, after=1)
        checklist(k, tasks)
    k.h2(f"Day {T['day']} agenda (180 minutes)")
    t = k.grid(["Min", "Block", "Activity"], [0.6, 1.3, 4.8], len(DAY["agenda"]), height=0.35)
    for i, (mins, label, text) in enumerate(DAY["agenda"], start=1):
        k.cell_text(t, i, 0, str(mins))
        k.cell_text(t, i, 1, label)
        k.cell_text(t, i, 2, text)
    k.h2("Learning objectives")
    bullets(k, DAY["objectives"])
    k.h2("Staff roles on the day")
    k.bullets([("Lead Instructor (Wayne Williams): ", "keeps time, introduces the presenter, leads the debrief and exit ticket."),
               ("Case Management Associate (Rasheed Murphy): ", "sign-in and headcount, late arrivals, ID or security issues, "
                                                                "and private questions about records."),
               ("Program Director (Cedric Thompson): ", "DLCP relationship, booking, and the thank-you note.")])
    k.h2("Booking request: what to ask DLCP for")
    bullets(k, [
        f"Date and time for a group of 15 to 20 participants plus 2 or 3 staff, {T['length']}.",
        "A 60-minute licensing session: registration, the Basic Business License, categories and endorsements, Certificate of "
        "Occupancy and home occupation permits, inspections, renewals, and how licensing considers records.",
        "45 minutes in the Small Business Resource Center with licensing specialists for pair lookups.",
        "A room for 30 minutes of work time and a debrief.",
        "Visitor ID and security rules, accessibility, and whether names must be sent in advance.",
        "The presenter's name and a day-of contact number."])
    k.h2("Participant materials")
    k.para("Licensing Visit Prep Sheet (handed out on Day 3), sign-in sheet, emergency contact list, and the draft DC "
           "Compliance Checklist from the Module 1 project.")
    k.h2("After the visit")
    checklist(k, T["staff_timeline"][-1][1])
    k.footer(f"{C.PROGRAM['title']} · Chart Academy · DLCP Field Trip Planning Guide · Staff only")
    out = ROOT / "docs" / "DLCP-Field-Trip-Planning-Guide.docx"
    out.parent.mkdir(exist_ok=True)
    k.save(str(out))
    return out


if __name__ == "__main__":
    C.check()
    for path in (prep_sheet(), planning_guide()):
        print("Wrote", path.relative_to(ROOT))
