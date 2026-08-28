"""
Chemistry Solver Engine & Step-by-Step Problem Resolution Library
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

class ChemistryEngine:
    """
    Comprehensive Chemistry Solver covering:
    - Stoichiometry & Mole Concept (Moles = Mass / Molar Mass)
    - Chemical Equilibrium & Le Chatelier's Principle (Kc = [Products]^p / [Reactants]^r)
    - Acid-Base Equilibrium & pH Calculations (pH = -log10[H+], Henderson-Hasselbalch)
    - Electrochemistry & Nernst Equation (E = E0 - (RT/nF) ln Q)
    - Organic Chemistry Reactions (Nucleophilic substitution SN1/SN2, Addition, Elimination E1/E2)
    - Periodic Table Trends & Electronic Configurations
    """

    @staticmethod
    def solve_doubt(title, question_text, latex_formula=""):
        combined_text = f"{title} {question_text} {latex_formula}".lower()

        if any(term in combined_text for term in ['mole', 'mass', 'stoichiometry', 'molarity', 'gram', 'yield']):
            steps = ChemistryEngine._solve_stoichiometry(combined_text)
        elif any(term in combined_text for term in ['ph', 'acid', 'base', 'buffer', 'titration', 'pka', 'neutralization']):
            steps = ChemistryEngine._solve_acid_base(combined_text)
        elif any(term in combined_text for term in ['organic', 'sn1', 'sn2', 'alkene', 'alcohol', 'benzene', 'reaction', 'substitution']):
            steps = ChemistryEngine._solve_organic_chemistry(combined_text)
        elif any(term in combined_text for term in ['equilibrium', 'kc', 'kp', 'chatelier', 'reaction quotient']):
            steps = ChemistryEngine._solve_equilibrium(combined_text)
        elif any(term in combined_text for term in ['electrochemistry', 'nernst', 'cell', 'cathode', 'anode', 'faraday']):
            steps = ChemistryEngine._solve_electrochemistry(combined_text)
        else:
            steps = ChemistryEngine._solve_general_chemistry(combined_text)

        return {
            'subject': 'Chemistry',
            'category': 'Core Chemistry Solver',
            'steps': steps
        }

    @staticmethod
    def _solve_stoichiometry(text):
        return [
            {
                'title': 'Balance Chemical Reaction Equation',
                'explanation': 'Ensure total atom count for each element is equal on reactant and product sides.',
                'formula': r'a A + b B \longrightarrow c C + d D'
            },
            {
                'title': 'Convert Given Quantities to Moles',
                'explanation': 'Calculate mole amounts using Moles n = mass / Molar Mass (M) or Volume / 22.4L (STP gas).',
                'formula': r'n = \frac{m}{M}, \quad C = \frac{n}{V}'
            },
            {
                'title': 'Identify Limiting Reagent',
                'explanation': 'Divide mole count of each reactant by its stoichiometric coefficient. The lowest ratio is the limiting reagent.',
                'formula': r'\text{Ratio} = \frac{n_{\text{reactant}}}{\text{coefficient}}'
            },
            {
                'title': 'Calculate Theoretical Yield',
                'explanation': 'Use mole ratio of limiting reagent to product to compute expected theoretical mass yield.',
                'formula': r'\text{\% Yield} = \frac{\text{Actual Yield}}{\text{Theoretical Yield}} \times 100\%'
            }
        ]

    @staticmethod
    def _solve_acid_base(text):
        return [
            {
                'title': 'Determine Acid/Base Strength & Dissociation',
                'explanation': 'Strong acids (HCl, HNO3, H2SO4) dissociate completely. Weak acids dissociate partially according to Ka.',
                'formula': r'HA + H_2O \rightleftharpoons H_3O^+ + A^-'
            },
            {
                'title': 'Set up Equilibrium Expression / ICE Table',
                'explanation': 'Initial, Change, Equilibrium table: Ka = [H3O+][A-] / [HA].',
                'formula': r'K_a = \frac{[H_3O^+][A^-]}{[HA]}'
            },
            {
                'title': 'Calculate pH / pOH',
                'explanation': 'Compute pH = -log10[H3O+]. For buffers, use Henderson-Hasselbalch equation pH = pKa + log10([A-]/[HA]).',
                'formula': r'\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[A^-]}{[HA]}\right)'
            }
        ]

    @staticmethod
    def _solve_organic_chemistry(text):
        return [
            {
                'title': 'Analyze Functional Groups & Reagents',
                'explanation': 'Identify substrate structure (alkyl halide, alkene, alcohol) and reagent nature (nucleophile, electrophile, base, acid catalyst).',
                'formula': r'\text{Substrate} + \text{Reagent} \longrightarrow \text{Intermediate} \longrightarrow \text{Product}'
            },
            {
                'title': 'Identify Reaction Mechanism Pathway',
                'explanation': 'Determine if mechanism is SN1 (carbocation intermediate, racemization) vs SN2 (backside attack, inversion of configuration, polar aprotic solvent).',
                'formula': r'\text{SN2: } R-X + Nu^- \longrightarrow [Nu \cdots R \cdots X]^\ddagger \longrightarrow R-Nu + X^-'
            },
            {
                'title': 'Predict Major Product & Regioselectivity',
                'explanation': 'Apply Zaitsev\'s Rule for elimination or Markovnikov\'s Rule for electrophilic addition to alkenes.',
                'formula': r'\text{Markovnikov: H adds to carbon with more hydrogens}'
            }
        ]

    @staticmethod
    def _solve_equilibrium(text):
        return [
            {
                'title': 'Write Equilibrium Constant Expression (Kc/Kp)',
                'explanation': 'Formulate ratio of active mass products to reactants raised to stoichiometric powers.',
                'formula': r'K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b}'
            },
            {
                'title': 'Calculate Reaction Quotient Q',
                'explanation': 'Compare Q to Kc: If Q < Kc, reaction shifts right. If Q > Kc, reaction shifts left. If Q = Kc, system is at equilibrium.',
                'formula': r'Q = \frac{[C]_{\text{current}}^c [D]_{\text{current}}^d}{[A]_{\text{current}}^a [B]_{\text{current}}^b}'
            },
            {
                'title': 'Apply Le Chatelier\'s Principle',
                'explanation': 'Predict shift direction upon altering temperature, pressure, volume, or concentration.',
                'formula': r'\Delta G^\circ = -R T \ln K_c'
            }
        ]

    @staticmethod
    def _solve_electrochemistry(text):
        return [
            {
                'title': 'Identify Anode (Oxidation) & Cathode (Reduction)',
                'explanation': 'AN OX (Anode Oxidation) & RED CAT (Reduction Cathode). Calculate standard cell potential E°cell = E°cathode - E°anode.',
                'formula': r'E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}'
            },
            {
                'title': 'Apply Nernst Equation for Non-Standard Conditions',
                'explanation': 'Adjust potential for non-unit molar concentrations at temperature T.',
                'formula': r'E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{0.0592}{n} \log_{10} Q \quad (\text{at } 298 \text{ K})'
            },
            {
                'title': 'Relate Potential to Free Energy & Equilibrium',
                'explanation': 'Calculate Gibbs Free Energy change ΔG° = -n F E°cell.',
                'formula': r'\Delta G^\circ = -n F E^\circ_{\text{cell}}'
            }
        ]

    @staticmethod
    def _solve_general_chemistry(text):
        return [
            {
                'title': 'Identify Chemical Principles',
                'explanation': 'Analyze electronic structure, chemical bonding (ionic, covalent, metallic), or periodic trends.',
                'formula': r'1s^2 2s^2 2p^6 \dots'
            },
            {
                'title': 'Step-by-Step Reaction Tracing',
                'explanation': 'Trace electron transfers, formal charges, and Lewis dot structure octet rules.',
                'formula': r'\text{Formal Charge} = V - N - \frac{B}{2}'
            },
            {
                'title': 'Solution Summary',
                'explanation': 'Synthesize stoichiometry, thermodynamic favorability, and product geometry.',
                'formula': r'VSEPR \longrightarrow \text{Molecular Geometry}'
            }
        ]
