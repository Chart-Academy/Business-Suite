"""Business Suite Curriculum: the single source for the ONSE curriculum document and the course website.

ONSE contract CW137729 (solicitation Doc814073). 60 instructional hours over 20 days (3 hours a day),
four modules: BUILD, BRAND, FINANCE, LAUNCH. Each day's agenda must add up to 180 minutes (build checks this).
Items marked CONFIRM are agency details to verify with the agency before each cohort.
"""

PROGRAM = {
    "title": "Business Suite Curriculum",
    "subtitle": "Entrepreneurship and Business Ownership Program",
    "contract": "CW137729",
    "solicitation": "Doc814073",
    "agency": "DC Office of Neighborhood Safety and Engagement (ONSE)",
    "program": "ONSE Pathways Program",
    "provider": "Center for Innovation, Research, and Transformation in Education (CIRTE), dba The Chart Academy",
    "partner": "Institute of Research for Social Justice and Action (IRSJA)",
    "hours": 60,
    "days": 20,
    "hours_per_day": 3,
    "cohort_size": "15 to 20 participants",
    "cohorts_per_year": "Up to 3",
    "population": ("ONSE Pathways participants, young adults ages 18 to 35, many of them returning citizens who are coming home "
                   "after months or years away and re-entering a city, an economy, and a technology landscape that changed "
                   "while they were gone."),
    "location": "529 14th Street NW, Suite 718, Washington, DC 20045 (Chart Academy), or another District-approved site",
    "schedule": "Monday to Friday, 3 hours a day within ONSE's standard operating hours (exact times set with ONSE for each cohort)",
}

# RFP C.5.5 required topics (and C.5.6.1 reference-guide topics). Codes are used to tag each day.
TOPICS = {
    "FIN": "Business finance and financial literacy",
    "PRICE": "Pricing strategies and revenue models",
    "BRAND": "Branding and marketing fundamentals",
    "SOCIAL": "Social media marketing and content strategy",
    "IP": "Protection of intellectual property and trademarks",
    "LIC": "Compliance with licensing and regulatory standards, and ethical business practices",
    "SPEAK": "Public speaking and professional communication",
    "NET": "Relationship building and networking",
    "WEALTH": "Wealth mindset and setting financial goals",
    "RESUME": "Resumes and interviews",
    "BANK": "Business banking and financial services",
}

STAFF = [
    ("Program Director", "Cedric Thompson, M.Ed.",
     "Overall program oversight, curriculum alignment, quality assurance, and ONSE relationship."),
    ("Subject Matter Expert, Curriculum Developer", "Dr. Jamila T. Davis (IRSJA)",
     "Developer of Boss Up, Money Moves, and Flipping the Game. Ensures curriculum fidelity and oversees implementation."),
    ("Lead Instructor / Facilitator (Key Personnel)", "Wayne Williams, PMP, CSM",
     "Primary in-person instruction, facilitation of learning activities, and instructional quality."),
    ("Case Management Associate", "Rasheed Murphy",
     "Attendance follow-up, barrier resolution, reentry resource connection, and coaching. Outreach after 2 consecutive absences."),
    ("Data Analyst", "Zerui Wu",
     "Attendance, assessment, and outcome data; daily progress reports, dashboards, and the final cohort report."),
    ("Operations and Reporting", "Alexus Faunteroy",
     "Deliverable tracking, invoicing, and compliance with contract reporting."),
    ("Guest Subject Matter Experts", "Partner network",
     "Master Class speakers: DLCP, SCORE, DC Chamber, GWBCC, Truist Bank, finance professionals, and local business owners."),
]

# The daily rhythm (the proposal's four-part instructional approach, plus a reentry-aware opening).
DAY_RHYTHM = [
    ("Open", "15 min", "Check-in circle, the day's goal, and a 5-minute Tech Catch-Up (one digital skill a day)."),
    ("Expert Content", "60 to 75 min", "Instructor-led lesson tied to the IRSJA reference guide for the module."),
    ("Field Experience or Master Class", "45 to 60 min", "Hands-on application with real markets, or a guest-led session."),
    ("Build", "20 to 30 min", "Each participant adds the day's piece to their own business portfolio."),
    ("Close", "10 min", "Exit ticket in Canvas (attendance and understanding check)."),
]

MODULES = [
    {
        "key": "build", "num": 1, "name": "BUILD", "days": (1, 5), "guide": "Boss Up",
        "focus": "Business setup and compliance",
        "summary": ("Lay the foundation: choose a business idea that fits the DC market, pick a legal structure, and map every "
                    "license, permit, and registration step, including the Clean Hands certificate."),
        "skills": "Business structure, licensing, ethics, and intellectual property",
        "project": "Business Plan Draft + DC Compliance Checklist",
        "project_items": ["Business idea and the problem it solves", "Chosen business structure and why",
                          "DC licenses, permits, and registration steps for this business", "Regulatory considerations",
                          "Ethical guidelines the business will follow", "How the business name will be protected"],
        "outcome": "A legally structured, registration-ready business plan.",
        "own_words": ['“I chose this business structure because …”', '“The compliance step that will take me the longest is … and my plan is …”'],
        "objectives": [
            "Choose a business structure (sole proprietorship, LLC, or other) that fits the business model and risk.",
            "Produce a complete DC compliance pathway: registration, EIN, Clean Hands, Basic Business License, and permits.",
            "Explain the ethical practices and intellectual property protections the business will use.",
        ],
        "rubric": [
            ("Business idea and plan", "States the idea, the customer, and the problem it solves, with all plan sections drafted.",
             "Idea is stated but the customer or problem is vague, or sections are missing.", "Plan is missing."),
            ("Business structure", "Chooses a structure and explains why it fits the business and its risk.",
             "Chooses a structure without a reason.", "No structure chosen."),
            ("DC compliance pathway", "Lists every registration, license, and permit step in order, with the agency for each.",
             "Lists some steps or misses the agency.", "Checklist is missing."),
            ("Ethics and IP", "Names at least three ethical practices and how the name will be protected.",
             "Names one or two, or skips IP.", "Missing."),
        ],
    },
    {
        "key": "brand", "num": 2, "name": "BRAND", "days": (6, 10), "guide": "Boss Up",
        "focus": "Branding and market validation",
        "summary": ("Find out what customers actually want before spending a dollar. Run customer interviews and a survey, "
                    "then build a brand, a social media plan, and an elevator pitch on that evidence."),
        "skills": "Customer discovery, brand identity, social media, and professional communication",
        "project": "Brand Kit",
        "project_items": ["Business name and tagline", "Logo (draft)", "Target audience profile from interviews and survey data",
                          "30-day social media content plan", "Capability statement (intro version)", "Elevator pitch (60 seconds)"],
        "outcome": "A customer-validated brand and market fit.",
        "own_words": ['“The most surprising thing a customer told me was …”', '“My brand is different from others in my market because …”'],
        "objectives": [
            "Build a data-informed target audience profile from 1:1 customer interviews and a survey.",
            "Develop a complete brand kit: name, tagline, logo, and market position.",
            "Deliver a 60-second elevator pitch and introduce yourself professionally at a networking event.",
        ],
        "rubric": [
            ("Customer evidence", "Summarizes at least 5 interviews and 15 survey responses and what they showed.",
             "Fewer interviews or responses, or no summary of what they showed.", "No customer evidence."),
            ("Brand identity", "Name, tagline, draft logo, and position statement are complete and consistent.",
             "One or two pieces missing or inconsistent.", "Brand kit missing."),
            ("Social media plan", "30-day plan with platform, audience, post types, and a weekly schedule.",
             "Plan is partial or not tied to the audience.", "No plan."),
            ("Pitch and capability statement", "Clear 60-second pitch and a one-page capability statement draft.",
             "Pitch runs long or is unclear, or statement is incomplete.", "Missing."),
        ],
    },
    {
        "key": "finance", "num": 3, "name": "FINANCE", "days": (11, 15), "guide": "Money Moves",
        "focus": "Financial planning and profitability",
        "summary": ("Build a financially viable business. Strengthen personal financial management, then set prices, build a revenue model, "
                    "and create startup and monthly budgets that a finance professional reviews."),
        "skills": "Financial literacy, pricing, revenue modeling, budgeting, banking, and funding",
        "project": "Revenue Model + Startup and Monthly Budget",
        "project_items": ["Pricing for each product or service (cost-based and value-based)", "Break-even point",
                          "12-month revenue model in Excel or Google Sheets", "Startup budget", "Monthly operating budget",
                          "Funding plan", "Personal financial goal statement"],
        "outcome": "A financially viable business model.",
        "own_words": ['“I set my price at … because …”', '“The number in my budget I am least sure about is … and I will check it by …”'],
        "objectives": [
            "Apply cost-based and value-based pricing to set profitable price points.",
            "Build a 12-month revenue model and defensible startup and monthly budgets in a spreadsheet.",
            "Open or plan a business bank account and write a personal financial goal statement.",
        ],
        "rubric": [
            ("Pricing", "Shows cost and value pricing for each offer and the break-even point.",
             "Uses one method only, or break-even is missing.", "No pricing."),
            ("Revenue model", "12-month model with units, price, and monthly revenue, tied to customer evidence.",
             "Model is incomplete or not tied to evidence.", "No model."),
            ("Budgets", "Startup and monthly budgets with every cost category and a funding source.",
             "One budget only, or categories missing.", "No budgets."),
            ("Financial goals", "Personal financial goal statement with a SMART goal and a banking step.",
             "Goal is vague or no banking step.", "Missing."),
        ],
    },
    {
        "key": "launch", "num": 4, "name": "LAUNCH", "days": (16, 20), "guide": "Flipping the Game",
        "focus": "Execution and presentation",
        "summary": ("Prepare for launch. Plan staffing, use AI tools, prepare a resume and interview skills for "
                    "income while you build, then pitch your business to a panel of business owners."),
        "skills": "Staffing, AI tools, resumes and interviews, stakeholder communication, and pitching",
        "project": "Capstone Business Portfolio + Final Pitch",
        "project_items": ["Business setup plan (Module 1)", "Brand kit (Module 2)", "Financial plan (Module 3)",
                          "Marketing strategy", "90-day launch plan", "Resume", "5-minute pitch with slides"],
        "outcome": "A launch-ready business validated by an external panel of business owners.",
        "own_words": ['“The problem my business solves is … for …”', '“My next three steps to launch are …”'],
        "objectives": [
            "Combine the business plan, brand, financial model, and marketing strategy into one capstone portfolio.",
            "Write a resume and answer interview questions, including how to talk about time away, with confidence.",
            "Deliver a formal pitch to a panel of business representatives.",
        ],
        "rubric": None,  # the capstone has its own 50-point rubric (CAPSTONE below)
    },
]

# Every day: 180 minutes. agenda = [(minutes, block, what happens)].
DAYS = [
    # ---------------- MODULE 1: BUILD ----------------
    {
        "n": 1, "title": "Orientation and Entrepreneurial Foundations", "topics": ["WEALTH", "FIN"],
        "objectives": ["Complete the pre-assessment and set up Canvas and email.",
                       "Name the business skills you already have from work, family, and the informal economy.",
                       "Write down three business ideas to test this week."],
        "agenda": [
            (20, "Open", "Welcome, introductions, group agreements, and what the next 20 days look like."),
            (30, "Assessment", "Pre-assessment in Canvas (knowledge and confidence). Staff help anyone who needs it."),
            (30, "Tech Catch-Up", "Log in to Canvas and email on the laptop and phone. Reset passwords, turn on two-step login."),
            (60, "Expert Content", "Flipping the Game: from informal enterprise to formal business. The skills you already have (sales, negotiation, "
                                   "managing money and people) and how they transfer to a legal business."),
            (30, "Build", "Business idea brainstorm: three ideas, who would pay, and why you."),
            (10, "Close", "Exit ticket: the idea you are most excited about, and one support you need this month."),
        ],
        "field": None, "master": None, "truist": None,
        "exit": "Which idea are you most excited about, and what is one support you need this month?",
        "reentry": ("Day one is about safety and belonging. Nobody is asked to share their story. The Case Management Associate "
                    "meets each participant this week for a short readiness review (ID, phone, housing, supervision schedule)."),
    },
    {
        "n": 2, "title": "Understanding a Business Plan", "topics": ["FIN", "BRAND"],
        "objectives": ["Explain the parts of a one-page business plan.",
                       "Match a business idea to real demand in DC (stadium, corridors, Ward 7 and 8 set-asides).",
                       "Choose one idea and start the business plan draft."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: saving and finding files in Google Drive."),
            (75, "Expert Content", "Understanding a Business Plan (Boss Up): the one-page plan and the business model canvas. "
                                   "Where DC's growth is: hospitality, retail, events, home and building services."),
            (40, "Field Experience", "Opportunity scan: small groups research one DC corridor or upcoming project and list "
                                     "the goods and services it will need."),
            (40, "Build", "Agent Lab BL-01: pick your idea and draft your one-page plan with the Business Plan Coach."),
            (10, "Close", "Exit ticket."),
        ],
        "field": "Opportunity scan of one DC corridor or development project.", "master": None, "truist": None,
        "exit": "Who is your customer, and what problem do you solve for them?",
        "reentry": "Many participants come home to a different DC. The opportunity scan doubles as a tour of what changed.",
        "lab": "BL-01",
    },
    {
        "n": 3, "title": "Business Structures and Registering in DC", "topics": ["LIC", "BANK", "FIN"],
        "objectives": ["Compare sole proprietorship, LLC, partnership, and corporation.",
                       "List the steps to register a business in DC, including an EIN and a Clean Hands certificate.",
                       "Explain why business and personal money stay separate."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: making an account on a government website safely."),
            (60, "Expert Content", "Business structures and risk. DC registration path: DLCP CorpOnline, IRS EIN, OTR "
                                   "tax registration, Clean Hands certificate, Basic Business License."),
            (60, "Master Class", "Truist Bank, Bank On Your Success (session 1 of 4): business finance basics, business "
                                 "structure, and organizing your finances."),
            (35, "Build", "Choose your structure, start your DC Compliance Checklist, and fill in the Licensing Visit "
                          "Prep Sheet for tomorrow's trip to DLCP."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": None,
        "truist": "Business finance basics; business structure and organizing your finances.",
        "exit": "Which business structure fits your business, and why?",
        "reentry": ("Clean Hands: DC will not issue a business license to anyone who owes the District more than $100 in taxes, "
                    "fines, or fees. Participants check their status on MyTax.DC.gov early, and case management helps set up "
                    "payment plans. Child support arrears are handled through the Child Support Services Division."),
    },
    {
        "n": 4, "title": "Licensing Field Trip: DC Department of Licensing and Consumer Protection", "topics": ["LIC"],
        "objectives": ["Walk through DC business registration and the Basic Business License with DLCP staff.",
                       "Identify the license category, endorsements, permits, and fees for your business.",
                       "Get answers to your prepared licensing questions and update your compliance checklist."],
        "agenda": [
            (15, "Arrival", "Meet at DLCP, sign in, pass building security, and review the visit plan."),
            (60, "Field Experience", "DLCP business licensing session: registering a business, the Basic Business License, "
                                     "license categories and endorsements, Certificate of Occupancy and home occupation "
                                     "permits, inspections, renewals, and how licensing considers records."),
            (45, "Field Experience", "Small Business Resource Center: in pairs, look up your license category and fees with "
                                     "a licensing specialist and ask your prepared questions."),
            (30, "Build", "On-site work time: update your DC Compliance Checklist with what you learned."),
            (30, "Close", "Group debrief, exit ticket in Canvas, and dismissal or travel back together."),
        ],
        "field": "Field trip to DLCP: business licensing session and Small Business Resource Center.",
        "master": "DLCP licensing staff.", "truist": None, "trip": True,
        "exit": "What did you learn at DLCP that changes your compliance checklist?",
        "reentry": ("Bring a photo ID for building security. Anyone without one tells their case manager by Day 2 so staff can "
                    "arrange entry. Questions about how a record affects licensing can be asked privately, and the class covers "
                    "where to get free legal help with record sealing (CONFIRM current rules and legal-aid contacts before each cohort)."),
    },
    {
        "n": 5, "title": "Ethics, Intellectual Property, and Technical Assistance Lab", "topics": ["IP", "LIC"],
        "objectives": ["Write three ethical rules your business will follow.",
                       "Explain trademarks, copyright, and trade names, and search the USPTO database.",
                       "Get one-on-one help from a DC small business technical assistance provider.",
                       "Submit the Module 1 project."],
        "agenda": [
            (15, "Open", "Check-in. Field trip debrief and compliance checklist peer check."),
            (30, "Expert Content", "Ethical Business Practices (Boss Up): contracts, honest pricing, paying taxes, and "
                                   "treating workers and customers fairly."),
            (30, "Expert Content", "Protection of Intellectual Property and Trademarks (Boss Up): searching USPTO and the DC "
                                   "trade name registry before you print anything."),
            (60, "Field Experience", "Technical Assistance Lab with DC APEX Accelerator and DSLBD Small Biz Assist "
                                     "(on site or at the MLK Library)."),
            (35, "Build", "Finish and submit the Module 1 project: Business Plan Draft + DC Compliance Checklist."),
            (10, "Close", "Module 1 reflection in Canvas."),
        ],
        "field": "Technical Assistance Lab: DC APEX Accelerator and DSLBD Small Biz Assist.", "master": None, "truist": None,
        "exit": "What is the next registration step you will take, and when?",
        "reentry": "Staff walk anyone without a working email or phone number through getting one before the lab.",
        "project": "build",
    },
    # ---------------- MODULE 2: BRAND ----------------
    {
        "n": 6, "title": "Customer Discovery", "topics": ["BRAND", "SPEAK"],
        "objectives": ["Write a customer interview script that avoids leading questions.",
                       "Practice interviews in pairs and start real interviews.",
                       "Describe a first-draft target customer."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: recording notes on your phone."),
            (60, "Expert Content", "Customer discovery: the five questions that tell you if people will pay."),
            (60, "Field Experience", "Customer interviews: practice in pairs, then interview at least two real people "
                                     "(by phone, on site, or in the community)."),
            (35, "Build", "Draft your target customer profile."),
            (10, "Close", "Exit ticket."),
        ],
        "field": "1:1 customer interviews (goal: 5 by Day 10).", "master": None, "truist": None,
        "exit": "What surprised you in your first interviews?",
        "reentry": ("Approaching strangers can be hard after years away. Scripts and pair practice come first, and participants "
                    "may start with people they already know."),
    },
    {
        "n": 7, "title": "Market Research and Demand Validation", "topics": ["BRAND", "PRICE"],
        "objectives": ["Build a market research survey in Google Forms.",
                       "Ask about price, preferences, and buying habits.",
                       "Send the survey to at least 15 target customers."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: making a Google Form and sharing a link by text."),
            (60, "Expert Content", "Market research basics: survey questions that give honest answers, and reading the results."),
            (60, "Field Experience", "Agent Lab BL-02, part 1: draft survey questions with the Market Research Assistant, "
                                     "rewrite them in your own words, test with a partner, and send your survey."),
            (35, "Build", "Brand identity worksheet: values, personality, and what makes you different."),
            (10, "Close", "Exit ticket."),
        ],
        "field": "Market research survey sent to target customers (goal: 15 responses).", "master": None, "truist": None,
        "lab": "BL-02",
        "exit": "What is one question in your survey that will help you set your price?",
        "reentry": None,
    },
    {
        "n": 8, "title": "Brand Identity Development", "topics": ["BRAND", "IP", "BANK"],
        "objectives": ["Create a business name, tagline, and draft logo.",
                       "Check that the name is available as a trademark and a web domain.",
                       "Explain why business and personal accounts stay separate."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: using Canva on the laptop."),
            (45, "Expert Content", "Branding fundamentals and IP and Trademark Basics (Boss Up): name, tagline, colors, logo, "
                                   "position statement, and checking the name is free to use."),
            (60, "Master Class", "Truist Bank, Bank On Your Success (session 2 of 4): separating business and personal "
                                 "finances, financial accounts and tools."),
            (50, "Build", "Mentorship session with SCORE mentors while you build your logo and brand kit in Canva."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": "SCORE mentors (mentor matching begins).",
        "truist": "Separating business and personal finances; financial accounts and tools.",
        "exit": "Share your business name and tagline.",
        "reentry": None,
    },
    {
        "n": 9, "title": "Social Media Marketing and Content Strategy", "topics": ["SOCIAL", "BRAND"],
        "objectives": ["Choose the right platforms for your customer.",
                       "Build a 30-day content plan.",
                       "Protect your privacy and reputation online."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: business accounts on Instagram, Facebook, TikTok, and Google Business Profile."),
            (60, "Expert Content", "Social Media Marketing Strategies (Boss Up): content types, posting schedule, simple "
                                   "metrics, and using AI to draft posts."),
            (45, "Master Class", "DC Chamber of Commerce speaker on local brand visibility."),
            (50, "Build", "Draft your 30-day content plan and your first three posts."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": "DC Chamber of Commerce: local brand visibility.", "truist": None,
        "exit": "Which platform will you use first, and why?",
        "reentry": ("Social media has changed a lot. Participants under supervision check whether their conditions limit social "
                    "media use before opening business accounts. The class covers scams, privacy settings, and keeping a "
                    "business page separate from a personal one."),
    },
    {
        "n": 10, "title": "Professional Communication and Networking", "topics": ["SPEAK", "NET"],
        "objectives": ["Deliver a 60-second elevator pitch.",
                       "Tell your story on your own terms, including how (or whether) to talk about time away.",
                       "Attend a networking event and follow up professionally."],
        "agenda": [
            (15, "Open", "Check-in. Review checkpoint: elevator pitch practice with peer feedback."),
            (60, "Expert Content", "Public Speaking and Professional Communication; Networking and Relationship Building "
                                   "(Boss Up): introductions, business cards, follow-up messages, and the capability statement."),
            (45, "Field Experience", "Networking: attend a DC small business or Greater Washington Black Chamber of Commerce "
                                     "event (or a facilitated networking session in class if no event falls this week)."),
            (50, "Build", "Agent Lab BL-02, part 2: analyze your real interview notes and survey results, then finish "
                          "and submit the Module 2 project: Brand Kit."),
            (10, "Close", "Module 2 reflection in Canvas."),
        ],
        "field": "Networking event (GWBCC or DC small business event).", "master": None, "truist": None,
        "exit": "Who did you meet, and what is your follow-up?",
        "reentry": ("Your story, your terms: participants practice a short, forward-looking way to explain a gap if they choose, "
                    "and learn they never have to disclose more than the law requires."),
        "project": "brand",
    },
    # ---------------- MODULE 3: FINANCE ----------------
    {
        "n": 11, "title": "Personal Financial Management and Credit", "topics": ["FIN", "WEALTH", "BANK"],
        "objectives": ["Build a personal monthly budget.",
                       "Pull your free credit report and read it.",
                       "Make a plan for fines, fees, debts, and rebuilding credit."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: banking apps, Zelle, Cash App, and avoiding payment scams."),
            (75, "Expert Content", "Financial Literacy (Money Moves): budgeting, credit scores, credit reports, secured cards, "
                                   "and second-chance bank accounts."),
            (60, "Field Experience", "Credit check lab: pull your free report at AnnualCreditReport.com and mark anything to fix."),
            (20, "Build", "Personal budget worksheet."),
            (10, "Close", "Exit ticket."),
        ],
        "field": "Credit report lab.", "master": None, "truist": None,
        "exit": "What is one thing on your credit report you will work on?",
        "reentry": ("People returning after years away may have no credit history, old debts, or identity theft. Pulling a credit "
                    "report is private and optional; case management helps dispute errors and find second-chance banking."),
    },
    {
        "n": 12, "title": "Business Finance: Costs and Cash Flow Management", "topics": ["FIN"],
        "objectives": ["Separate fixed and variable costs.",
                       "Explain cash flow and how a business owner pays themselves.",
                       "Start a startup budget in a spreadsheet."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: spreadsheet basics (cells, sums, and copying a formula)."),
            (75, "Expert Content", "Business Finance (Money Moves): startup costs, fixed and variable costs, cash flow, "
                                   "profit, and taxes to set aside."),
            (60, "Field Experience", "Spreadsheet lab: build your startup budget in Excel or Google Sheets."),
            (20, "Build", "List every monthly cost for your business."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": None, "truist": None,
        "exit": "What is your biggest startup cost?",
        "reentry": "Spreadsheets may be new. Staff pair participants and use a fill-in template so nobody starts from a blank sheet.",
    },
    {
        "n": 13, "title": "Pricing Strategies and Revenue Models", "topics": ["PRICE", "FIN"],
        "objectives": ["Set prices using cost-based and value-based methods.",
                       "Find your break-even point.",
                       "Build a 12-month revenue model."],
        "agenda": [
            (15, "Open", "Check-in. Review checkpoint: pricing exercise (cost-based vs. value-based)."),
            (60, "Expert Content", "Pricing Strategies and Revenue Models (Money Moves): markup, value pricing, bundles, "
                                   "subscriptions, contracts, and break-even."),
            (45, "Master Class", "Selling the vision: communicating pricing, value, and financial viability to customers, "
                                 "partners, and stakeholders."),
            (50, "Build", "Agent Lab BL-03: check your costs and break-even with the Pricing and Budget Analyst, then "
                          "build your revenue model from your survey's price data."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": "Selling the vision: communicating price and value.", "truist": None,
        "lab": "BL-03",
        "exit": "What is your price, and how many sales do you need to break even?",
        "reentry": None,
    },
    {
        "n": 14, "title": "Business Funding and Capital Access", "topics": ["FIN", "BANK"],
        "objectives": ["Compare savings, microloans, grants, and community lenders.",
                       "Explain what lenders look for.",
                       "Create a business borrowing profile."],
        "agenda": [
            (15, "Open", "Check-in. Draft budget review with feedback."),
            (60, "Expert Content", "Funding Your Business (Money Moves): DC grants and programs (DSLBD), CDFIs, microloans, "
                                   "and avoiding predatory lenders."),
            (60, "Master Class", "Truist Bank, Bank On Your Success (session 3 of 4): borrowing for small business, where to "
                                 "find funding, what lenders look for, and creating your borrowing profile."),
            (35, "Build", "Funding plan: how you will pay for your startup budget."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": None,
        "truist": "Borrowing for small business; where to find funding; what lenders look for; your borrowing profile.",
        "exit": "Where will your startup money come from?",
        "reentry": "Case management connects participants to opening a business bank account with Truist or another partner.",
    },
    {
        "n": 15, "title": "Wealth Building, Financial Goals, and Plan Review", "topics": ["WEALTH", "FIN", "PRICE"],
        "objectives": ["Write a personal financial goal statement.",
                       "Present your pricing, revenue model, and budget to a finance professional.",
                       "Submit the Module 3 project."],
        "agenda": [
            (15, "Open", "Check-in."),
            (45, "Expert Content", "Cultivating a Wealth Mindset and Setting Financial Goals (Money Moves, Flipping the Game): "
                                   "short-term survival vs. long-term wealth, SMART money goals."),
            (60, "Field Experience", "Finance professionals review each participant's pricing, revenue model, and budget."),
            (50, "Build", "Revise with feedback and submit the Module 3 project."),
            (10, "Close", "Module 3 reflection in Canvas."),
        ],
        "field": "Finance professional review of pricing, revenue model, and budget.", "master": None, "truist": None,
        "exit": "What is your 12-month money goal?",
        "reentry": None,
        "project": "finance",
    },
    # ---------------- MODULE 4: LAUNCH ----------------
    {
        "n": 16, "title": "Staffing Strategy and Artificial Intelligence in Business", "topics": ["FIN", "LIC"],
        "objectives": ["Compare employees, contractors, and partners, and the rules for each.",
                       "Use AI tools for business tasks (drafting, planning, customer messages) safely.",
                       "Start the marketing strategy for the portfolio."],
        "agenda": [
            (15, "Open", "Check-in. Tech Catch-Up: trying an AI assistant on a phone."),
            (60, "Expert Content", "Understanding Staffing Needs and Types; Leveraging Artificial Intelligence (Flipping the Game)."),
            (60, "Field Experience", "AI lab: review the agents you built, set your privacy rules, and use AI to draft your "
                                     "marketing strategy, a customer email, and pitch slide outlines, then fact-check and edit them."),
            (35, "Build", "Marketing strategy section of the capstone portfolio."),
            (10, "Close", "Exit ticket."),
        ],
        "field": "AI business tools lab.", "master": None, "truist": None,
        "exit": "Name one task AI will help you with, and one thing you will always check yourself.",
        "reentry": "AI tools did not exist in this form a few years ago. The lab starts from zero and covers privacy and scams.",
    },
    {
        "n": 17, "title": "Resume Development and Interview Preparation", "topics": ["RESUME", "SPEAK"],
        "objectives": ["Write a resume that shows business and life skills.",
                       "Answer common interview questions, including questions about time away.",
                       "Know your rights under DC fair-chance hiring law."],
        "agenda": [
            (15, "Open", "Check-in."),
            (60, "Expert Content", "Resume and interview preparation: an entrepreneur's resume, filling gaps honestly, and "
                                   "the STAR method. Many owners keep a job while the business grows."),
            (60, "Field Experience", "Mock interviews with staff and partners, with written feedback."),
            (35, "Build", "Resume draft in Canvas; capability statement final version."),
            (10, "Close", "Exit ticket."),
        ],
        "field": "Mock interviews.", "master": None, "truist": None,
        "exit": "How will you answer 'Tell me about yourself'?",
        "reentry": ("DC's Fair Criminal Record Screening law limits when most employers may ask about records (CONFIRM current "
                    "rules before each cohort). Participants practice a short, honest, forward-looking answer about gaps."),
    },
    {
        "n": 18, "title": "Investor and Stakeholder Communication", "topics": ["SPEAK", "BANK", "NET"],
        "objectives": ["Build a 5-minute pitch with slides.",
                       "Explain what investors, lenders, and partners want to hear.",
                       "Learn how to build, expand, and protect a business."],
        "agenda": [
            (15, "Open", "Check-in."),
            (45, "Expert Content", "Investor and Stakeholder Communication; Presentation Strategy (Flipping the Game)."),
            (45, "Master Class", "The Business Owner: recent business owners on launch, early challenges, and first customers."),
            (45, "Master Class", "Truist Bank, Bank On Your Success (session 4 of 4): build and expand your business, "
                                 "manage cash flow, and protect your business."),
            (20, "Build", "Pitch slides draft."),
            (10, "Close", "Exit ticket."),
        ],
        "field": None, "master": "Recent business owners on launch execution.",
        "truist": "Build and expand your business; manage cash flow; protect your business.",
        "exit": "What is the one sentence you want the panel to remember?",
        "reentry": None,
    },
    {
        "n": 19, "title": "Pitch Rehearsal and Portfolio Completion", "topics": ["SPEAK"],
        "objectives": ["Rehearse the pitch and use critique to improve it.",
                       "Finish the capstone portfolio and 90-day launch plan.",
                       "Confirm next steps with case management."],
        "agenda": [
            (15, "Open", "Check-in. Review checkpoint."),
            (75, "Field Experience", "Agent Lab BL-04: practice panel questions with the Pitch Coach, then rehearse in small "
                                     "groups with peer and instructor critique (timed, with the rubric)."),
            (70, "Build", "Finish the capstone portfolio and 90-day launch plan. Upload to Canvas."),
            (20, "Close", "Next-steps meeting sign-up with case management; attire and logistics for the capstone."),
        ],
        "field": "Pitch rehearsals with critique.", "master": None, "truist": None,
        "lab": "BL-04",
        "exit": "What will you change after today's rehearsal?",
        "reentry": "Dress for Success package (attire, headshots, business cards) is delivered before the capstone.",
    },
    {
        "n": 20, "title": "Capstone Pitch Competition", "topics": ["SPEAK", "NET"],
        "objectives": ["Pitch your business to an external panel.",
                       "Complete the post-assessment.",
                       "Leave with a plan, a network, and your next steps."],
        "agenda": [
            (15, "Open", "Welcome guests, panel, families, and ONSE staff."),
            (105, "Capstone", "Pitch competition: each participant delivers a 5-minute pitch plus panel questions, scored on "
                              "viability, clarity, financial readiness, and market alignment."),
            (25, "Assessment", "Post-assessment in Canvas and program evaluation survey."),
            (35, "Close", "Awards (top three receive a $500 startup package), certificates, GWBCC membership activation, and "
                          "next steps."),
        ],
        "field": "Pitch competition before an external panel.", "master": None, "truist": None,
        "exit": None,
        "reentry": ("Graduates keep Canvas access, their reference guides, the GWBCC membership, and follow-up from case "
                    "management after the program ends."),
        "project": "launch",
    },
]

CAPSTONE = {
    "summary": ("Every participant presents their business to a panel of established business owners and professionals. "
                "The capstone has two parts: the Business Portfolio (submitted in Canvas by Day 19) and the Pitch (Day 20)."),
    "portfolio": ["Business setup plan and DC compliance checklist", "Brand kit", "Financial plan: pricing, revenue model, budgets",
                  "Marketing strategy and 30-day content plan", "90-day launch plan", "Resume"],
    "pitch": ["5 minutes, with up to 8 slides", "The problem and your customer", "Your business and why you",
              "Evidence from interviews and the survey", "Price, revenue, and what it costs to start",
              "Your ask: what you need next", "3 to 5 minutes of panel questions"],
    "awards": "The top three pitches receive a $500 startup package for licensing, incorporation, and launch.",
    "rubric": [
        ("Viability", 10, "The business solves a real problem for a defined customer, backed by interview and survey evidence."),
        ("Financial readiness", 10, "Prices, revenue model, budgets, and funding plan are complete and realistic."),
        ("Market alignment", 10, "The business fits a real DC market opportunity and has a clear marketing strategy."),
        ("Clarity and delivery", 10, "The pitch is clear, on time, and confident, and the answers to questions are direct."),
        ("Portfolio completeness", 10, "All six portfolio pieces are submitted and consistent with each other."),
    ],
}

ASSESSMENT = [
    ("Pre-assessment", "Day 1", "25 items: 20 knowledge questions across the RFP topics and 5 confidence ratings. Results summary "
                                "sent to ONSE on or before Day 1."),
    ("Exit tickets", "Every day", "One or two questions in Canvas. Also records daily participation."),
    ("Review checkpoints", "Days 5, 10, 13, 14, 19", "Peer and instructor checks before each module project."),
    ("Module projects", "Days 5, 10, 15", "Three projects, 20 points each (4 rows x 5 points: Full 5, Partial 3, Not yet 1)."),
    ("Capstone", "Days 19 and 20", "Portfolio and pitch, 50 points, scored by an external panel and the instructor."),
    ("Post-assessment", "Day 20", "Same 25 items as the pre-assessment, so growth can be measured for each participant."),
    ("Program evaluation", "Day 20", "Participant satisfaction and feedback survey; results feed the final cohort report."),
]

# Course grade weights (approved by Cedric Thompson, October 24, 2026)
WEIGHTS = [
    ("Participation", "Daily attendance, exit tickets, and the four Agent Labs, submitted in Canvas", 20),
    ("Module projects", "Module 1, 2, and 3 projects (15% each), submitted in Canvas", 45),
    ("Capstone", "Business portfolio (15%) and pitch (20%)", 35),
]

COMPLETION = ("A participant completes the program by attending at least 80% of instructional hours (48 of 60), submitting "
              "the three module projects, and delivering the capstone pitch. (Proposed; confirm with ONSE.)")

STANDARDS = [
    ("RFP C.5.5 required topics", "Every required topic is taught in at least one Expert Content session and practiced in a "
                                  "project (see the topic crosswalk)."),
    ("National Content Standards for Entrepreneurship Education (Consortium for Entrepreneurship Education)",
     "Entrepreneurial Skills (processes, traits and behaviors); Ready Skills (business foundations, communication, digital "
     "skills, financial literacy, professional development); Business Functions (financial, marketing, operations, risk, "
     "human resources, and strategic management)."),
    ("Jump$tart National Standards for Personal Financial Education (2021)",
     "Earning income, spending, saving, managing credit, and managing risk (Module 3)."),
    ("U.S. Department of Education Employability Skills Framework",
     "Applied knowledge, effective relationships, and workplace skills (communication, resources, technology use)."),
]

TEACHING = [
    ("Trauma-informed, culturally responsive facilitation",
     "Predictable routine every day, choice in what to share, no forced disclosure, and staff with lived experience."),
    ("Adult learning", "Every lesson is applied the same day to the participant's own business."),
    ("Learn, do, show", "Expert Content, then Field Experience or Master Class, then a portfolio piece and an exit ticket."),
    ("Peer learning", "Pairs and small groups for interviews, critique, and pitch rehearsal."),
    ("Real-world exposure", "Master Classes, networking events, and finance professional reviews every week."),
    ("Blended learning", "In-person class with Canvas for materials, templates, submissions, and attendance."),
]

DIVERSE_LEARNERS = [
    ("Reentry supports", "A short readiness review in week 1 (ID, phone, housing, supervision schedule, Clean Hands status), "
                         "with the Case Management Associate following up on each barrier."),
    ("Digital catch-up", "A 5-minute Tech Catch-Up opens most days, so participants who have been away build phone, email, "
                         "Canvas, spreadsheet, and AI skills in small steps. Laptops are provided."),
    ("Supervision-friendly scheduling", "Staff work with participants who have check-ins with CSOSA or other supervision, and "
                                        "provide attendance letters on request."),
    ("Reading and language", "Plain-language materials, read-aloud of key directions, visual templates, and fill-in worksheets."),
    ("Different paces", "Every assignment has a must-do core and an optional stretch; office hours before class for catch-up."),
    ("Accommodations", "Participants can ask for accommodations at intake or any time; staff adjust seating, timing, and formats."),
    ("Wellness", "Staff know the warning signs of crisis and connect participants to 988 and the DC Access Helpline."),
]

ENHANCEMENTS = [
    ("Social capital (C.5.2.1a, C.5.9)", "A field trip to the DC Department of Licensing and Consumer Protection; Master "
                                        "Classes with DC Chamber, SCORE, and local business owners; a networking event; an "
                                        "external pitch panel; and a one-year Greater Washington Black Chamber of Commerce "
                                        "membership."),
    ("Mentorship (C.5.2.1b, C.5.10)", "SCORE mentor matching in Module 2, group mentoring in Master Classes, and finance "
                                      "professional reviews in Module 3."),
    ("Financial institution (C.5.2.1c, C.5.11)", "Truist Bank, Bank On Your Success: four weekly sessions (Days 3, 8, 14, 18) "
                                                 "on business accounts, financial products, credit building, and banking "
                                                 "best practices, with referrals to open business accounts."),
    ("Participant readiness", "Laptop and professional bag, Dress for Success package (attire, headshots, business cards), "
                              "and continued Canvas access after the program."),
]

# DC resources for the reentry page. CONFIRM addresses, phone numbers, and program rules before each cohort.
REENTRY_RESOURCES = [
    {
        "area": "Getting back on the grid",
        "items": [
            ("Mayor's Office on Returning Citizen Affairs (MORCA)", "https://orca.dc.gov",
             "Help with IDs, referrals for housing, jobs, and benefits for people coming home."),
            ("DC DMV identification card", "https://dmv.dc.gov",
             "A REAL ID or DC ID is needed to register a business and open a bank account."),
            ("DC Vital Records (birth certificates)", "https://dchealth.dc.gov/service/vital-records",
             "Needed for many ID applications."),
            ("Free phone service (Lifeline)", "https://www.lifelinesupport.org", "Discounted phone or internet service."),
        ],
    },
    {
        "area": "Clean Hands, debts, and taxes",
        "items": [
            ("MyTax.DC.gov: Clean Hands certificate", "https://mytax.dc.gov",
             "Check whether you owe DC more than $100. You need a Clean Hands certificate for a business license."),
            ("DC Child Support Services Division", "https://cssd.dc.gov",
             "Ask about modifying an order or a payment plan, especially if your income changed while away."),
            ("IRS: get an EIN", "https://www.irs.gov/ein", "Free. Never pay a website to get an EIN."),
        ],
    },
    {
        "area": "Records and legal help",
        "items": [
            ("Public Defender Service for DC", "https://www.pdsdc.org", "Information on record sealing and reentry legal help."),
            ("Neighborhood Legal Services Program", "https://www.nlsp.org", "Free civil legal help for DC residents."),
            ("DC Courts Self-Help Center", "https://www.dccourts.gov/services/self-help-center",
             "Forms and guidance, including record sealing motions."),
        ],
    },
    {
        "area": "Starting a business in DC",
        "items": [
            ("DLCP: business licensing", "https://dlcp.dc.gov", "Register your business and apply for a Basic Business License."),
            ("DSLBD Small Biz Assist", "https://dslbd.dc.gov", "Free help from the Department of Small and Local Business Development."),
            ("DC APEX Accelerator", "https://dslbd.dc.gov/service/dc-apex-accelerator", "Help winning government contracts."),
            ("SCORE Washington DC", "https://www.score.org", "Free business mentors."),
            ("USPTO trademark search", "https://tmsearch.uspto.gov", "Check that your business name is free to use."),
            ("Greater Washington Black Chamber of Commerce", "https://www.gwbcc.org", "Your one-year membership comes with the program."),
        ],
    },
    {
        "area": "Money and banking",
        "items": [
            ("AnnualCreditReport.com", "https://www.annualcreditreport.com", "The only official site for free credit reports."),
            ("Truist: Bank On Your Success", "https://www.truist.com", "Program partner for business banking education."),
            ("Consumer Financial Protection Bureau", "https://www.consumerfinance.gov", "Credit, debt, and scam guidance."),
        ],
    },
    {
        "area": "Jobs, basic needs, and wellness",
        "items": [
            ("DOES Project Empowerment", "https://does.dc.gov", "Transitional employment for DC residents with barriers to work."),
            ("DC Access Helpline", "tel:18887934357", "1-888-793-4357, 24/7 mental health and substance use support."),
            ("988 Suicide and Crisis Lifeline", "tel:988", "Call or text 988, 24/7."),
            ("DC 211", "https://dc211.org", "Food, housing, utilities, and other help."),
        ],
    },
]

TECH_CATCHUP = [
    "Logging in to Canvas and email; strong passwords and two-step login",
    "Saving, finding, and sharing files in Google Drive",
    "Government websites: making an account safely, reading PDFs, and filling in forms",
    "Recording notes and voice memos on your phone",
    "Google Forms for surveys; sharing a link by text",
    "Canva for logos and flyers",
    "Business social media accounts and privacy settings",
    "Banking apps, Zelle and Cash App, and spotting payment scams",
    "Spreadsheet basics: cells, sums, and formulas",
    "AI assistants: what they are good at, and what to check yourself",
]


# Agent Labs: one AI agent per module, in the AI for Workforce Readiness course's Agent Lab format.
# Any free AI assistant works (Google Gemini, ChatGPT, Claude, or Microsoft Copilot).
AI_GUARD = ('AI Instructions: Before you start, ask me to explain in my own words what this agent is for and what I changed in the [brackets]. Do not continue until I answer in my own words.')

AGENT_LABS = [
    {
        "id": "BL-01", "day": 2, "module": "build", "name": "Business Plan Coach",
        "summary": "Interviews you one question at a time and turns your answers into a one-page business plan, "
                   "marking anything you still need to find out instead of guessing.",
        "tools": "AI assistant, Google Docs",
        "prompt": ("You are a business plan coach for a new small business owner in Washington, DC. My business idea is "
                   "[describe your idea in one sentence]. My customer is [who will pay for it]. Interview me one question at a "
                   "time to fill in a one-page business plan with these sections: Problem, Solution, Customer, Competition, How "
                   "I make money, Startup costs, Licenses to look up, and Next steps. Use only what I tell you. If I don't know "
                   "an answer, write TO FIND OUT instead of guessing. When we finish, show the plan as a table and list every "
                   "fact I still need to check."),
        "steps": ["Set up the Business Plan Coach with the starter instructions and fill in the [brackets].",
                  "Answer its questions one at a time, in your own words.",
                  "Highlight anything in the plan that you did not say. Delete it or check it.",
                  "Copy the plan into a Google Doc. Keep every TO FIND OUT item; you will answer the licensing ones at DLCP on Day 4."],
        "check": "AI can invent facts that sound right. Licenses, fees, and rules must come from DLCP, not from the AI.",
        "own_words": ["“The coach asked me … and that made me realize …”",
                      "“One thing the AI added that I did not say was … so I …”"],
        "upload": "Your one-page plan (Google Doc shared as Anyone with the link → Viewer) and your own-words answers.",
    },
    {
        "id": "BL-02", "day": 7, "module": "brand", "name": "Market Research Assistant",
        "summary": "Drafts unbiased survey questions, then organizes your real interview notes and survey results into "
                   "patterns, customer needs, and a price range, quoting the responses it used.",
        "tools": "AI assistant, Google Forms, Google Sheets",
        "prompt": ("You are a market research assistant for my small business in [neighborhood or ward], Washington, DC. I sell "
                   "[product or service] to [target customer]. Help me with three jobs, one at a time, and wait for me between "
                   "jobs. 1. Draft 8 survey questions for Google Forms about buying habits, price, and preferences, with no "
                   "leading questions. 2. When I paste my real interview notes and survey results, summarize the patterns, the "
                   "top 3 customer needs, and the price range customers named, and quote the responses you used. 3. List the "
                   "kinds of competitors I should look up near me and what to compare (price, hours, reviews, and what they "
                   "offer). Never invent customer responses, numbers, or business names. If I have not given you data, say so."),
        "steps": ["Day 7: ask for draft survey questions (job 1). Rewrite them in your own words, remove any that lead the "
                  "customer, and test the survey with a partner before you send it.",
                  "Days 7 to 10: send the survey and finish at least 5 real customer interviews. The AI cannot do this part.",
                  "Day 10: paste your interview notes and survey results (job 2). Check every quote against your notes.",
                  "Ask for the competitor list (job 3) and look up three real competitors yourself.",
                  "Use what you found in your target audience profile and brand kit."],
        "check": "Every customer quote and number must come from your own interviews and survey. If the AI shows a quote you "
                 "never collected, delete it.",
        "own_words": ["“The pattern I saw in my customers is …”",
                      "“A claim the AI made that my data did not support was …”"],
        "upload": "Your survey link, your results summary, your competitor notes, and your own-words answers.",
    },
    {
        "id": "BL-03", "day": 13, "module": "finance", "name": "Pricing and Budget Analyst",
        "summary": "Asks about costs new owners often forget, explains your break-even point with your own numbers, and "
                   "tests what happens to profit if your price changes.",
        "tools": "AI assistant, Excel or Google Sheets",
        "prompt": ("You are a pricing and budget analyst for a new small business in Washington, DC. I sell [product or "
                   "service] at [your price]. Here are my costs: [paste your startup and monthly costs]. 1. Ask me about costs "
                   "a business like mine often forgets, such as licenses, insurance, taxes, and fees, as questions, not numbers. "
                   "2. Explain my break-even point step by step using only my numbers, and show your math. 3. Show what happens "
                   "to my monthly profit if my price is 10% lower or 10% higher. Do not make up prices or costs. If a number is "
                   "missing, ask me for it."),
        "steps": ["Paste your cost list and answer the analyst's questions about missing costs.",
                  "Find real prices for anything missing (quotes, websites, or the DLCP fee schedule). Do not use AI guesses.",
                  "Rebuild the break-even math in your spreadsheet with formulas. Check that it matches the AI's math.",
                  "Bring the results to the finance professional review on Day 15."],
        "check": "AI can make math mistakes. Your spreadsheet formulas are the final answer, not the chat.",
        "own_words": ["“My break-even point is … which means I need to …”",
                      "“The AI's math was (right / wrong) when … I checked it by …”"],
        "upload": "Your budget and revenue spreadsheet (shared as Anyone with the link → Viewer) and your own-words answers.",
    },
    {
        "id": "BL-04", "day": 19, "module": "launch", "name": "Pitch Coach",
        "summary": "Scores your pitch script on the panel's four criteria, then plays a tough but fair panelist and asks "
                   "questions one at a time so you can practice your answers.",
        "tools": "AI assistant (voice mode works well)",
        "prompt": ("You are a pitch coach and a tough but fair panelist for a small business pitch competition in Washington, "
                   "DC. My business is [business name], and here is my 5-minute pitch script: [paste your script]. 1. Score it 1 "
                   "to 5 on viability, financial readiness, market alignment, and clarity, with one reason for each score. 2. Ask "
                   "me 5 questions a panel of DC business owners would ask, one at a time, and wait for my answer. 3. After each "
                   "answer, tell me one thing that worked and one thing to tighten. Do not rewrite my pitch for me. Tell me what "
                   "to change and let me change it."),
        "steps": ["Paste your own pitch script and read the scores.",
                  "Answer all 5 practice questions out loud or by typing, without notes.",
                  "Make your own changes to the script, then time yourself: 5 minutes or less.",
                  "Rehearse with your group and compare the AI's feedback with your classmates' feedback."],
        "check": "The panel scores you, not the AI. Use the coach to practice, and trust your classmates' and instructor's feedback too.",
        "own_words": ["“The hardest practice question was … and my answer now is …”",
                      "“The biggest change I made to my pitch was … because …”"],
        "upload": "Your revised pitch script and your own-words answers (submit with the capstone portfolio).",
    },
]

# Licensing field trip (Day 4). CONFIRM the address, visitor ID rules, and contacts with DLCP when booking each cohort.
FIELD_TRIP = {
    "day": 4,
    "host": "DC Department of Licensing and Consumer Protection (DLCP)",
    "address": "1100 4th Street SW, Washington, DC 20024",
    "transit": "Metro Green Line to Waterfront station, then a short walk",
    "length": "3 hours, including arrival and debrief",
    "bring": ["A government photo ID (needed for building security)",
              "Your phone, charged",
              "Your Licensing Visit Prep Sheet (filled in on Day 3)",
              "Your draft DC Compliance Checklist",
              "A pen and a folder for handouts"],
    "wear": "Business casual. You are meeting the agency that will license your business.",
    "know": ["Your business idea in one sentence",
             "Your business structure (sole proprietorship, LLC, or other)",
             "Where you plan to operate: from home, a storefront, a vehicle, events, or online",
             "Your Clean Hands status from MyTax.DC.gov, if you checked it"],
    "questions": ["What license category and endorsements fit my business?",
                  "Do I need a Certificate of Occupancy or a home occupation permit?",
                  "What will my license cost, and how long does it last?",
                  "Will my business need inspections or any other permits?",
                  "What should I do first, and what can wait until I have customers?",
                  "(Optional, ask privately) How could a criminal record affect my license, and where can I get help?"],
    "conduct": ["Arrive on time with your cohort; sign-in at DLCP counts for attendance.",
                "Phones on silent during the session; use them only for notes and lookups.",
                "Do not share personal information you are not comfortable sharing. Specialists can answer general questions.",
                "Stay with the group until staff dismiss you."],
    "after": ["Update your DC Compliance Checklist with every license, permit, and fee you learned about.",
              "Answer the exit ticket in Canvas.",
              "Bring your updated checklist to Day 5 for the peer check and the Technical Assistance Lab."],
    "staff_timeline": [
        ("4 weeks before", ["Request the visit from DLCP's small business or outreach team: date, time, group size (15 to 20 "
                            "plus staff), a licensing presentation, and Small Business Resource Center time.",
                            "Share the topics in the Day 4 agenda so the presenter can prepare.",
                            "Ask about visitor ID and security rules, accessibility, and whether names must be sent in advance."]),
        ("2 weeks before", ["Get the visit confirmed in writing, with the presenter's name and a day-of contact number.",
                            "Send the participant list if DLCP needs it for security.",
                            "Check each participant's supervision check-ins, work, and childcare for conflicts on Day 4.",
                            "Plan transit: meet at the site or travel together; load SmarTrip cards if the program covers fares.",
                            "Confirm accommodations for anyone who needs them."]),
        ("1 week before", ["Print the Licensing Visit Prep Sheet, sign-in sheet, and emergency contact list.",
                           "Case management confirms photo ID and Clean Hands status with each participant."]),
        ("Day 3", ["Hand out and go over the Prep Sheet in the Build block; each participant writes their questions.",
                   "Remind participants of the time, address, ID, and dress."]),
        ("Day before", ["Send a reminder text with the address, meeting time, and staff phone number.",
                        "Reconfirm with the DLCP contact."]),
        ("Day 4", ["Two staff on site. Headcount and sign-in at arrival and departure; the sign-in sheet is the attendance record.",
                   "Lead Instructor keeps time; Case Management Associate handles late arrivals and private questions.",
                   "Take photos only with participant consent."]),
        ("After the visit", ["Send a thank-you to DLCP the same week.",
                             "Record attendance in Canvas and the daily progress report to ONSE.",
                             "Note what to change for the next cohort's visit."]),
    ],
}


def module_days(mod):
    lo, hi = mod["days"]
    return [d for d in DAYS if lo <= d["n"] <= hi]


def check():
    assert len(DAYS) == PROGRAM["days"]
    assert sum(w for _, _, w in WEIGHTS) == 100, "Grade weights must add up to 100%"
    for d in DAYS:
        total = sum(m for m, _, _ in d["agenda"])
        assert total == 180, f"Day {d['n']} adds up to {total} minutes"
    for lab in AGENT_LABS:
        day = next(d for d in DAYS if d["n"] == lab["day"])
        assert day.get("lab") == lab["id"], f"{lab['id']} is not on Day {lab['day']}"
    assert next(d for d in DAYS if d["n"] == FIELD_TRIP["day"]).get("trip"), "Field trip day is not marked"
    covered = {t for d in DAYS for t in d["topics"]}
    missing = set(TOPICS) - covered
    assert not missing, f"Topics never taught: {missing}"
    return sum(sum(m for m, _, _ in d["agenda"]) for d in DAYS) / 60


if __name__ == "__main__":
    print(f"{check():.0f} instructional hours across {len(DAYS)} days; every required topic covered.")
