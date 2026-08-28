/**
 * General Aptitude Knowledge Base Library
 */
const AptitudeKnowledge = {
    formulas: [
        {
            name: "Combined Work Time",
            category: "Time & Work",
            expression: "Time = (A * B) / (A + B)",
            description: "Total days taken by two workers combined when working together.",
            variables: ["A: Days for worker 1", "B: Days for worker 2"]
        },
        {
            name: "Compound Interest Formula",
            category: "Financial Math",
            expression: "A = P * (1 + R/100)^N",
            description: "Calculates total accumulated amount with compound interest.",
            variables: ["P: Principal amount", "R: Annual interest rate", "N: Number of compounding periods"]
        }
    ]
};

window.AptitudeKnowledge = AptitudeKnowledge;
