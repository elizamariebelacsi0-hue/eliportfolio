"""Skills shown on the Skills page.

Each group is drawn twice: as a ring in the animated orbit and as a card
in the grid below it. Icons live in static/images/skills/.
"""

SKILL_GROUPS = [
    {
        'key': 'frontend',
        'title': 'Frontend',
        'orbit': 'Inner orbit',
        'blurb': 'Building the parts of a website people see and touch.',
        'skills': [
            {'name': 'HTML', 'icon': 'html', 'role': 'Structure', 'brand': '#e34f26'},
            {'name': 'CSS', 'icon': 'css', 'role': 'Styling', 'brand': '#1572b6'},
            {'name': 'JavaScript', 'icon': 'javascript', 'role': 'Interactivity (ES6+)', 'brand': '#e8c700'},
            {'name': 'React.js', 'icon': 'react', 'role': 'UI components', 'brand': '#3fc5e8'},
        ],
    },
    {
        'key': 'backend',
        'title': 'Backend',
        'orbit': 'Middle orbit',
        'blurb': 'The logic, data, and servers that power it.',
        'skills': [
            {'name': 'Python', 'icon': 'python', 'role': 'Logic & machine learning', 'brand': '#3776ab'},
            {'name': 'Django', 'icon': 'django', 'role': 'Web framework', 'brand': '#44b78b'},
            {'name': 'SQL', 'icon': 'sql', 'role': 'Queries & data', 'brand': '#2f80c4'},
            {'name': 'PostgreSQL', 'icon': 'postgresql', 'role': 'Relational database', 'brand': '#336791'},
            {'name': 'Firebase', 'icon': 'firebase', 'role': 'Auth & hosting', 'brand': '#ffa000'},
        ],
    },
    {
        'key': 'design',
        'title': 'Design & Tools',
        'orbit': 'Outer orbit',
        'blurb': 'Planning, prototyping, and shipping the work.',
        'skills': [
            {'name': 'Figma', 'icon': 'figma', 'role': 'Wireframes & UI', 'brand': '#a259ff'},
            {'name': 'Adobe XD', 'icon': 'xd', 'role': 'Prototyping', 'brand': '#ff61f6'},
            {'name': 'GitHub', 'icon': 'github', 'role': 'Collaboration', 'brand': '#6e7681'},
        ],
    },
]

SKILL_COUNT = sum(len(group['skills']) for group in SKILL_GROUPS)
