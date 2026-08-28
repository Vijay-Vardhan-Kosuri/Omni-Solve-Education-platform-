/**
 * Biology Knowledge Base Library
 */
const BiologyKnowledge = {
    formulas: [
        {
            name: "Hardy-Weinberg Principle",
            category: "Genetics",
            expression: "p² + 2pq + q² = 1",
            description: "States that allele and genotype frequencies in a population will remain constant from generation to generation in absence of evolutionary influences.",
            variables: ["p: Dominant allele frequency", "q: Recessive allele frequency", "2pq: Heterozygotes"]
        },
        {
            name: "Cellular Respiration ATP Yield",
            category: "Metabolism",
            expression: "C6H12O6 + 6O2 → 6CO2 + 6H2O + 32 ATP",
            description: "Oxidation of glucose into chemical energy stored as ATP.",
            variables: ["ATP: Adenosine Triphosphate"]
        }
    ]
};

window.BiologyKnowledge = BiologyKnowledge;
