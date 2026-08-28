/**
 * Chemistry Formula & Knowledge Base Library
 */
const ChemistryKnowledge = {
    formulas: [
        {
            name: "Mole Concept",
            category: "Stoichiometry",
            expression: "n = m / M",
            description: "Number of moles equals mass in grams divided by molar mass in g/mol.",
            variables: ["n: Moles", "m: Mass (g)", "M: Molar Mass (g/mol)"]
        },
        {
            name: "pH Calculation",
            category: "Acids & Bases",
            expression: "pH = -log10[H+]",
            description: "Negative logarithm of hydrogen ion concentration in solution.",
            variables: ["[H+]: Molar hydrogen ion concentration"]
        },
        {
            name: "Henderson-Hasselbalch Equation",
            category: "Buffers",
            expression: "pH = pKa + log10([A-] / [HA])",
            description: "Estimates pH of buffer solution composed of weak acid and conjugate base.",
            variables: ["pKa: -log10(Ka)", "[A-]: Conjugate base", "[HA]: Weak acid"]
        },
        {
            name: "Nernst Equation",
            category: "Electrochemistry",
            expression: "E = E° - (RT / nF) * ln(Q)",
            description: "Calculates cell potential under non-standard conditions.",
            variables: ["E°: Standard potential", "n: Moles of electrons", "F: Faraday's constant", "Q: Reaction quotient"]
        }
    ]
};

window.ChemistryKnowledge = ChemistryKnowledge;
