from django.core.management.base import BaseCommand
from SkillPath.models import Skill, Course, Career


SKILLS = [
    ("Python Programming", "Write Python scripts and programs to solve computational problems.", "technical"),
    ("Object-Oriented Design", "Design software using classes, inheritance, and encapsulation.", "technical"),
    ("Data Structures", "Choose and implement appropriate data structures for a given problem.", "technical"),
    ("Algorithm Design", "Analyse and design efficient algorithms with Big-O complexity.", "technical"),
    ("Functional Programming", "Apply pure functions, recursion, and immutability in Haskell.", "technical"),
    ("Formal Verification", "Prove program correctness using logic and formal methods.", "technical"),
    ("Computer Architecture", "Understand CPU, memory, assembly language, and digital logic.", "technical"),
    ("Embedded Systems", "Program microcontrollers and interface with hardware peripherals.", "technical"),
    ("Compiler Design", "Build lexers, parsers, and code generators for a programming language.", "technical"),
    ("Web Development", "Build dynamic web applications using HTML, CSS, JavaScript, and frameworks.", "technical"),
    ("SQL & Databases", "Design schemas and write queries using relational databases.", "data"),
    ("Data Analysis", "Clean, transform, and summarise datasets using statistical methods.", "data"),
    ("Machine Learning", "Train and evaluate supervised and unsupervised ML models.", "data"),
    ("Statistical Modelling", "Apply regression, hypothesis testing, and probability distributions.", "data"),
    ("Data Visualisation", "Communicate data insights through effective charts and dashboards.", "data"),
    ("AI Problem Solving", "Formulate and solve AI search, constraint, and planning problems.", "data"),
    ("UX Research", "Conduct user interviews, usability tests, and synthesise findings.", "research"),
    ("Interaction Design", "Design usable interfaces applying HCI principles and prototyping.", "research"),
    ("User Needs Analysis", "Identify and prioritise user needs through observation and research.", "research"),
    ("Advanced Prototyping", "Build high-fidelity interactive prototypes and conduct design critiques.", "research"),
    ("Discrete Mathematics", "Apply logic, sets, graphs, and combinatorics to computing problems.", "technical"),
    ("System Design", "Architect scalable, maintainable software systems.", "technical"),
    ("Version Control", "Use Git for collaborative software development.", "technical"),
    ("Technical Communication", "Write clear technical documentation and present findings.", "research"),
    ("Project Management", "Plan, scope, and deliver software projects using agile methods.", "business"),
]


COURSES = [
    {
        "code": "CSSE1001",
        "name": "Introduction to Software Engineering",
        "description": "Introduces programming using Python, covering problem decomposition, functions, data types, and basic software engineering practices.",
        "difficulty": "easy",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Python Programming", "Version Control", "Technical Communication"],
    },
    {
        "code": "CSSE2002",
        "name": "Programming in the Large",
        "description": "Covers object-oriented design, software testing, and design patterns using Java for building larger, maintainable systems.",
        "difficulty": "medium",
        "workload": "10-12 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Object-Oriented Design", "System Design", "Version Control"],
    },
    {
        "code": "COMP3506",
        "name": "Algorithms & Data Structures",
        "description": "Rigorous study of fundamental algorithms and data structures, with emphasis on correctness proofs and complexity analysis.",
        "difficulty": "hard",
        "workload": "12-15 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Algorithm Design", "Data Structures", "Discrete Mathematics"],
    },
    {
        "code": "COMP1100",
        "name": "Introduction to Functional Programming",
        "description": "Introduces functional programming using Haskell, covering recursion, higher-order functions, and type systems.",
        "difficulty": "medium",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Functional Programming", "Algorithm Design", "Formal Verification"],
    },
    {
        "code": "DECO2500",
        "name": "Human-Computer Interaction",
        "description": "Explores HCI principles, usability evaluation, and user-centred design processes for interactive systems.",
        "difficulty": "easy",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Project + Report",
        "skills": ["UX Research", "Interaction Design", "User Needs Analysis"],
    },
    {
        "code": "INFS2200",
        "name": "Relational Database Systems",
        "description": "Covers relational database design, SQL, normalisation, transactions, and query optimisation.",
        "difficulty": "medium",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["SQL & Databases", "Data Analysis", "System Design"],
    },
    {
        "code": "COMP3702",
        "name": "Artificial Intelligence",
        "description": "Covers AI foundations including search algorithms, constraint satisfaction, Bayesian networks, and reinforcement learning.",
        "difficulty": "hard",
        "workload": "12-15 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["AI Problem Solving", "Algorithm Design", "Python Programming"],
    },
    {
        "code": "COMP4702",
        "name": "Machine Learning",
        "description": "In-depth study of machine learning theory and practice, including neural networks, SVMs, and model evaluation.",
        "difficulty": "hard",
        "workload": "12-15 hrs/wk",
        "assessment_type": "Assignments + Project",
        "skills": ["Machine Learning", "Statistical Modelling", "Data Analysis", "Python Programming"],
    },
    {
        "code": "STAT2201",
        "name": "Analysis of Scientific Data",
        "description": "Applies statistical methods to scientific data, covering experimental design, regression, and hypothesis testing using R.",
        "difficulty": "medium",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Statistical Modelling", "Data Analysis", "Data Visualisation"],
    },
    {
        "code": "CSSE2010",
        "name": "Introduction to Computer Systems",
        "description": "Covers computer architecture, assembly language (AVR), digital logic, memory systems, and C programming for embedded systems.",
        "difficulty": "medium",
        "workload": "10-12 hrs/wk",
        "assessment_type": "Project + Exam",
        "skills": ["Computer Architecture", "Embedded Systems", "Algorithm Design"],
    },
    {
        "code": "INFS3202",
        "name": "Web Information Systems",
        "description": "Covers web application development including server-side programming, REST APIs, databases, and security.",
        "difficulty": "medium",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Project + Exam",
        "skills": ["Web Development", "SQL & Databases", "System Design"],
    },
    {
        "code": "DECO3000",
        "name": "Advanced Interaction Design",
        "description": "Advanced topics in interaction design: speculative design, embodied interaction, design ethics, and high-fidelity prototyping.",
        "difficulty": "medium",
        "workload": "10-12 hrs/wk",
        "assessment_type": "Portfolio + Critique",
        "skills": ["Advanced Prototyping", "Interaction Design", "UX Research", "User Needs Analysis"],
    },
    {
        "code": "MATH1061",
        "name": "Discrete Mathematics",
        "description": "Covers logic, proof techniques, sets, functions, combinatorics, graph theory, and their applications in computing.",
        "difficulty": "medium",
        "workload": "8-10 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Discrete Mathematics", "Algorithm Design", "Formal Verification"],
    },
    {
        "code": "CSSE3100",
        "name": "Reasoning About Programs",
        "description": "Formal methods for software correctness: Hoare logic, model checking, specification languages, and verified programming.",
        "difficulty": "hard",
        "workload": "10-12 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Formal Verification", "Discrete Mathematics", "System Design"],
    },
    {
        "code": "COMP4403",
        "name": "Compilers and Interpreters",
        "description": "Design and implementation of compilers: lexical analysis, parsing, semantic analysis, code generation, and optimisation.",
        "difficulty": "hard",
        "workload": "12-15 hrs/wk",
        "assessment_type": "Assignments + Exam",
        "skills": ["Compiler Design", "Algorithm Design", "Formal Verification"],
    },
]


CAREERS = [
    {
        "name": "Software Engineer",
        "description": "Designs, builds, and maintains software systems. Works across the full stack or specialises in backend, frontend, or systems programming.",
        "skills": ["Python Programming", "Object-Oriented Design", "Algorithm Design", "Data Structures", "System Design", "Version Control", "Web Development"],
    },
    {
        "name": "Data Scientist",
        "description": "Extracts insights from large datasets using statistical modelling, machine learning, and data visualisation to inform business decisions.",
        "skills": ["Machine Learning", "Statistical Modelling", "Data Analysis", "Data Visualisation", "Python Programming", "SQL & Databases"],
    },
    {
        "name": "UX Designer",
        "description": "Researches user needs and designs intuitive, accessible interfaces through prototyping, testing, and iterative design.",
        "skills": ["UX Research", "Interaction Design", "User Needs Analysis", "Advanced Prototyping", "Technical Communication"],
    },
    {
        "name": "AI / ML Engineer",
        "description": "Builds and deploys machine learning models and AI systems at scale, bridging research and production engineering.",
        "skills": ["Machine Learning", "AI Problem Solving", "Python Programming", "Algorithm Design", "Statistical Modelling", "Data Analysis"],
    },
    {
        "name": "Product Manager",
        "description": "Owns the product roadmap, aligns stakeholders, and translates user needs into features that deliver business value.",
        "skills": ["User Needs Analysis", "UX Research", "Technical Communication", "Project Management", "Data Analysis"],
    },
    {
        "name": "Embedded Systems Engineer",
        "description": "Develops firmware and low-level software for hardware devices, IoT systems, and real-time applications.",
        "skills": ["Embedded Systems", "Computer Architecture", "Algorithm Design", "Formal Verification", "System Design"],
    },
]


class Command(BaseCommand):
    help = "Seed the database with UQ SkillPath course, skill, and career data"

    def handle(self, *args, **options):
        self.stdout.write("Seeding skills...")
        skill_map = {}
        for name, description, category in SKILLS:
            skill, _ = Skill.objects.get_or_create(
                name=name,
                defaults={"description": description, "category": category},
            )
            skill_map[name] = skill
        self.stdout.write(f"  {len(skill_map)} skills ready")

        self.stdout.write("Seeding courses...")
        for data in COURSES:
            course, _ = Course.objects.get_or_create(
                code=data["code"],
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                    "difficulty": data["difficulty"],
                    "workload": data["workload"],
                    "assessment_type": data["assessment_type"],
                },
            )
            for skill_name in data["skills"]:
                if skill_name in skill_map:
                    course.skills.add(skill_map[skill_name])
        self.stdout.write(f"  {len(COURSES)} courses ready")

        self.stdout.write("Seeding careers...")
        for data in CAREERS:
            career, _ = Career.objects.get_or_create(
                name=data["name"],
                defaults={"description": data["description"]},
            )
            for skill_name in data["skills"]:
                if skill_name in skill_map:
                    career.skills.add(skill_map[skill_name])
        self.stdout.write(f"  {len(CAREERS)} careers ready")

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
