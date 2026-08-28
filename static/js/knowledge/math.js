/**
 * Mathematics Formula & Knowledge Base Library
 */
const MathKnowledge = {
    formulas: [
        {
            name: "Quadratic Formula",
            category: "Algebra",
            expression: "x = (-b ± √(b² - 4ac)) / (2a)",
            description: "Solves roots of ax² + bx + c = 0.",
            variables: ["a: coefficient of x²", "b: coefficient of x", "c: constant term"]
        },
        {
            name: "Integration by Parts",
            category: "Calculus",
            expression: "∫ u dv = u v - ∫ v du",
            description: "Used to integrate product of two functions.",
            variables: ["u: differentiable function", "v: antiderivative of dv"]
        },
        {
            name: "Euler's Formula",
            category: "Complex Analysis",
            expression: "e^(i x) = cos(x) + i sin(x)",
            description: "Establishes relationship between trigonometric functions and complex exponentials.",
            variables: ["x: real angle in radians", "i: imaginary unit √(-1)"]
        },
        {
            name: "Pythagorean Theorem",
            category: "Geometry",
            expression: "a² + b² = c²",
            description: "Relates sides of a right-angled triangle.",
            variables: ["a, b: perpendicular legs", "c: hypotenuse"]
        },
        {
            name: "Bayes' Theorem",
            category: "Probability",
            expression: "P(A|B) = [P(B|A) * P(A)] / P(B)",
            description: "Calculates conditional probability of an event based on prior knowledge.",
            variables: ["P(A|B): posterior probability", "P(A): prior probability"]
        }
    ]
};

window.MathKnowledge = MathKnowledge;
