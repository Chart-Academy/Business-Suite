"""Builds the Business Suite course website from curriculum.py.

Run: .venv/bin/python _build/build_site.py
Pages: index, getting-started, modules/build|brand|finance|launch, capstone, reentry.
"""
from html import escape as e
from pathlib import Path

import curriculum as C
from canvas_links import link

ROOT = Path(__file__).resolve().parent.parent
CSS_V = "20261024a"

NAV = [("index.html", "Home"), ("getting-started.html", "Getting Started"), ("modules/build.html", "1 · Build"),
       ("modules/brand.html", "2 · Brand"), ("modules/finance.html", "3 · Finance"), ("modules/launch.html", "4 · Launch"),
       ("capstone.html", "Capstone"), ("reentry.html", "Reentry Toolkit")]


def page(path, title, body):
    up = "../" if "/" in path else ""
    nav = "\n".join(f'<li><a href="{up}{href}"{" aria-current=page" if href == path else ""}>{e(label)}</a></li>'
                    for href, label in NAV)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · Business Suite · Chart Academy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}css/style.css?v={CSS_V}">
</head>
<body id="top">
<header class="site-header"><div class="wrap">
<a class="brand" href="{up}index.html"><img src="{up}images/chart-logo-icon.png" alt="Chart Academy logo"><span class="brand-text">Business Suite<small>Chart Academy · ONSE Pathways</small></span></a>
<nav aria-label="Main"><input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Show or hide the menu"><label for="nav-toggle" class="nav-btn" aria-hidden="true"><span class="bars"></span>Menu</label>
<ul class="nav">
{nav}
</ul></nav>
</div></header>

<main>
{body}
</main>

<footer class="site-footer"><div class="wrap cols">
<div><h4>Modules</h4><ul>{"".join(f'<li><a href="{up}modules/{m["key"]}.html">{m["num"]} · {m["name"].title()}</a></li>' for m in C.MODULES)}</ul></div>
<div><h4>Support</h4><ul><li><a href="{up}getting-started.html">Getting Started</a></li><li><a href="{up}reentry.html">Reentry Toolkit</a></li><li><a href="{up}capstone.html">Capstone</a></li><li><a href="{link("HOME")}" target="_blank" rel="noopener">Canvas</a></li></ul></div>
<div><p>© 2026 Chart Academy · In partnership with IRSJA<br>Delivered for the DC Office of Neighborhood Safety and Engagement<br><a href="https://www.thechartacademy.com" target="_blank" rel="noopener">thechartacademy.com</a></p><p>Crisis support: call or text <a href="tel:988">988</a> · DC Access Helpline <a href="tel:18887934357">1-888-793-4357</a></p><p><a href="#top">Back to top ↑</a></p></div>
</div></footer>
<script>/* open the day a link points to (for example modules/build.html#day-3) */
function openHash(){{var d=location.hash&&document.querySelector(location.hash);if(d&&d.tagName==="DETAILS"){{d.open=true;d.scrollIntoView();}}}}
addEventListener("hashchange",openHash);openHash();</script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(exist_ok=True)
    out.write_text(html)


def canvas_btn(key, label="Submit in Canvas"):
    return f'<a class="btn" href="{link(key)}" target="_blank" rel="noopener">{e(label)} ↗</a>'


def plain(text):
    """Website wording for the internal CONFIRM reminders."""
    return text.replace("(CONFIRM current rules and legal-aid contacts before each cohort)",
                        "(your instructor confirms current rules with you)").replace(
        "(CONFIRM current rules before each cohort)", "(your instructor confirms current rules with you)")


def index():
    mods = "".join(f"""
    <article class="card mod-card course{' c2' if m['num'] % 2 == 0 else ''}">
      <span class="tag t{m['num']}">Module {m['num']} · Days {m['days'][0]}–{m['days'][1]}</span>
      <h3>{m['name']}</h3>
      <p><strong>{e(m['focus'])}.</strong> {e(m['summary'])}</p>
      <p class="small">You build: {e(m['project'])}</p>
      <div class="go-btn"><a class="btn" href="modules/{m['key']}.html">Open module</a></div>
    </article>""" for m in C.MODULES)
    leave = ["A launch-ready business portfolio: plan, brand, finances, and pitch",
             "Your IRSJA guides to keep: Boss Up, Money Moves, Flipping the Game",
             "A laptop, a professional bag, and a Dress for Success package",
             "A one-year Greater Washington Black Chamber of Commerce membership",
             "A business banking relationship through Truist Bank",
             "Canvas access, templates, and resources after you graduate"]
    body = f"""
<div class="hero"><div class="wrap hero-grid">
  <div>
  <p class="eyebrow">ONSE Pathways · 60 hours · 20 days</p>
  <h1>Entrepreneurship and Business Ownership Program</h1>
  <p class="lead">Develop the skills, plans, and professional network to launch and operate a legally registered business in the District of Columbia. In four weeks you will build a business plan, a brand, a financial plan, and a pitch, and present it to a panel of DC business owners.</p>
  <p><span class="partner">Curriculum by <strong>IRSJA</strong> · Delivered by <strong>Chart Academy</strong></span></p>
  <div class="btns">
    <a class="btn" href="getting-started.html">Start here →</a>
    <a class="btn ghost" href="reentry.html">Reentry Toolkit</a>
  </div>
  </div>
  <img src="images/chart-logo-full.png" alt="Chart Academy logo">
</div></div>

<section class="alt" id="modules"><div class="wrap">
  <p class="eyebrow">Four modules · one business</p>
  <h2>Build → Brand → Finance → Launch</h2>
  <div class="mod-grid" style="--cols:4">{mods}</div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Every day · 3 hours</p>
  <h2>How each day works</h2>
  <ol class="steps">
    <li><strong>Open</strong>Check in, set the day's goal, and a 5-minute Tech Catch-Up.</li>
    <li><strong>Learn</strong>Expert Content from your instructor and your IRSJA guide.</li>
    <li><strong>Do</strong>Field Experience in the real market, or a Master Class with a guest expert.</li>
    <li><strong>Build</strong>Add today's piece to your business portfolio, then the exit ticket in Canvas.</li>
  </ol>
</div></section>

<section class="alt"><div class="wrap">
  <div class="grid g2">
    <div><p class="eyebrow">What you leave with</p><h2>Program resources and network</h2>
      <ul>{"".join(f"<li>{e(x)}</li>" for x in leave)}</ul></div>
    <div><p class="eyebrow">Reentry support</p><h2>Designed for returning citizens</h2>
      <p>If you have been away for a while, a lot changed: phones, apps, banking, how businesses get customers. This course meets you where you are. Every day starts with a short Tech Catch-Up, a case manager helps with ID, Clean Hands, supervision schedules, and anything else in the way, and nobody has to share their story unless they want to.</p>
      <a class="btn ghost" href="reentry.html">See the Reentry Toolkit</a></div>
  </div>
</div></section>"""
    page("index.html", "Home", body)


def getting_started():
    checks = ["A government photo ID (or a plan with your case manager to get one)",
              "Your phone, charged, with a working number",
              "An email address you can log in to (we will help you make one)",
              "Your supervision check-in schedule, if you have one, so we can plan around it",
              "One or two business ideas, even rough ones"]
    rules = [("Respect", "One voice at a time. Disagree with ideas, not people."),
             ("Your story, your terms", "You never have to share anything about your past."),
             ("Confidential", "What people share in this room stays in this room."),
             ("Attendance", "Two missed days in a row and your case manager will reach out to help, not to judge."),
             ("Phones", "Phones are tools here. Use them for class work, silence them otherwise.")]
    body = f"""
<div class="hero"><div class="wrap">
  <p class="eyebrow">Day 1</p>
  <h1>Getting Started</h1>
  <p class="lead">Everything you need for your first day, and who to ask when something gets in the way.</p>
</div></div>

<section class="alt"><div class="wrap grid g2">
  <div><h2>Bring on Day 1</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in checks)}</ul>
  <p class="small">Missing something? Come anyway. Your case manager will help you sort it out.</p></div>
  <div><h2>Your accounts</h2>
  <div class="card"><h3>Canvas</h3><p>Where you find materials, take the daily exit ticket (that is how attendance is counted), and submit your projects. You keep access after you graduate.</p>{canvas_btn("HOME", "Open Canvas")}</div>
  <div class="card" style="margin-top:14px"><h3>Pre-assessment</h3><p>A short check of what you already know, on Day 1. It is not graded. You take the same one on Day 20 to see how much you grew.</p>{canvas_btn("PRE", "Take it in Canvas")}</div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Group agreements</h2>
  <table class="facts">{"".join(f"<tr><th>{e(a)}</th><td>{e(b)}</td></tr>" for a, b in rules)}</table>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">5 minutes a day</p>
  <h2>Tech Catch-Up</h2>
  <p>Most days start with one quick digital skill. If you have been away for years, this is where you catch up. If you already know it, you help someone who does not.</p>
  <ol>{"".join(f"<li>{e(x)}</li>" for x in C.TECH_CATCHUP)}</ol>
</div></section>

<section><div class="wrap">
  <h2>Finishing the program</h2>
  <div class="note info">To complete the program, attend at least 48 of the 60 hours, submit the three module projects, and pitch on Day 20. The top three pitches win a $500 startup package.</div>
  <h2>Your team</h2>
  <table class="facts">{"".join(f"<tr><th>{e(r)}</th><td><strong>{e(n)}</strong><br>{e(d)}</td></tr>" for r, n, d in C.STAFF if r not in ("Data Analyst", "Operations and Reporting"))}</table>
</div></section>"""
    page("getting-started.html", "Getting Started", body)


def day_block(day):
    chips = []
    if day.get("master"):
        chips.append(f'<span class="chip c-master">Master Class · {e(day["master"])}</span>')
    if day.get("truist"):
        chips.append(f'<span class="chip c-bank">Truist Bank · {e(day["truist"])}</span>')
    if day.get("field"):
        chips.append(f'<span class="chip c-field">Field · {e(day["field"])}</span>')
    agenda = "".join(f'<li><span class="mins">{m} min</span><b>{e(label)}</b> {e(text)}</li>' for m, label, text in day["agenda"])
    topics = ", ".join(C.TOPICS[t] for t in day["topics"])
    reentry = (f'<div class="note info"><strong>Reentry support.</strong> {e(plain(day["reentry"]))}</div>'
               if day.get("reentry") else "")
    exit_ = (f'<div class="download"><div><div class="file">Exit ticket</div><div class="meta">{e(day["exit"])}</div></div>'
             f'{canvas_btn(f"D{day["n"]}", "Answer in Canvas")}</div>' if day.get("exit") else "")
    project = ""
    if day.get("project"):
        m = next(x for x in C.MODULES if x["key"] == day["project"])
        key = {"build": "M1", "brand": "M2", "finance": "M3", "launch": "CAP"}[m["key"]]
        project = (f'<div class="download"><div><div class="file">Due today: {e(m["project"])}</div>'
                   f'<div class="meta">See the checklist and rubric at the top of this page.</div></div>{canvas_btn(key)}</div>')
    return f"""
  <details class="acc day" id="day-{day['n']}"><summary><span class="acc-head"><span class="eyebrow">Day {day['n']} · 3 hours</span><span class="acc-title">{e(day['title'])}</span></span></summary>
  <div class="acc-body">
    <p class="small">Topics: {e(topics)}</p>
    <h4>Today you will</h4><ul>{"".join(f"<li>{e(o)}</li>" for o in day["objectives"])}</ul>
    {"<p class='chips'>" + "".join(chips) + "</p>" if chips else ""}
    <h4>Agenda</h4><ol class="agenda">{agenda}</ol>
    {reentry}{exit_}{project}
  </div></details>"""


def module_page(m, prev, nxt):
    days = C.module_days(m)
    if m["rubric"]:
        rubric = "".join(f"<tr><th>{e(r[0])}</th><td><strong>Full (5):</strong> {e(r[1])}<br><strong>Partial (3):</strong> "
                         f"{e(r[2])}<br><strong>Not yet (1):</strong> {e(r[3])}</td></tr>" for r in m["rubric"])
        key = f"M{m['num']}"
        grading = f"""<details class="acc" style="margin-top:14px"><summary><span class="acc-head"><span class="eyebrow">20 points · scored in Canvas</span><span class="acc-title">How it's graded</span></span></summary>
    <div class="acc-body"><table class="facts">{rubric}</table></div></details>"""
    else:
        key, grading = "CAP", '<p>Scored with the 50-point capstone rubric. <a href="../capstone.html">See the capstone page.</a></p>'
    pager = ('<div class="mod-nav">'
             + (f'<a class="btn ghost" href="{prev["key"]}.html">← Module {prev["num"]}: {prev["name"].title()}</a>' if prev else "<span></span>")
             + (f'<a class="btn ghost" href="{nxt["key"]}.html">Module {nxt["num"]}: {nxt["name"].title()} →</a>' if nxt
                else '<a class="btn ghost" href="../capstone.html">Capstone →</a>') + "</div>")
    body = f"""
<div class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> › Module {m['num']}</p>
  <p class="eyebrow">Module {m['num']} · Days {m['days'][0]}–{m['days'][1]} · 15 hours · Guide: {e(m['guide'])}</p>
  <h1>{m['name']}</h1>
  <p class="lead">{e(m['summary'])}</p>
</div></div>

<section class="alt"><div class="wrap grid g2">
  <div><h2>By the end of this module</h2><ul>{"".join(f"<li>{e(o)}</li>" for o in m["objectives"])}</ul>
    <p><strong>Outcome:</strong> {e(m['outcome'])}</p></div>
  <div class="card course"><p class="eyebrow">Module project</p><h3>{e(m['project'])}</h3>
    <ul>{"".join(f"<li>{e(x)}</li>" for x in m["project_items"])}</ul>
    {canvas_btn(key)}
    {grading}</div>
</div></section>

<section><div class="wrap">
  <h2>Day by day</h2>
  <p class="small">Tap a day to open it.</p>
  {"".join(day_block(d) for d in days)}
  {pager}
</div></section>"""
    page(f"modules/{m['key']}.html", f"Module {m['num']}: {m['name'].title()}", body)


def capstone():
    rub = "".join(f"<tr><th>{e(n)} · {p}</th><td>{e(d)}</td></tr>" for n, p, d in C.CAPSTONE["rubric"])
    body = f"""
<div class="hero"><div class="wrap">
  <p class="eyebrow">Days 19 and 20 · 50 points</p>
  <h1>Capstone Pitch Competition</h1>
  <p class="lead">{e(C.CAPSTONE['summary'])}</p>
</div></div>

<section class="alt"><div class="wrap grid g2">
  <div class="card course"><p class="eyebrow">Part 1 · due Day 19</p><h3>Business Portfolio</h3>
    <ul>{"".join(f"<li>{e(x)}</li>" for x in C.CAPSTONE["portfolio"])}</ul>{canvas_btn("CAP", "Upload in Canvas")}</div>
  <div class="card course c2"><p class="eyebrow">Part 2 · Day 20</p><h3>The Pitch</h3>
    <ul>{"".join(f"<li>{e(x)}</li>" for x in C.CAPSTONE["pitch"])}</ul></div>
</div></section>

<section><div class="wrap">
  <h2>How the panel scores you</h2>
  <table class="facts">{rub}</table>
  <div class="note">{e(C.CAPSTONE['awards'])}</div>
  <div class="own-words"><b>Practice out loud</b><ul>
    <li>“The problem I solve is … for …”</li>
    <li>“I know people will pay because … (what my interviews and survey showed).”</li>
    <li>“It costs … to start, I charge …, and I break even after … sales.”</li>
    <li>“What I need next is …”</li></ul></div>
</div></section>"""
    page("capstone.html", "Capstone", body)


def reentry():
    groups = "".join(f"""
  <details class="acc" style="margin-top:12px"{' open' if i == 0 else ''}><summary><span class="acc-head"><span class="acc-title">{e(g['area'])}</span></span></summary>
  <div class="acc-body"><table class="facts">{"".join(f'<tr><th><a href="{e(url)}" target="_blank" rel="noopener">{e(name)}</a></th><td>{e(desc)}</td></tr>' for name, url, desc in g["items"])}</table></div></details>"""
                     for i, g in enumerate(C.REENTRY_RESOURCES))
    tips = [d for d in C.DAYS if d.get("reentry")]
    body = f"""
<div class="hero"><div class="wrap">
  <p class="eyebrow">Support for returning citizens</p>
  <h1>Reentry Toolkit</h1>
  <p class="lead">Starting a business after time away means clearing a few extra hurdles: ID, debts to DC, a record, credit, supervision rules, and a world that went digital. None of these has to stop you. Here is where to start, and your case manager will walk each step with you.</p>
</div></div>

<section class="alt"><div class="wrap">
  <h2>Four things to check in week one</h2>
  <ol class="steps">
    <li><strong>ID</strong>You need a government photo ID to register a business and open a bank account.</li>
    <li><strong>Clean Hands</strong>DC will not license a business if you owe the District more than $100. Check on MyTax.DC.gov.</li>
    <li><strong>Supervision</strong>If you are on supervision, tell your officer about self-employment and check any limits on social media.</li>
    <li><strong>Credit</strong>Pull your free report. No history or old debts? We will build a plan.</li>
  </ol>
  <div class="note info">Your case manager meets with you in week one to go through these. Nothing you share is used to judge you, and you decide what to share.</div>
</div></section>

<section><div class="wrap">
  <h2>DC resources</h2>
  <p class="small">Programs and rules change. Your instructor checks these before each cohort.</p>
  {groups}
</div></section>

<section class="alt"><div class="wrap">
  <h2>Built into the lessons</h2>
  <table class="facts">{"".join(f'<tr><th><a href="modules/{next(m["key"] for m in C.MODULES if m["days"][0] <= d["n"] <= m["days"][1])}.html#day-{d["n"]}">Day {d["n"]}</a></th><td>{e(plain(d["reentry"]))}</td></tr>' for d in tips)}</table>
</div></section>

<section><div class="wrap">
  <div class="note">In crisis or need to talk? Call or text <a href="tel:988">988</a>, or call the DC Access Helpline at <a href="tel:18887934357">1-888-793-4357</a>, any time.</div>
</div></section>"""
    page("reentry.html", "Reentry Toolkit", body)


def main():
    C.check()
    index()
    getting_started()
    for i, m in enumerate(C.MODULES):
        module_page(m, C.MODULES[i - 1] if i else None, C.MODULES[i + 1] if i + 1 < len(C.MODULES) else None)
    capstone()
    reentry()
    print("Built", len(list(ROOT.glob("*.html"))) + len(list((ROOT / "modules").glob("*.html"))), "pages")


if __name__ == "__main__":
    main()
