"""Builds the Business Suite course website from curriculum.py, in the same design as the
AI for Workforce Readiness course (css/style.css and js/theme.js come from that site).

Run: .venv/bin/python _build/build_site.py
Pages: index, getting-started, lessons, capstone, grading, readiness.
"""
import re
from html import escape as e
from pathlib import Path

import art
import curriculum as C
from canvas_links import link

ROOT = Path(__file__).resolve().parent.parent
CSS_V = "20261024c"

NAV = [("index.html", "Home"), ("getting-started.html", "Getting Started"), ("lessons.html", "Lessons"),
       ("capstone.html", "Capstone"), ("grading.html", "Grading"), ("readiness.html", "Readiness Review")]

# weight-bar color class for each grading component, in curriculum.WEIGHTS order
BAR_CLASS = ["wb-part", "wb-lessons", "wb-final"]

PROJECT_KEY = {"build": "M1", "brand": "M2", "finance": "M3", "launch": "CAP"}


def page(path, title, body):
    nav = "\n".join(f'        <li><a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{e(label)}</a></li>'
                    for href, label in NAV)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Lexend:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
  <link rel="icon" type="image/png" href="images/chart-icon.png">
  <link rel="stylesheet" href="css/style.css?v={CSS_V}">
  <script>(function(){{try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}}})();</script>
</head>
<body id="top">
  <nav class="site-nav" aria-label="Main">
    <div class="wrap">
      <a class="brand-mark" href="index.html"><img src="images/chart-icon.png" alt="" width="40" height="40"><span>Chart Academy</span></a>
      <ul class="navbar">
{nav}
      </ul>
      <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode"></button>
    </div>
  </nav>
  <div class="road" aria-hidden="true"></div>
{body}
  <footer class="site-footer">
    <div class="wrap">
      <nav class="footer-map" aria-label="Site map">
        <div>
          <p class="footer-head">Course</p>
          <ul><li><a href="index.html">Home</a></li><li><a href="getting-started.html">Getting Started</a></li><li><a href="grading.html">Grading</a></li></ul>
        </div>
        <div>
          <p class="footer-head">Learn</p>
          <ul><li><a href="lessons.html">Lessons</a></li><li><a href="capstone.html">Capstone</a></li><li><a href="readiness.html">Readiness Review</a></li></ul>
        </div>
        <div>
          <p class="footer-head">Support</p>
          <ul><li><a href="{link("HOME")}" target="_blank" rel="noopener">Canvas</a></li><li><a href="tel:988">988 Crisis Line</a></li><li><a href="tel:18887934357">DC Access Helpline</a></li></ul>
        </div>
      </nav>
      <a class="to-top" href="#top">Back to top <span aria-hidden="true">↑</span></a>
      <div class="footer-meta">
        <p>© 2026 Chart Academy · Curriculum by IRSJA</p>
        <p>{e(C.PROGRAM["title"])} · Delivered for the DC Office of Neighborhood Safety and Engagement · <a href="https://www.thechartacademy.com">thechartacademy.com</a></p>
      </div>
    </div>
  </footer>
  <script src="js/theme.js"></script>
  <script>/* open the lesson a link points to, for example lessons.html#day-3 */
  function openHash(){{var d=location.hash&&document.querySelector(location.hash);if(d&&d.tagName==="DETAILS"){{d.open=true;d.scrollIntoView();}}}}
  addEventListener("hashchange",openHash);openHash();</script>
</body>
</html>
"""
    (ROOT / path).write_text(html)


def canvas_btn(key, label="Submit in Canvas"):
    return f'<a class="btn btn-primary" href="{link(key)}" target="_blank" rel="noopener">{e(label)}</a>'


def plain(text):
    """Website wording for the internal CONFIRM reminders."""
    return (text.replace("(CONFIRM current rules and legal-aid contacts before each cohort)",
                         "(your instructor confirms current rules with you)")
            .replace("(CONFIRM current rules before each cohort)", "(your instructor confirms current rules with you)"))


def module_of(day):
    return next(m for m in C.MODULES if m["days"][0] <= day["n"] <= m["days"][1])


def head(eyebrow, title, lede, art_svg=""):
    return f"""    <header class="page-head gs-head">
      <div class="gs-head-text">
        <p class="eyebrow">{e(eyebrow)}</p>
        <h1>{e(title)}</h1>
        <p class="lede">{lede}</p>
      </div>
      {art_svg}
    </header>"""


def outcome(text):
    return f'<li class="outcome">{art.OUTCOME_ICON}<p>{text}</p></li>'


def own_words(lines):
    return (f'<div class="own-words"><p class="label">In your own words · write this part yourself</p>'
            f'<ul>{"".join(f"<li>{e(x)}</li>" for x in lines)}</ul></div>')


def road_map():
    """Switchback road climbing four rows (one per module, five days each); project days are red."""
    rows = [222, 167, 112, 57]
    xs = [70, 135, 200, 265, 330]
    pts = []
    for r, y in enumerate(rows):
        pts += [(x, y) for x in (xs if r % 2 == 0 else xs[::-1])]
    d = f"M28 {rows[0]} H362"
    for r in range(1, len(rows)):
        y0, y1 = rows[r - 1], rows[r]
        if r % 2:  # turn on the right, then run left
            d += f" C402 {y0} 402 {y1} 362 {y1} H58"
        else:  # turn on the left, then run right
            d += f" C18 {y0} 18 {y1} 58 {y1} H362"
    d += " H34"
    stops = "".join(
        f'<g class="rm-stop{" lab" if day.get("project") else ""}"><circle cx="{x}" cy="{y}" r="9"/>'
        f'<text x="{x}" y="{y + 3.5}" text-anchor="middle">{day["n"]}</text></g>'
        for day, (x, y) in zip(C.DAYS, pts))
    cx, cy = 30, rows[-1] - 26
    return f"""<svg class="road-art" viewBox="0 0 420 240" role="img" aria-label="A road that climbs back and forth through four modules, with stops for Day 1 through Day 20, ending at a graduation cap">
        <path class="rm-road" d="{d}"/>
        <path class="rm-dash" d="{d}"/>
        {stops}
        <g class="rm-cap bs" transform="translate({cx:.0f} {cy:.0f})">
          <path d="M-22 0l22-9 22 9-22 9z"/>
          <path d="M-12 4v8c0 4 24 4 24 0v-8l-12 5z"/>
          <path class="rm-tassel" d="M20 1v12"/>
        </g>
        <g class="rm-legend"><circle cx="300" cy="22" r="6"/><text x="312" y="26">Project due</text></g>
      </svg>"""


# ---------------------------------------------------------------- pages

def index():
    slots = [("00", "Getting Started", "Day 1: accounts, ground rules, and the pre-assessment")] + [
        (f"0{m['num']}", f"{m['name'].title()}: {m['focus']}", f"Days {m['days'][0]}–{m['days'][1]} · {m['project']}")
        for m in C.MODULES] + [("05", "Capstone Pitch Competition", "Day 20: present to a panel of DC business owners")]
    timecard = "".join(f'<li><span class="slot">{s}</span><span><span class="slot-title">{e(t)}</span>'
                       f'<span class="slot-note">{e(n)}</span></span></li>' for s, t, n in slots)
    outcomes = "".join(outcome(x) for x in [
        "<strong>A launch-ready business portfolio</strong>: business plan, DC compliance checklist, brand kit, financial plan, and marketing strategy.",
        "<strong>A registration path for your business</strong>: the structure, licenses, permits, and Clean Hands steps you need in DC.",
        "<strong>Prices and budgets you can defend</strong>, reviewed by finance professionals.",
        "<strong>A pitch delivered to real business owners</strong>, and a resume and interview practice for income while you build.",
        "<strong>A professional network</strong>: a one-year Greater Washington Black Chamber of Commerce membership, SCORE mentors, and a Truist Bank banking relationship.",
        "<strong>Four AI agents you built yourself</strong>: a Business Plan Coach, a Market Research Assistant, a Pricing and Budget Analyst, and a Pitch Coach.",
        "<strong>Tools to keep</strong>: a laptop, professional bag, Dress for Success package, your IRSJA guides, and Canvas access after you graduate.",
    ])
    paths = [
        ('<svg class="path-art" viewBox="0 0 200 130" role="img" aria-label="A lightbulb, for starting from an idea">'
         '<ellipse class="pa-soft" cx="100" cy="114" rx="78" ry="12"/><circle class="pa-fill" cx="100" cy="54" r="34"/>'
         '<rect class="pa-paper" x="86" y="86" width="28" height="18" rx="4"/><path class="pa-line" d="M90 96h20"/>'
         '<path class="pa-accent-line" d="M100 8v-2M146 30l6-4M54 30l-6-4M156 60h8M36 60h8"/></svg>',
         "Path A", "Starting from an idea",
         "Test whether people will pay for your idea before you spend money, then turn it into a registered business with a plan, a brand, and a budget."),
        ('<svg class="path-art" viewBox="0 0 200 130" role="img" aria-label="A storefront with an awning, for formalizing work you already do">'
         '<ellipse class="pa-soft" cx="100" cy="116" rx="80" ry="10"/><rect class="pa-paper" x="44" y="50" width="112" height="62" rx="4"/>'
         '<path class="pa-fill" d="M38 34h124l-8 22H46z"/><rect class="pa-fill" x="88" y="72" width="26" height="40" rx="2"/>'
         '<rect class="pa-soft" x="56" y="66" width="24" height="20" rx="2"/><rect class="pa-soft" x="124" y="66" width="22" height="20" rx="2"/>'
         '<path class="pa-accent" d="M170 18l4 8 9 1-7 6 2 9-8-5-8 5 2-9-7-6 9-1z"/></svg>',
         "Path B", "Formalizing work you already do",
         "Already earning from a skill, a trade, or side work? Register it, price it properly, open a business bank account, and grow it on solid ground."),
        ('<svg class="path-art" viewBox="0 0 200 130" role="img" aria-label="Rising steps with an upward arrow, for building after time away">'
         '<ellipse class="pa-soft" cx="100" cy="116" rx="80" ry="10"/><rect class="pa-soft" x="36" y="84" width="34" height="30" rx="3"/>'
         '<rect class="pa-fill" x="74" y="62" width="34" height="52" rx="3"/><rect class="pa-fill" x="112" y="38" width="34" height="76" rx="3"/>'
         '<path class="pa-accent-line" d="M34 72l40-24 26 10 50-38"/><path class="pa-accent-line" d="M132 18h20v20"/></svg>',
         "Path C", "Building after time away",
         "Catch up on the tools and systems that changed, clear the steps that come first (ID, Clean Hands, credit), and build something that is yours."),
    ]
    paths_html = "".join(f'<div class="path">{svg}<p class="eyebrow">{a}</p><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                         for svg, a, t, d in paths)
    body = f"""
  <section class="hero-band">
      <div class="wrap hero">
        <div class="hero-intro">
          <p class="eyebrow">Chart Academy · ONSE Pathways · 2026</p>
          <h1>{e(C.PROGRAM["title"])}</h1>
          <p class="lede">The {e(C.PROGRAM["subtitle"])}: four weeks of in-person instruction that take you from a business idea to a registered, branded, and financially planned business, ending with a pitch to a panel of DC business owners. No business experience needed.</p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="getting-started.html">Start here <span aria-hidden="true">→</span></a>
            <a class="btn btn-on-dark" href="lessons.html">See the 20 lessons</a>
          </div>
        </div>

        <div class="hero-art">
          <img src="images/chart-full.png" alt="Chart Academy logo: a graduation cap above a map pin with a winding road" width="900" height="665">
          {art.AVATARS}
          <p class="avatar-caption">For every participant: starting fresh, formalizing, or growing.</p>
        </div>
      </div>
    <div class="hero-road" aria-hidden="true"></div>
  </section>

  <main class="wrap">
    <section class="home-section">
      <p class="eyebrow">Who it's for</p>
      <h2 class="section-title">Who this course is for</h2>
      <p class="lede section-lede">Wherever you're starting from, the goal is the same: a legal, registered business you understand inside and out.</p>
      <div class="paths">{paths_html}</div>
    </section>

    <section class="home-section outcomes-band">
      <p class="eyebrow">Outcomes</p>
      <h2 class="section-title">What you'll leave with</h2>
      <ul class="outcomes">{outcomes}</ul>
    </section>

    <section class="home-section plan-section">
      <div class="plan-intro">
        <p class="eyebrow">Course plan</p>
        <h2 class="section-title">Four modules, 20 days, one business</h2>
        <p>Every class follows the same rhythm: <strong>Learn → Do → Build</strong>. You learn a skill, use it in the real market or with a guest expert, then add it to your own business portfolio. 60 hours, 3 hours a day, with four <span class="lab-badge">Agent Lab</span> days and a <span class="lab-badge">Field Trip</span> to the DC licensing office.</p>
        <p><a class="btn btn-primary" href="lessons.html">See all lessons</a></p>
      </div>
      <aside class="timecard" aria-label="Course plan">
        <div class="timecard-head"><span>Module</span><span>20 days</span></div>
        <ol>{timecard}</ol>
      </aside>
    </section>
  </main>
"""
    page("index.html", C.PROGRAM["title"], body)


def getting_started():
    accounts = [
        ('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', "A professional email",
         "One you're comfortable giving to customers and lenders. If yours is a nickname, we will help you make one with your name."),
        ('<path d="M4 5h16v14H4z"/><path d="M4 9h16M9 9v10"/>', "Canvas",
         "Where you find materials, answer the daily exit ticket (that is how attendance is counted), and submit your projects. You keep access after you graduate."),
        ('<path d="M4 18l4-12h8l4 12z"/><path d="M8 6l8 12M16 6L8 18"/>', "A Google account",
         "Google Drive keeps your plan, survey, and spreadsheets in one place, and Google Gemini is a free AI assistant for the Agent Labs. ChatGPT, Claude, or Microsoft Copilot also work."),
        ('<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>', "Your phone",
         "Charged, with a working number. You'll use it for customer interviews, banking apps, and your business social media."),
    ]
    flow = [
        ('<path d="M4 5h7a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H4z"/><path d="M20 5h-4a3 3 0 0 0-2 1"/><path d="M20 5v13h-6"/>', "1. Learn",
         "Expert Content from your instructor and your IRSJA guide: Boss Up, Money Moves, or Flipping the Game."),
        ('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>', "2. Do",
         "Field Experience in the real market (interviews, surveys, networking) or a Master Class with a guest expert or Truist Bank."),
        ('<path d="M14 6l4 4-9 9H5v-4z"/><path d="M12 8l4 4"/>', "3. Build",
         "Add today's piece to your own business portfolio, then answer the exit ticket and click <strong>Submit in Canvas</strong>."),
    ]
    rules = [
        ('<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/>', "Respect: one voice at a time. Disagree with ideas, not people."),
        ('<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>', "Your story, your terms: you never have to share anything about your past."),
        ('<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>', "What people share in this room stays in this room."),
        ('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', "Attendance: miss two days in a row and your case manager reaches out to help, not to judge."),
        ('<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>', "Check facts that matter, especially licensing rules and numbers, before you rely on them."),
        ('<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>', "Never paste your Social Security number, bank details, passwords, or details about a record into an AI tool."),
        ('<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/>', "Customer quotes, survey results, and numbers must be real. AI organizes your evidence; it never makes it up."),
        ('<path d="M14 6l4 4-9 9H5v-4z"/>', "Write the “In your own words” part of every project and lab yourself."),
    ]
    card = lambda icon, h, p: (f'<li class="gs-card"><svg class="gs-icon" viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>'
                               f'<h3>{e(h)}</h3><p>{p}</p></li>')
    body = f"""
  <main class="wrap">
{head("Day 1 · Orientation", "Getting Started", "On the first day, we set up your accounts together, go over how the class works, and you take a short pre-assessment. Bring your phone and a photo ID if you have one. Laptops are provided.", art.WALK)}

    <section class="readiness-box" id="pre-assessment">
      <div class="readiness-text">
        <p class="eyebrow">Pre-assessment · about 25 minutes</p>
        <h2>Day One Pre-Assessment</h2>
        <p>A short check of what you already know about starting and running a business. It shows where you're starting, so the course can help you grow from there. It isn't graded, and it's fine not to know the answers yet. You take the same check on Day 20 to see how far you've come.</p>
        <ol class="readiness-steps">
          <li>Log in to Canvas with the account your instructor sets up with you.</li>
          <li>Answer on your own. It measures you, not a search engine or an AI tool.</li>
          <li>Click <strong>Submit</strong> at the end.</li>
        </ol>
        <p>{canvas_btn("PRE", "Start the pre-assessment")}</p>
      </div>
    </section>

    <section>
      <h2 class="section-title">Set up your accounts</h2>
      <ul class="gs-cards four">{"".join(card(*a) for a in accounts)}</ul>
      <p class="callout">Missing an ID, a phone, or an email? Come anyway. Your case manager will help you sort it out in your <a href="readiness.html">Readiness Review</a> this week.</p>
    </section>

    <section>
      <h2 class="section-title">How each class works</h2>
      <p class="lede section-lede">Every class is 3 hours and follows the same rhythm: <strong>Learn → Do → Build</strong>. Most days start with a 5-minute Tech Catch-Up on one digital skill.</p>
      <ol class="gs-cards three gs-flow">{"".join(card(*f) for f in flow)}</ol>
    </section>

    <section class="gs-box">
      <h2 class="section-title">Your words, your work</h2>
      <div class="prose">
        <p>Every module project ends with an <strong>In your own words</strong> section. Your instructor, AI tools, and classmates can help you build your plan, but this part you write yourself. Lenders, partners, and the pitch panel want to know what <em>you</em> understand about your business.</p>
        <ul><li><em>“I chose this business structure because …”</em></li><li><em>“I set my price at … because …”</em></li></ul>
        <p>Short and honest beats long and polished.</p>
      </div>
    </section>

    <section class="gs-box rules">
      <h2 class="section-title">Ground rules</h2>
      <ul class="rule-list">{"".join(f'<li><svg class="gs-icon" viewBox="0 0 24 24" aria-hidden="true">{i}</svg><span>{e(t)}</span></li>' for i, t in rules)}</ul>
    </section>

    <section>
      <h2 class="section-title">Tech Catch-Up</h2>
      <p class="lede section-lede">One quick digital skill most days. If you have been away for a while, this is where you catch up. If you already know it, you help someone who doesn't.</p>
      <div class="prose"><ol>{"".join(f"<li>{e(x)}</li>" for x in C.TECH_CATCHUP)}</ol></div>
    </section>
    <p class="callout">New to business or to computers, or coming back after time away? That's who this course was built for. Ask questions early and often.</p>
  </main>
"""
    page("getting-started.html", f"Getting Started · {C.PROGRAM['title']}", body)


def agent_lab(lab):
    steps = re.sub(r" (\d)\. ", r"\n\1. ", lab["prompt"])  # one numbered job per line
    prompt = e(steps) + f'\n\n<span class="ai-note">{e(C.AI_GUARD)}</span>'
    return f"""
          <details class="lesson-part agent-lab" id="{lab['id'].lower()}" data-wo="{lab['id']}">
            <summary class="part-title"><span><span class="lab-tag">Agent Lab · {lab['id']}</span> {e(lab['name'])}</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body">
              <p>{e(lab['summary'])}</p>
              <p class="lab-meta"><strong>Tools:</strong> {e(lab['tools'])} · Any free AI assistant works: Google Gemini, ChatGPT, Claude, or Microsoft Copilot.</p>
              <div>
              <p class="label">Starter instructions</p>
              <pre class="prompt">{prompt}</pre>
              </div>
              <div class="assess">
              <p class="label">Lab assignment · submit in Canvas</p>
              <ol>{"".join(f"<li>{e(x)}</li>" for x in lab["steps"])}</ol>
              <p class="callout"><strong>Check the AI:</strong> {e(lab['check'])}</p>
              {own_words(lab["own_words"])}
              <p class="upload"><strong>Upload to Canvas:</strong> {e(lab['upload'])}</p>
              <p class="submit-canvas">{canvas_btn(lab['id'])}</p>
              </div>
            </div>
          </details>"""


def field_trip():
    T = C.FIELD_TRIP
    li = lambda items: "".join(f"<li>{e(x)}</li>" for x in items)
    return f"""
          <details class="lesson-part agent-lab" id="field-trip">
            <summary class="part-title"><span><span class="lab-tag">Field Trip</span> Prepare for your visit to DLCP</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body">
              <p>Today we visit the {e(T['host'])}, the agency that registers and licenses DC businesses. Fill in the prep sheet on Day 3 and bring it with you.</p>
              <div class="table-wrap"><table><tbody>
                <tr><td><strong>Where</strong></td><td>{e(T['host'])}, {e(T['address'])}</td></tr>
                <tr><td><strong>Getting there</strong></td><td>{e(T['transit'])}. Your instructor confirms the meeting time and place.</td></tr>
                <tr><td><strong>How long</strong></td><td>{e(T['length'])}</td></tr>
                <tr><td><strong>Wear</strong></td><td>{e(T['wear'])}</td></tr>
              </tbody></table></div>
              <div class="materials">
              <p class="label">Prep sheet</p>
              <ul class="files"><li><a href="files/Licensing-Visit-Prep-Sheet.docx">Licensing Visit Prep Sheet (Word)</a></li></ul>
              </div>
              <div class="prose">
              <h4>Bring with you</h4><ul>{li(T['bring'])}</ul>
              <h4>Know before you go</h4><ul>{li(T['know'])}</ul>
              <h4>Questions to ask a licensing specialist</h4><ol>{li(T['questions'])}</ol>
              <h4>During the visit</h4><ul>{li(T['conduct'])}</ul>
              <h4>After the visit</h4><ol>{li(T['after'])}</ol>
              </div>
            </div>
          </details>"""


def lesson(day):
    m = module_of(day)
    if day.get("trip"):
        badge = "Field Trip"
    elif day.get("lab"):
        badge = "Agent Lab"
    elif day.get("project"):
        badge = "Capstone" if m["key"] == "launch" else "Project due"
    elif day.get("truist"):
        badge = "Truist Bank"
    elif day.get("master"):
        badge = "Master Class"
    else:
        badge = None
    badge_html = f'<span class="lab-badge">{e(badge)}</span>' if badge else ""
    agenda = "".join(f"<li><strong>{e(label)} · {mins} min.</strong> {e(text)}</li>" for mins, label, text in day["agenda"])
    partners = [x for x in (day.get("master") and f"<li><strong>Master Class:</strong> {e(day['master'])}</li>",
                            day.get("truist") and f"<li><strong>Truist Bank, Bank On Your Success:</strong> {e(day['truist'])}</li>",
                            day.get("field") and f"<li><strong>Field Experience:</strong> {e(day['field'])}</li>") if x]
    build = next((t for _, label, t in day["agenda"] if label == "Build"), None)
    steps = []
    if build:
        steps.append(f"<li><strong>Build:</strong> {e(build)}</li>")
    if day.get("exit"):
        steps.append(f"<li><strong>Exit ticket:</strong> {e(day['exit'])}</li>")
    project = ""
    if day.get("project"):
        pm = next(x for x in C.MODULES if x["key"] == day["project"])
        where = "capstone.html" if pm["key"] == "launch" else f"grading.html#rubric-m{pm['num']}"
        title = "Capstone" if pm["key"] == "launch" else f"Module {pm['num']} project"
        project = f"""
          <details class="lesson-part assignment">
            <summary class="part-title"><span>{title}: {e(pm["project"])}</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body"><div class="assess">
            <ol>{"".join(f"<li>{e(x)}</li>" for x in pm["project_items"])}</ol>
            {own_words(pm["own_words"])}
            <p class="upload"><strong>Upload to Canvas:</strong> your project files or Google links (shared as <strong>Anyone with the link → Viewer</strong>) and your own-words answers. <a href="{where}">See how it's scored.</a></p>
            <p class="submit-canvas">{canvas_btn(PROJECT_KEY[pm["key"]])}</p>
            </div></div>
          </details>"""
    support = (f"""
          <details class="lesson-part">
            <summary class="part-title"><span>Readiness support</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body"><p>{e(plain(day["reentry"]))}</p><p><a href="readiness.html">Open the Readiness Review</a></p></div>
          </details>""" if day.get("reentry") else "")
    assignment = (f"""
          <details class="lesson-part assignment">
            <summary class="part-title"><span>In-class assignment</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body"><div class="assess">
            <ol>{"".join(steps)}</ol>
            <p class="submit-canvas">{canvas_btn(f"D{day['n']}", "Answer the exit ticket in Canvas")}</p>
            </div></div>
          </details>""" if day.get("exit") else "")
    return f"""
      <details class="lesson" id="day-{day['n']}">
        <summary><span class="lesson-num">Day {day['n']}</span><span class="lesson-title">{e(day['title'])}</span>{badge_html}<span class="lesson-toggle" aria-hidden="true">+</span></summary>
        <div class="lesson-body">
          <p>{e(", ".join(C.TOPICS[t] for t in day["topics"]))}. Reference guide: {e(m["guide"])}.</p>
          <details class="lesson-part objectives">
            <summary class="part-title"><span>Learning objectives</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body">
            <p class="objectives-lead">The participant will be able to:</p>
            <ol class="objectives">{"".join(f"<li>{e(o)}</li>" for o in day["objectives"])}</ol>
            </div>
          </details>
          <details class="lesson-part">
            <summary class="part-title"><span>Class agenda · 3 hours</span><span class="part-toggle" aria-hidden="true">+</span></summary>
            <div class="part-body"><div class="prose"><ol>{agenda}</ol>{f"<ul>{''.join(partners)}</ul>" if partners else ""}</div></div>
          </details>{field_trip() if day.get("trip") else ""}{"".join(agent_lab(l) for l in C.AGENT_LABS if l["id"] == day.get("lab"))}{support}{assignment}{project}
        </div>
      </details>"""


def lessons():
    mods = "".join(f"""
    <div class="module">
      <div class="module-head">
        <p class="eyebrow">Module {m['num']} · Days {m['days'][0]}–{m['days'][1]} · Guide: {e(m['guide'])}</p>
        <h2>{e(m['name'].title())}: {e(m['focus'])}</h2>
        <p class="module-note">{e(m['summary'])}</p>
      </div>
{"".join(lesson(d) for d in C.module_days(m))}
    </div>""" for m in C.MODULES)
    body = f"""
  <main class="wrap">
{head("20 lessons, in order", "Lessons", 'Open a day to see its learning objectives, the class agenda, and the in-class assignment. Days marked <span class="lab-badge">Agent Lab</span> include an AI agent you build and test in class, and <span class="lab-badge">Field Trip</span> is our visit to the DC licensing office. Module projects are due on Days 5, 10, and 15.', road_map())}
{mods}
  </main>
"""
    page("lessons.html", f"Lessons · {C.PROGRAM['title']}", body)


def capstone():
    launch = next(m for m in C.MODULES if m["key"] == "launch")
    hire = art.HIRE.replace(">HIRED<", ">READY<").replace(
        'aria-label="A résumé and a job posting under a magnifying glass, stamped Hired"',
        'aria-label="A business plan and a pitch deck, stamped Ready"')
    body = f"""
  <main class="wrap">
{head("Days 19 and 20 · two parts", "Capstone Pitch Competition", e(C.CAPSTONE["summary"]), hire)}

    <section>
      <h2 class="section-title">Part A: Business Portfolio (due Day 19)</h2>
      <div class="prose">
        <p>Your portfolio brings together everything you built in the four modules. It must be consistent: the prices in your financial plan should match your pitch, and your brand should match your marketing.</p>
        <ol>{"".join(f"<li>{e(x)}</li>" for x in C.CAPSTONE["portfolio"])}</ol>
        <p class="submit-canvas">{canvas_btn("CAP", "Upload your portfolio in Canvas")}</p>
      </div>
    </section>

    <section class="capstone">
      <p class="eyebrow">Capstone</p>
      <h2 class="section-title">Part B: The Pitch (Day 20)</h2>
      <div class="prose">
        <p>You present your business to a panel of established business owners and professionals, with ONSE staff, partners, and guests in the room.</p>
        <ol>{"".join(f"<li>{e(x)}</li>" for x in C.CAPSTONE["pitch"])}</ol>
        <p class="callout">{e(C.CAPSTONE["awards"])}</p>
        {own_words(launch["own_words"] + ["“I know people will pay because … (what my interviews and survey showed)”"])}
      </div>
    </section>

    <section>
      <h2 class="section-title">How the panel scores you</h2>
      <div class="table-wrap"><table>
        <thead><tr><th>Criterion</th><th>What the panel looks for</th><th class="num">Points</th></tr></thead>
        <tbody>{"".join(f"<tr><td><strong>{e(n)}</strong></td><td>{e(d)}</td><td class='num'>{p}</td></tr>" for n, p, d in C.CAPSTONE["rubric"])}</tbody>
        <tfoot><tr><td>Total</td><td></td><td class="num">{sum(p for _, p, _ in C.CAPSTONE["rubric"])}</td></tr></tfoot>
      </table></div>
    </section>

    <section>
      <h2 class="section-title">Also on Day 20</h2>
      <div class="prose"><ul>
        <li><strong>Post-assessment:</strong> the same check you took on Day 1, so you can see your growth.</li>
        <li><strong>Graduation:</strong> certificates, your Greater Washington Black Chamber of Commerce membership, and next steps with your case manager.</li>
      </ul>
      <p>{canvas_btn("POST", "Take the post-assessment")}</p></div>
    </section>
  </main>
"""
    page("capstone.html", f"Capstone · {C.PROGRAM['title']}", body)


def grading():
    rows = "".join(f"<tr><td>{e(n)}</td><td>{e(d)}</td><td class='num'>{w}%</td></tr>" for n, d, w in C.WEIGHTS)
    bar = "".join(f'<span class="{cls}" style="flex: {w};">{e(n)} {w}%</span>' for (n, _, w), cls in zip(C.WEIGHTS, BAR_CLASS))
    rubrics = "".join(f"""
      <details class="lesson-part rubric" id="rubric-m{m['num']}">
        <summary class="part-title"><span>Module {m['num']}: {e(m['project'])}</span><span class="part-toggle" aria-hidden="true">+</span></summary>
        <div class="part-body"><div class="table-wrap"><table>
          <thead><tr><th>Rubric row</th><th>Full (5)</th><th>Partial (3)</th><th>Not yet (1)</th></tr></thead>
          <tbody>{"".join(f"<tr><td><strong>{e(r[0])}</strong></td><td>{e(r[1])}</td><td>{e(r[2])}</td><td>{e(r[3])}</td></tr>" for r in m["rubric"])}</tbody>
          <tfoot><tr><td>Total</td><td></td><td></td><td class="num">20</td></tr></tfoot>
        </table></div></div>
      </details>""" for m in C.MODULES if m["rubric"])
    cap_rubric = f"""
      <details class="lesson-part rubric" id="rubric-capstone">
        <summary class="part-title"><span>Capstone: Portfolio and Pitch</span><span class="part-toggle" aria-hidden="true">+</span></summary>
        <div class="part-body"><div class="table-wrap"><table>
          <thead><tr><th>Rubric row</th><th>What the panel looks for</th><th class="num">Points</th></tr></thead>
          <tbody>{"".join(f"<tr><td><strong>{e(n)}</strong></td><td>{e(d)}</td><td class='num'>{p}</td></tr>" for n, p, d in C.CAPSTONE["rubric"])}</tbody>
          <tfoot><tr><td>Total</td><td></td><td class="num">50</td></tr></tfoot>
        </table></div></div>
      </details>"""
    completion = (art.COMPLETION
                  .replace(">AI for Workforce Readiness<", ">Business Suite Curriculum<")
                  .replace(">with 80% proficiency or higher<", ">Entrepreneurship and Business Ownership<")
                  .replace(">AI WORKFORCE<", ">BUSINESS<")
                  .replace(">80% PROFICIENCY<", ">ONSE PATHWAYS<")
                  .replace('aria-label="AI Workforce Ready digital badge from Chart Academy"',
                           'aria-label="Business Ready digital badge from Chart Academy"'))
    body = f"""
  <main class="wrap">
{head("How work is scored", "Grading", "You're graded on work you do in class and submit in Canvas, on your capstone, and on whether you can explain your business in your own words.", art.GRADE)}

    <section>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Component</th><th>What counts</th><th class="num">Weight</th></tr></thead>
          <tbody>{rows}</tbody>
          <tfoot><tr><td>Total</td><td></td><td class="num">100%</td></tr></tfoot>
        </table>
      </div>
      <div class="weight-bar" aria-hidden="true">{bar}</div>
    </section>

    <section id="rubrics">
      <h2 class="section-title">How each project is scored</h2>
      <div class="prose"><p>Each module project is worth <strong>20 points</strong>: four rubric rows, each scored <strong>Full</strong> (5), <strong>Partial</strong> (3), or <strong>Not yet</strong> (1). The capstone is worth <strong>50 points</strong> and is scored by the pitch panel and your instructor. Open a project to see its rubric.</p></div>
      <h3 class="rubric-group">Module projects</h3>
      {rubrics}
      <h3 class="rubric-group">Capstone</h3>
      {cap_rubric}
    </section>

    <section>
      <h2 class="section-title">How your work is reviewed</h2>
      <div class="prose">
        <p>Your instructor scores every project with its rubric and leaves written feedback in Canvas within two class days.</p>
        <ul>
          <li>Submit your work with the <strong>Submit in Canvas</strong> button in each lesson.</li>
          <li>If a Google link isn't shared as <strong>Anyone with the link → Viewer</strong>, your work can't be read until you share it.</li>
          <li>The daily exit ticket is how attendance is recorded, so answer it before you leave.</li>
        </ul>
      </div>
    </section>

    <section>
      <h2 class="section-title">Pre- and post-assessment</h2>
      <div class="prose">
        <p>You take the same short assessment twice: on Day 1 and on Day 20.</p>
        <ul>
          <li><strong>Day 1</strong> isn't graded. It only shows where you're starting.</li>
          <li><strong>Day 20</strong> shows your growth. Your results are shared with you and the program.</li>
        </ul>
      </div>
    </section>

    <section class="completion">
      <div class="completion-text">
        <p class="eyebrow">Finish strong</p>
        <h2 class="section-title">Certificate of completion</h2>
        <p class="lede">Complete the program to earn a <strong>Certificate of Completion</strong> and a <strong>digital badge</strong> for your LinkedIn profile.</p>
        <ul class="earn-list">
          <li><strong>Attend at least 48 of the 60 hours.</strong> Your daily exit ticket records attendance.</li>
          <li><strong>Submit all three module projects</strong> in Canvas.</li>
          <li><strong>Deliver your pitch</strong> at the Capstone Pitch Competition.</li>
          <li><strong>Show it off.</strong> List the certificate on your resume and capability statement, and add the badge to LinkedIn.</li>
        </ul>
      </div>
      {completion}
    </section>
  </main>
"""
    page("grading.html", f"Grading · {C.PROGRAM['title']}", body)


def readiness():
    checks = [
        ('<rect x="3" y="6" width="18" height="12" rx="2"/><circle cx="8.5" cy="12" r="2"/><path d="M13 10h5M13 14h4"/>', "ID",
         "A government photo ID is needed to register a business and open a bank account."),
        ('<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/>', "Clean Hands",
         "DC will not license a business if you owe the District more than $100. Check your status on MyTax.DC.gov."),
        ('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', "Supervision",
         "If you are on supervision, tell your officer about self-employment and check any limits on social media."),
        ('<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h4"/>', "Credit and banking",
         "Pull your free credit report. No history or old debts? Your case manager helps you build a plan."),
    ]
    groups = "".join(f"""
      <details class="lesson-part"{" open" if i == 0 else ""}>
        <summary class="part-title"><span>{e(g['area'])}</span><span class="part-toggle" aria-hidden="true">+</span></summary>
        <div class="part-body"><div class="table-wrap"><table>
          <tbody>{"".join(f'<tr><td><a href="{e(url)}" target="_blank" rel="noopener"><strong>{e(name)}</strong></a></td><td>{e(desc)}</td></tr>' for name, url, desc in g["items"])}</tbody>
        </table></div></div>
      </details>""" for i, g in enumerate(C.REENTRY_RESOURCES))
    tips = "".join(f'<tr><td><a href="lessons.html#day-{d["n"]}"><strong>Day {d["n"]}</strong></a></td><td>{e(plain(d["reentry"]))}</td></tr>'
                   for d in C.DAYS if d.get("reentry"))
    body = f"""
  <main class="wrap">
{head("Week 1 · with your case manager", "Readiness Review", "Starting a business can mean clearing a few steps first: ID, debts to DC, a record, credit, supervision rules, and a world that went digital. None of these has to stop you. In week one, you and your case manager go through each one together.")}

    <section>
      <h2 class="section-title">Four things to check in week one</h2>
      <ul class="gs-cards four">{"".join(f'<li class="gs-card"><svg class="gs-icon" viewBox="0 0 24 24" aria-hidden="true">{i}</svg><h3>{e(h)}</h3><p>{e(p)}</p></li>' for i, h, p in checks)}</ul>
      <p class="callout">Nothing you share in your Readiness Review is used to judge you, and you decide what to share.</p>
    </section>

    <section>
      <h2 class="section-title">DC resources</h2>
      <p class="lede section-lede">Programs and rules change. Your instructor checks these before each cohort.</p>
      {groups}
    </section>

    <section>
      <h2 class="section-title">Built into the lessons</h2>
      <div class="table-wrap"><table><tbody>{tips}</tbody></table></div>
    </section>

    <p class="callout">In crisis or need to talk? Call or text <a href="tel:988">988</a>, or call the DC Access Helpline at <a href="tel:18887934357">1-888-793-4357</a>, any time.</p>
  </main>
"""
    page("readiness.html", f"Readiness Review · {C.PROGRAM['title']}", body)


def main():
    C.check()
    for build in (index, getting_started, lessons, capstone, grading, readiness):
        build()
    print("Built", len(list(ROOT.glob("*.html"))), "pages")


if __name__ == "__main__":
    main()
