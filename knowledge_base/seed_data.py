"""
Comprehensive Seed Data Generator & Database Seeding Engine
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

from doubts.models import Subject, TopicCategory, Doubt, SolutionStep
from forum.models import ForumQuestion, ForumAnswer
from flashcards.models import FlashcardDeck, Flashcard, StudentNote

def seed_database():
    """
    Populates default subjects, curated solved student doubts, flashcard decks,
    community forum questions, and study notes.
    """
    subjects_data = [
        {
            'name': 'Mathematics',
            'code': 'MATH',
            'description': 'Calculus, Algebra, Geometry, Trigonometry, Linear Algebra & Probability.',
            'color_hex': '#2563EB',
            'icon_name': 'calculator'
        },
        {
            'name': 'Physics',
            'code': 'PHYS',
            'description': 'Mechanics, Kinematics, Thermodynamics, Electromagnetism & Optics.',
            'color_hex': '#EC4899',
            'icon_name': 'atom'
        },
        {
            'name': 'Chemistry',
            'code': 'CHEM',
            'description': 'Organic Reactions, Stoichiometry, Periodic Table & Electrochemistry.',
            'color_hex': '#8B5CF6',
            'icon_name': 'flask'
        },
        {
            'name': 'Computer Science',
            'code': 'CS',
            'description': 'Algorithms, Data Structures, Code Debugging & System Design.',
            'color_hex': '#10B981',
            'icon_name': 'code'
        },
        {
            'name': 'Biology',
            'code': 'BIO',
            'description': 'Genetics, Cell Biology, Molecular DNA/RNA & Physiology.',
            'color_hex': '#F59E0B',
            'icon_name': 'dna'
        },
        {
            'name': 'General Aptitude',
            'code': 'APT',
            'description': 'Quantitative Reasoning, Time & Work, Financial Math & Logical Deduction.',
            'color_hex': '#06B6D4',
            'icon_name': 'brain'
        }
    ]

    subject_objs = {}
    for s in subjects_data:
        obj, _ = Subject.objects.get_or_create(
            code=s['code'],
            defaults={
                'name': s['name'],
                'description': s['description'],
                'color_hex': s['color_hex'],
                'icon_name': s['icon_name']
            }
        )
        subject_objs[s['code']] = obj

    # Seed Doubts and Solutions
    sample_doubts = [
        # Math Doubts
        {
            'subject': subject_objs['MATH'],
            'title': 'How to evaluate the indefinite integral \\int x \\cdot \\sin(x) \\, dx?',
            'question_text': 'I am stuck on integrating x * sin(x). Should I use integration by parts or trigonometric substitution?',
            'latex_formula': r'\int x \sin(x) \, dx',
            'difficulty': 'MEDIUM',
            'student_name': 'Sarah Jenkins',
            'upvotes': 24,
            'steps': [
                {'title': 'Identify u and dv for Integration by Parts', 'explanation': 'Using LIATE rule, choose Algebraic u = x and Trigonometric dv = sin(x) dx.', 'formula': r'u = x, \quad dv = \sin(x) \, dx \implies du = dx, \quad v = -\cos(x)'},
                {'title': 'Apply Integration by Parts Formula', 'explanation': 'Substitute terms into \\int u dv = uv - \\int v du.', 'formula': r'\int x \sin(x) \, dx = -x \cos(x) - \int (-\cos(x)) \, dx'},
                {'title': 'Integrate Remaining Term', 'explanation': 'The integral of -cos(x) is -sin(x), so subtracting it yields +sin(x).', 'formula': r'= -x \cos(x) + \sin(x) + C'},
                {'title': 'Final Solution Verification', 'explanation': 'Differentiating sin(x) - x*cos(x) gives cos(x) - (cos(x) - x*sin(x)) = x*sin(x). Correct!', 'formula': r'\sin(x) - x \cos(x) + C'}
            ]
        },
        {
            'subject': subject_objs['MATH'],
            'title': 'How to find eigenvalues of a 2x2 matrix?',
            'question_text': 'What is the step-by-step method to calculate eigenvalues for matrix A = [[4, 1], [2, 3]]?',
            'latex_formula': r'\det(A - \lambda I) = 0',
            'difficulty': 'HARD',
            'student_name': 'Marcus Vance',
            'upvotes': 18,
            'steps': [
                {'title': 'Formulate Characteristic Equation', 'explanation': 'Subtract λ from main diagonal entries of matrix A.', 'formula': r'A - \lambda I = \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix}'},
                {'title': 'Compute Determinant', 'explanation': 'Determinant = (4-λ)(3-λ) - (1)(2) = λ^2 - 7λ + 12 - 2 = λ^2 - 7λ + 10.', 'formula': r'\lambda^2 - 7\lambda + 10 = 0'},
                {'title': 'Factor Quadratic Equation', 'explanation': 'Factor (λ - 5)(λ - 2) = 0.', 'formula': r'\lambda_1 = 5, \quad \lambda_2 = 2'},
                {'title': 'Final Eigenvalues', 'explanation': 'The eigenvalues of matrix A are λ = 5 and λ = 2.', 'formula': r'\lambda \in \{2, 5\}'}
            ]
        },

        # Physics Doubts
        {
            'subject': subject_objs['PHYS'],
            'title': 'Calculating stopping distance for a car under friction',
            'question_text': 'A 1200kg car travels at 25 m/s. If the coefficient of kinetic friction μ_k = 0.5, what is the stopping distance when brakes are applied?',
            'latex_formula': r'v^2 = u^2 + 2as, \quad f_k = \mu_k m g',
            'difficulty': 'MEDIUM',
            'student_name': 'Liam Connor',
            'upvotes': 31,
            'steps': [
                {'title': 'Calculate Frictional Force & Acceleration', 'explanation': 'Friction f_k = μ_k * m * g. Acceleration a = -f_k / m = -μ_k * g = -0.5 * 9.8 = -4.9 m/s^2.', 'formula': r'a = -\mu_k g = -4.9 \text{ m/s}^2'},
                {'title': 'Apply Kinematic Equation', 'explanation': 'Final velocity v = 0. Use v^2 = u^2 + 2*a*s => 0 = 25^2 + 2(-4.9)s.', 'formula': r'0 = 625 - 9.8 s'},
                {'title': 'Solve for Stopping Distance s', 'explanation': 's = 625 / 9.8 = 63.78 meters.', 'formula': r's = 63.78 \text{ meters}'}
            ]
        },

        # CS Doubts
        {
            'subject': subject_objs['CS'],
            'title': 'Why is my Binary Search algorithm getting stuck in infinite loop?',
            'question_text': 'My code `mid = (low + high) // 2` with `low = mid` in Python gets stuck when low and high differ by 1.',
            'code_snippet': 'while low < high:\n    mid = (low + high) // 2\n    if arr[mid] < target:\n        low = mid  # Bug here!\n    else:\n        high = mid',
            'difficulty': 'MEDIUM',
            'student_name': 'Elena Rostova',
            'upvotes': 42,
            'steps': [
                {'title': 'Identify Infinite Loop Cause', 'explanation': 'When `high = low + 1`, `(low + high) // 2` evaluates to `low`. Setting `low = mid` sets `low` back to its previous value, creating infinite loop.', 'code_output': 'Infinite loop at low=0, high=1 -> mid=0 -> low=0'},
                {'title': 'Fix Pointer Update', 'explanation': 'Update low pointer to `low = mid + 1` to ensure strict progress in search space.', 'code_output': 'low = mid + 1'},
                {'title': 'Correct Implementation', 'explanation': 'Use standard binary search bounds.', 'code_output': 'while low <= high:\n    mid = low + (high - low) // 2\n    if arr[mid] == target:\n        return mid\n    elif arr[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1'}
            ]
        },

        # Chemistry Doubts
        {
            'subject': subject_objs['CHEM'],
            'title': 'How to calculate pH of 0.05 M H2SO4 solution?',
            'question_text': 'Assuming H2SO4 dissociates completely in both stages, what is the pH of a 0.05 M aqueous solution?',
            'latex_formula': r'\text{pH} = -\log_{10}[H^+]',
            'difficulty': 'EASY',
            'student_name': 'Ananya Patel',
            'upvotes': 15,
            'steps': [
                {'title': 'Identify Dissociation Stoichiometry', 'explanation': 'H2SO4 is a diprotic acid: H2SO4 -> 2 H+ + SO4(2-).', 'formula': r'[H^+] = 2 \times [H_2SO_4] = 2 \times 0.05 = 0.10 \text{ M}'},
                {'title': 'Calculate pH', 'explanation': 'pH = -log10(0.10) = 1.0.', 'formula': r'\text{pH} = -\log_{10}(0.10) = 1.0'}
            ]
        },

        # Biology Doubts
        {
            'subject': subject_objs['BIO'],
            'title': 'Phenotypic ratio of dihybrid cross between two heterozygous individuals',
            'question_text': 'If two pea plants heterozygous for flower color (Pp) and seed shape (Rr) are crossed, what fraction will be purple and wrinkled (P_rr)?',
            'latex_formula': r'PpRr \times PpRr',
            'difficulty': 'MEDIUM',
            'student_name': 'Julian Vance',
            'upvotes': 29,
            'steps': [
                {'title': 'Apply Law of Independent Assortment', 'explanation': 'Break cross into independent monohybrid crosses: Pp x Pp and Rr x Rr.', 'formula': r'P(\text{Purple P\_}) = 3/4, \quad P(\text{Wrinkled rr}) = 1/4'},
                {'title': 'Multiply Independent Probabilities', 'explanation': 'P(Purple AND Wrinkled) = (3/4) * (1/4) = 3/16.', 'formula': r'P(P\_rr) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16} \quad (18.75\%)'}
            ]
        },

        # Aptitude Doubts
        {
            'subject': subject_objs['APT'],
            'title': 'A and B can complete a work in 12 and 16 days. How long if they work together?',
            'question_text': 'Person A completes a job in 12 days. Person B completes the same job in 16 days. If both work together, how many days will it take?',
            'latex_formula': r'T = \frac{X \cdot Y}{X + Y}',
            'difficulty': 'EASY',
            'student_name': 'Rohit Sharma',
            'upvotes': 20,
            'steps': [
                {'title': 'Calculate Individual Work Rates', 'explanation': 'A\'s 1-day rate = 1/12. B\'s 1-day rate = 1/16.', 'formula': r'\text{Combined Rate} = \frac{1}{12} + \frac{1}{16} = \frac{4 + 3}{48} = \frac{7}{48}'},
                {'title': 'Compute Combined Days', 'explanation': 'Total days = 48 / 7 = 6.85 days (or 6 days and 20 hours).', 'formula': r'T = \frac{48}{7} \approx 6.85 \text{ days}'}
            ]
        }
    ]

    for d in sample_doubts:
        doubt_obj, created = Doubt.objects.get_or_create(
            title=d['title'],
            defaults={
                'question_text': d['question_text'],
                'subject': d['subject'],
                'latex_formula': d.get('latex_formula', ''),
                'code_snippet': d.get('code_snippet', ''),
                'difficulty': d['difficulty'],
                'student_name': d['student_name'],
                'upvotes': d['upvotes'],
                'status': 'SOLVED'
            }
        )
        if created:
            for idx, s in enumerate(d['steps'], start=1):
                SolutionStep.objects.create(
                    doubt=doubt_obj,
                    step_number=idx,
                    step_title=s['title'],
                    explanation=s['explanation'],
                    formula_used=s.get('formula', ''),
                    code_execution_output=s.get('code_output', '')
                )

    # Seed Flashcard Decks
    decks_data = [
        {
            'subject': subject_objs['MATH'],
            'title': 'Essential Integration & Derivative Formulas',
            'cards': [
                {'front': 'Derivative of sin(x)', 'back': 'cos(x)'},
                {'front': 'Integral of 1/x dx', 'back': 'ln|x| + C'},
                {'front': 'Integration by Parts Formula', 'back': '∫ u dv = uv - ∫ v du'},
                {'front': 'Derivative of e^(kx)', 'back': 'k * e^(kx)'}
            ]
        },
        {
            'subject': subject_objs['PHYS'],
            'title': 'Kinematics & Dynamics Quick Recall',
            'cards': [
                {'front': 'Newton\'s Second Law', 'back': 'F = m * a'},
                {'front': 'Kinematic Equation for Displacement', 'back': 's = ut + 0.5 a t^2'},
                {'front': 'Work-Energy Theorem', 'back': 'W_net = ΔK = K_final - K_initial'},
                {'front': 'Ideal Gas Equation', 'back': 'PV = nRT'}
            ]
        },
        {
            'subject': subject_objs['CS'],
            'title': 'Data Structures & Big-O Complexities',
            'cards': [
                {'front': 'Average Time Complexity of Quick Sort', 'back': 'O(N log N)'},
                {'front': 'Worst Case Time Complexity of Hash Table Search', 'back': 'O(N) when high hash collision, O(1) average'},
                {'front': 'Binary Search Time Complexity', 'back': 'O(log N)'},
                {'front': 'In-order traversal of BST yields what?', 'back': 'Elements in strictly sorted ascending order'}
            ]
        }
    ]

    for deck in decks_data:
        deck_obj, created = FlashcardDeck.objects.get_or_create(
            title=deck['title'],
            defaults={'subject': deck['subject'], 'description': f"Flashcard study set for {deck['subject'].name}"}
        )
        if created:
            for card in deck['cards']:
                Flashcard.objects.create(
                    deck=deck_obj,
                    front_prompt=card['front'],
                    back_solution=card['back']
                )

    # Seed Forum Questions
    forum_data = [
        {
            'subject': subject_objs['MATH'],
            'title': 'What is the intuitive geometric meaning of a matrix determinant?',
            'content': 'I know how to calculate det(A) using formulas, but what does the determinant actually represent visually in 2D or 3D transformations?',
            'author': 'Alex Chen',
            'tags': 'linear algebra, matrix, determinant, geometry',
            'answer': 'The determinant of a matrix represents the scaling factor of area (in 2D) or volume (in 3D) after applying the linear transformation! If det(A) = 2, shapes double in area. If det(A) = 0, space is collapsed into a lower dimension line/point.'
        },
        {
            'subject': subject_objs['CS'],
            'title': 'When to use BFS vs DFS in graph traversal?',
            'content': 'Can someone explain when Breadth-First Search (BFS) is preferred over Depth-First Search (DFS) for pathfinding problems?',
            'author': 'Maya Patel',
            'tags': 'graph, bfs, dfs, algorithms',
            'answer': 'Use BFS when looking for the SHORTEST path in unweighted graphs (since it explores level by level). Use DFS when checking if a path exists, searching deep trees, or solving mazes with backtracking where memory space is restricted.'
        }
    ]

    for fq in forum_data:
        q_obj, created = ForumQuestion.objects.get_or_create(
            title=fq['title'],
            defaults={
                'content': fq['content'],
                'subject': fq['subject'],
                'author_name': fq['author'],
                'tags': fq['tags'],
                'upvotes': 14
            }
        )
        if created:
            ForumAnswer.objects.create(
                question=q_obj,
                content=fq['answer'],
                author_name='Verified Academic Assistant',
                is_accepted=True,
                upvotes=19
            )

    print("Database seeding completed successfully with default subjects, doubts, flashcards, and forum posts.")
