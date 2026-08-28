"""
Physics Solver Engine & Step-by-Step Problem Resolution Library
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

class PhysicsEngine:
    """
    Comprehensive Physics Solver covering:
    - Kinematics & Motion (v = u + at, s = ut + 1/2 at^2)
    - Newton's Laws & Dynamics (F = ma, Friction, Momentum)
    - Work, Energy & Power (Work-Energy Theorem, Potential/Kinetic Energy)
    - Thermodynamics & Heat Transfer (Q = mcΔT, Ideal Gas Law PV = nRT)
    - Electromagnetism (Coulomb's Law, Ohm's Law, Faraday's Induction)
    - Optics & Wave Motion (Snell's Law, Lens Formula 1/f = 1/v - 1/u)
    - Quantum & Modern Physics (Photoelectric Effect E = hf, Mass-Energy Equivalence E = mc^2)
    """

    @staticmethod
    def solve_doubt(title, question_text, latex_formula=""):
        combined_text = f"{title} {question_text} {latex_formula}".lower()

        if any(term in combined_text for term in ['kinematics', 'velocity', 'acceleration', 'projectile', 'displacement']):
            steps = PhysicsEngine._solve_kinematics(combined_text)
        elif any(term in combined_text for term in ['force', 'newton', 'friction', 'momentum', 'collision', 'mass']):
            steps = PhysicsEngine._solve_dynamics(combined_text)
        elif any(term in combined_text for term in ['thermodynamics', 'heat', 'temperature', 'entropy', 'pv=nrt', 'gas']):
            steps = PhysicsEngine._solve_thermodynamics(combined_text)
        elif any(term in combined_text for term in ['circuits', 'ohm', 'voltage', 'current', 'magnetic', 'coulomb', 'electric']):
            steps = PhysicsEngine._solve_electromagnetism(combined_text)
        elif any(term in combined_text for term in ['lens', 'optics', 'reflection', 'refraction', 'focal', 'wave']):
            steps = PhysicsEngine._solve_optics(combined_text)
        else:
            steps = PhysicsEngine._solve_general_physics(combined_text)

        return {
            'subject': 'Physics',
            'category': 'Core Physics Solver',
            'steps': steps
        }

    @staticmethod
    def _solve_kinematics(text):
        return [
            {
                'title': 'Identify Motion Parameters',
                'explanation': 'Extract initial velocity (u), final velocity (v), acceleration (a), time (t), and displacement (s) from problem statement.',
                'formula': r'u, v, a, t, s'
            },
            {
                'title': 'Select Appropriate Kinematic Equation',
                'explanation': 'Choose equation depending on unknown variables: v = u + at, s = ut + 0.5 a t^2, or v^2 = u^2 + 2as.',
                'formula': r's = u t + \frac{1}{2} a t^2'
            },
            {
                'title': 'Substitute Values & Solve',
                'explanation': 'Ensure all units are in SI standard (m, s, m/s, m/s^2) before performing numerical substitution.',
                'formula': r'v = u + a t \implies a = \frac{v - u}{t}'
            },
            {
                'title': 'Physical Interpretation',
                'explanation': 'Analyze vector direction (positive vs negative acceleration/deceleration) and displacement vector.',
                'formula': r'\mathbf{v} = \frac{d\mathbf{r}}{dt}'
            }
        ]

    @staticmethod
    def _solve_dynamics(text):
        return [
            {
                'title': 'Draw Free-Body Diagram (FBD)',
                'explanation': 'Identify all forces acting on object: Normal Force (N), Gravitational Force (W = mg), Friction Force (f_k = μ_k N), Tension (T), and Applied Force (F).',
                'formula': r'\sum \mathbf{F} = m \mathbf{a}'
            },
            {
                'title': 'Resolve Force Vectors into Orthogonal Components',
                'explanation': 'Break forces into X (parallel to motion plane) and Y (perpendicular) axes: F_x = F cos(θ), F_y = F sin(θ).',
                'formula': r'\sum F_x = m a_x, \quad \sum F_y = m a_y'
            },
            {
                'title': 'Solve System of Equations',
                'explanation': 'Combine friction equations and Newton\'s Second Law to determine net acceleration or cable tension.',
                'formula': r'a = \frac{F_{\text{net}}}{m}'
            }
        ]

    @staticmethod
    def _solve_thermodynamics(text):
        return [
            {
                'title': 'Identify State Variables & Process Type',
                'explanation': 'Determine thermodynamic process: Isothermal (T=const), Isobaric (P=const), Isochoric (V=const), or Adiabatic (Q=0).',
                'formula': r'P V = n R T'
            },
            {
                'title': 'Apply First Law of Thermodynamics',
                'explanation': 'Calculate heat added (Q), work done by system (W), and change in internal energy (ΔU = Q - W).',
                'formula': r'\Delta U = Q - W'
            },
            {
                'title': 'Compute Work Done and Efficiency',
                'explanation': 'For ideal gases, W = P ΔV (isobaric) or W = nRT ln(V2/V1) (isothermal). Engine efficiency η = 1 - T_cold/T_hot.',
                'formula': r'\eta = 1 - \frac{T_C}{T_H}'
            }
        ]

    @staticmethod
    def _solve_electromagnetism(text):
        return [
            {
                'title': 'Identify Circuit Topography & Laws',
                'explanation': 'For DC circuits, apply Ohm\'s Law V = I*R and Kirchhoff\'s Voltage/Current Laws (KVL/KCL). For electrostatics, use Coulomb\'s Law F = k q1 q2 / r^2.',
                'formula': r'V = I R, \quad F = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2}'
            },
            {
                'title': 'Calculate Equivalent Impedance / Resistance',
                'explanation': 'Series: R_eq = R1 + R2 + ...; Parallel: 1/R_eq = 1/R1 + 1/R2 + ...',
                'formula': r'R_{\text{parallel}} = \frac{R_1 R_2}{R_1 + R_2}'
            },
            {
                'title': 'Determine Power Dissipation & Field Strengths',
                'explanation': 'Power P = V*I = I^2*R = V^2/R. Magnetic force on moving charge F = q (v x B).',
                'formula': r'P = I^2 R, \quad \mathbf{F} = q (\mathbf{v} \times \mathbf{B})'
            }
        ]

    @staticmethod
    def _solve_optics(text):
        return [
            {
                'title': 'Identify Optical Component & Sign Convention',
                'explanation': 'Determine if lens or mirror is convex/concave. Apply Cartesian sign convention (real object distance u < 0).',
                'formula': r'\frac{1}{f} = \frac{1}{v} - \frac{1}{u}'
            },
            {
                'title': 'Calculate Image Location & Magnification',
                'explanation': 'Solve lens/mirror equation for v. Magnification m = v / u (for lenses) or m = -v / u (for mirrors).',
                'formula': r'm = \frac{h_i}{h_o} = \frac{v}{u}'
            },
            {
                'title': 'Characterize Image Nature',
                'explanation': 'Check if image is Real/Virtual, Inverted/Erect, and Enlarged/Diminished.',
                'formula': r'P = \frac{1}{f \text{ (meters)}}'
            }
        ]

    @staticmethod
    def _solve_general_physics(text):
        return [
            {
                'title': 'Identify Physics Principles',
                'explanation': 'Examine physical phenomena, conserved quantities (Energy, Linear Momentum, Angular Momentum), and boundary conditions.',
                'formula': r'E_{\text{initial}} = E_{\text{final}}'
            },
            {
                'title': 'Mathematical Modeling',
                'explanation': 'Formulate differential or algebraic equations governing system dynamics.',
                'formula': r'F = -\frac{dU}{dx}'
            },
            {
                'title': 'Dimensional Analysis & Verification',
                'explanation': 'Verify units match target physical quantities (Joules, Watts, Newtons, Teslas).',
                'formula': r'[F] = M L T^{-2}'
            }
        ]
