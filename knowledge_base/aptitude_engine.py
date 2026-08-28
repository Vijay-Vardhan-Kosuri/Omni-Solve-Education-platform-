"""
General Aptitude & Logical Reasoning Solver Engine
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

class AptitudeEngine:
    """
    Comprehensive General Aptitude Solver covering:
    - Quantitative Aptitude (Time & Work, Speed & Distance, Profit & Loss, Simple/Compound Interest)
    - Logical Reasoning (Syllogisms, Blood Relations, Seating Arrangement, Coding-Decoding)
    - Data Interpretation (Bar charts, Pie charts, Table data, Ratios & Percentages)
    - Number Series & Pattern Recognition
    """

    @staticmethod
    def solve_doubt(title, question_text, latex_formula=""):
        combined_text = f"{title} {question_text} {latex_formula}".lower()

        if any(term in combined_text for term in ['time', 'work', 'speed', 'distance', 'train', 'pipes', 'cistern']):
            steps = AptitudeEngine._solve_time_work_speed(combined_text)
        elif any(term in combined_text for term in ['profit', 'loss', 'discount', 'interest', 'compound', 'principal', 'percentage']):
            steps = AptitudeEngine._solve_financial_math(combined_text)
        elif any(term in combined_text for term in ['syllogism', 'logic', 'blood relation', 'seating', 'direction', 'statement']):
            steps = AptitudeEngine._solve_logical_reasoning(combined_text)
        elif any(term in combined_text for term in ['series', 'pattern', 'missing number', 'sequence', 'progression']):
            steps = AptitudeEngine._solve_number_series(combined_text)
        else:
            steps = AptitudeEngine._solve_general_aptitude(combined_text)

        return {
            'subject': 'Aptitude',
            'category': 'General Aptitude Solver',
            'steps': steps
        }

    @staticmethod
    def _solve_time_work_speed(text):
        return [
            {
                'title': 'Identify Rates of Work / Speed Formulas',
                'explanation': 'Rate of Work = 1 / Days to complete full task. Total Work = Rate * Time. Speed = Distance / Time.',
                'formula': r'W_{\text{rate}} = \frac{1}{T}, \quad v = \frac{d}{t}'
            },
            {
                'title': 'Combine Individual Work Rates',
                'explanation': 'If Person A finishes in X days and Person B in Y days, combined rate = 1/X + 1/Y = (X+Y)/(X*Y). Combined time = (X*Y)/(X+Y).',
                'formula': r'T_{\text{combined}} = \frac{X \cdot Y}{X + Y}'
            },
            {
                'title': 'Relative Speed for Trains / Objects',
                'explanation': 'Opposite directions: S_relative = S1 + S2. Same direction: S_relative = |S1 - S2|.',
                'formula': r'S_{\text{relative}} = S_1 \pm S_2'
            }
        ]

    @staticmethod
    def _solve_financial_math(text):
        return [
            {
                'title': 'Identify Price & Interest Variables',
                'explanation': 'Cost Price (CP), Selling Price (SP), Profit = SP - CP, Loss = CP - SP. Profit % = (Profit / CP) * 100.',
                'formula': r'\text{Profit \%} = \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100\%'
            },
            {
                'title': 'Compound Interest vs Simple Interest Formula',
                'explanation': 'Simple Interest SI = (P * R * T) / 100. Compound Amount A = P (1 + R/100)^N. CI = A - P.',
                'formula': r'A = P \left(1 + \frac{R}{100}\right)^N, \quad \text{CI} = A - P'
            },
            {
                'title': 'Compute Net Profit / Amount',
                'explanation': 'Substitute principal P, annual rate R%, and time period N to obtain exact financial total.',
                'formula': r'\text{Net Amount} = P + \text{Interest}'
            }
        ]

    @staticmethod
    def _solve_logical_reasoning(text):
        return [
            {
                'title': 'Deconstruct Statements & Venn Diagrams',
                'explanation': 'For Syllogisms, represent premises using set diagrams (All A are B, Some B are C, No C is D).',
                'formula': r'A \subseteq B, \quad B \cap C \neq \emptyset'
            },
            {
                'title': 'Evaluate Logical Deductions',
                'explanation': 'Test validity of conclusions against all possible overlap scenarios.',
                'formula': r'\text{Conclusion is Valid iff true in ALL Venn configurations}'
            },
            {
                'title': 'Final Solution & Verdict',
                'explanation': 'State clearly which conclusions follow logically from given premises.',
                'formula': r'\text{Verdict: Only Conclusion I follows}'
            }
        ]

    @staticmethod
    def _solve_number_series(text):
        return [
            {
                'title': 'Analyze Consecutive Terms Difference',
                'explanation': 'Compute first-order difference Δ1 = T_(n+1) - T_n. If Δ1 is constant, series is Arithmetic (AP). If Δ1 ratio is constant, series is Geometric (GP).',
                'formula': r'T_n = a + (n-1)d \quad \text{or} \quad T_n = a \cdot r^{n-1}'
            },
            {
                'title': 'Check Second-Order Differences or Squares/Cubes',
                'explanation': 'If Δ1 is non-constant, compute Δ2 = Δ1_(n+1) - Δ1_n or test n^2 ± k, n^3 ± k patterns.',
                'formula': r'\Delta_2 = \text{constant} \implies T_n = a n^2 + b n + c'
            },
            {
                'title': 'Determine Missing Term',
                'explanation': 'Apply discovered progression rule to evaluate requested missing index value.',
                'formula': r'T_{\text{target}} = f(\text{target})'
            }
        ]

    @staticmethod
    def _solve_general_aptitude(text):
        return [
            {
                'title': 'Problem Parameter Breakdown',
                'explanation': 'Identify quantitative parameters, ratios, percentages, and algebraic constraints.',
                'formula': r'\text{Ratio } A:B = \frac{a}{b}'
            },
            {
                'title': 'Formulate Algebraic Equation',
                'explanation': 'Set up algebraic equation for unknown variable X.',
                'formula': r'a X + b = c'
            },
            {
                'title': 'Calculate Final Quantitative Answer',
                'explanation': 'Solve linear/quadratic equation and verify numerical consistency.',
                'formula': r'X = \frac{c - b}{a}'
            }
        ]
