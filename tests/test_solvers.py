import unittest
from knowledge_base.math_engine import MathEngine
from knowledge_base.physics_engine import PhysicsEngine
from knowledge_base.chemistry_engine import ChemistryEngine
from knowledge_base.cs_engine import CSEngine

class SolverEngineTests(unittest.TestCase):
    def test_math_solver(self):
        res = MathEngine.solve_doubt("Integrate x*sin(x)", "Find integral")
        self.assertEqual(res['subject'], 'Mathematics')
        self.assertGreater(len(res['steps']), 0)

    def test_physics_solver(self):
        res = PhysicsEngine.solve_doubt("Calculate velocity", "v = u + at")
        self.assertEqual(res['subject'], 'Physics')
        self.assertGreater(len(res['steps']), 0)

    def test_chemistry_solver(self):
        res = ChemistryEngine.solve_doubt("Calculate pH", "0.05 M HCl")
        self.assertEqual(res['subject'], 'Chemistry')

    def test_cs_solver(self):
        res = CSEngine.solve_doubt("Binary Search Complexity", "O(log N)")
        self.assertEqual(res['subject'], 'Computer Science')

if __name__ == '__main__':
    unittest.main()
