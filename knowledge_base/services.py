"""
Central Doubt Routing & Solution Dispatcher Service
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

from .math_engine import MathEngine
from .physics_engine import PhysicsEngine
from .chemistry_engine import ChemistryEngine
from .cs_engine import CSEngine
from .biology_engine import BiologyEngine
from .aptitude_engine import AptitudeEngine

def solve_student_doubt(subject_code, title, question_text, latex_formula="", code_snippet=""):
    """
    Routes student doubts to the appropriate specialized heuristic solver engine based on subject code and query intent.
    """
    subject_code = (subject_code or 'MATH').upper().strip()

    if subject_code == 'MATH':
        return MathEngine.solve_doubt(title, question_text, latex_formula)
    elif subject_code == 'PHYS':
        return PhysicsEngine.solve_doubt(title, question_text, latex_formula)
    elif subject_code == 'CHEM':
        return ChemistryEngine.solve_doubt(title, question_text, latex_formula)
    elif subject_code == 'CS':
        return CSEngine.solve_doubt(title, question_text, code_snippet, latex_formula)
    elif subject_code == 'BIO':
        return BiologyEngine.solve_doubt(title, question_text, latex_formula)
    elif subject_code in ['APT', 'APTITUDE']:
        return AptitudeEngine.solve_doubt(title, question_text, latex_formula)
    else:
        # Fallback to Math solver
        return MathEngine.solve_doubt(title, question_text, latex_formula)
