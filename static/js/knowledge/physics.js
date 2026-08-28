/**
 * Physics Formula & Knowledge Base Library
 */
const PhysicsKnowledge = {
    formulas: [
        {
            name: "Newton's Second Law",
            category: "Mechanics",
            expression: "F = m * a",
            description: "Force equals mass times acceleration.",
            variables: ["F: Force (Newtons)", "m: Mass (kg)", "a: Acceleration (m/s²)"]
        },
        {
            name: "Kinematic Equation",
            category: "Kinematics",
            expression: "v² = u² + 2 a s",
            description: "Relates initial/final velocities, acceleration, and displacement.",
            variables: ["u: Initial velocity", "v: Final velocity", "a: Acceleration", "s: Displacement"]
        },
        {
            name: "Ideal Gas Law",
            category: "Thermodynamics",
            expression: "P * V = n * R * T",
            description: "Equation of state of a hypothetical ideal gas.",
            variables: ["P: Pressure", "V: Volume", "n: Moles", "R: Universal gas constant", "T: Absolute temperature"]
        },
        {
            name: "Coulomb's Law",
            category: "Electrostatics",
            expression: "F = k * (|q1 * q2|) / r²",
            description: "Electrostatic force of attraction or repulsion between two point charges.",
            variables: ["k: Coulomb's constant 8.99e9 N·m²/C²", "q1, q2: Electric charges", "r: Separation distance"]
        },
        {
            name: "Snell's Law of Refraction",
            category: "Optics",
            expression: "n1 * sin(θ1) = n2 * sin(θ2)",
            description: "Describes relationship between angles of incidence and refraction for light crossing media interface.",
            variables: ["n1, n2: Refractive indices", "θ1, θ2: Angles relative to normal"]
        }
    ]
};

window.PhysicsKnowledge = PhysicsKnowledge;
