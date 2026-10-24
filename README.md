# Business Suite Curriculum: Course Site

Chart Academy's in-person entrepreneurship program for the DC Office of Neighborhood Safety and Engagement (ONSE)
Pathways Program, contract CW137729. Curriculum by IRSJA (Boss Up, Money Moves, Flipping the Game).
60 hours over 20 days in four modules: BUILD, BRAND, FINANCE, LAUNCH, ending in a pitch competition.
Designed for participants coming home after time away, with a daily Tech Catch-Up and a Readiness Review.

## How it's built

Everything comes from one file, `_build/curriculum.py`, so the website and the ONSE document never disagree.
The site uses the same design as the AI for Workforce Readiness course (Chart-Academy/ai-workforce-readiness):
`css/style.css`, `js/theme.js`, and the illustrations in `_build/art.py` come from it. Business Suite additions are at the
end of `style.css`.

Pages: Home, Getting Started, Lessons (20 days in 4 modules), Capstone, Grading, Readiness Review.

| To change… | Do this |
|---|---|
| A lesson, agenda, objective, rubric, or resource | Edit `_build/curriculum.py`, then run both builds below |
| The website | `.venv/bin/python _build/build_site.py` |
| The ONSE curriculum document (Word) | `.venv/bin/python _build/build_curriculum_doc.py` (writes to `docs/`, which is not uploaded to GitHub) |
| Canvas links | Fill in `_build/canvas_links.py` once the Canvas course exists, then rebuild the site |

Setup once: `python3 -m venv .venv && .venv/bin/pip install python-docx`.

## Still to do

- [ ] Create the Business Suite Canvas course and assignments (module projects M1–M3, capstone, pre/post assessment, daily exit tickets), then fill in `canvas_links.py`.
- [ ] Before each cohort, confirm the agency details and rules flagged CONFIRM in `curriculum.py` and the resource links on the Readiness Review page.
- [ ] Participant workbook and project templates (Word).
- [ ] Pre/post assessment questions (25 items).
- [ ] Confirm the grading weights (Participation 20%, module projects 45%, capstone 35%) in `build_site.py`.
- [ ] Class slides for each day, if wanted (the AI course posts slides inside each lesson).
