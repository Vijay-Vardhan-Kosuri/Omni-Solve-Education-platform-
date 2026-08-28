/**
 * Computer Science & Algorithms Knowledge Base Library
 */
const CSKnowledge = {
    formulas: [
        {
            name: "Master Theorem",
            category: "Algorithms",
            expression: "T(n) = a T(n/b) + f(n)",
            description: "Provides asymptotic bounds for divide-and-conquer recurrence relations.",
            variables: ["a: Number of subproblems", "b: Subproblem factor", "f(n): Divide/combine cost"]
        },
        {
            name: "Binary Search Complexity",
            category: "Data Structures",
            expression: "O(log N)",
            description: "Time complexity for searching in a sorted array by halving space at each step.",
            variables: ["N: Total array elements"]
        },
        {
            name: "Hash Table Average Search",
            category: "Data Structures",
            expression: "O(1)",
            description: "Constant time lookup using hash function mapping keys to indices.",
            variables: ["O(1): Constant time under low load factor"]
        }
    ]
};

window.CSKnowledge = CSKnowledge;
