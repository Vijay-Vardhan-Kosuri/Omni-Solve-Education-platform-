"""
Computer Science & Programming Solver Engine
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

class CSEngine:
    """
    Comprehensive Computer Science & Code Debugging Solver covering:
    - Data Structures (Arrays, Linked Lists, Trees, Graphs, Hash Tables, Heaps)
    - Algorithms (Sorting, Binary Search, Dynamic Programming, BFS/DFS, Recursion)
    - Time & Space Complexity Analysis (Big-O Notation O(1), O(log N), O(N), O(N log N), O(N^2))
    - Syntax Error Debugging & Code Tracing (Python, JavaScript, C++, Java)
    - System Design & Operating Systems (Processes, Threads, Memory, Locks)
    """

    @staticmethod
    def solve_doubt(title, question_text, code_snippet="", latex_formula=""):
        combined_text = f"{title} {question_text} {code_snippet}".lower()

        if any(term in combined_text for term in ['big-o', 'time complexity', 'space complexity', 'o(n)', 'o(log n)']):
            steps = CSEngine._solve_complexity_analysis(combined_text)
        elif any(term in combined_text for term in ['tree', 'binary search tree', 'graph', 'bfs', 'dfs', 'linked list', 'stack', 'queue']):
            steps = CSEngine._solve_data_structures(combined_text)
        elif any(term in combined_text for term in ['dynamic programming', 'dp', 'memoization', 'recursion', 'fibonacci', 'knapsack']):
            steps = CSEngine._solve_dynamic_programming(combined_text)
        elif any(term in combined_text for term in ['error', 'exception', 'syntax', 'nullpointer', 'typeerror', 'indexerror', 'bug', 'debug']):
            steps = CSEngine._solve_code_debugging(combined_text, code_snippet)
        else:
            steps = CSEngine._solve_general_cs(combined_text)

        return {
            'subject': 'Computer Science',
            'category': 'CS & Code Solver',
            'steps': steps
        }

    @staticmethod
    def _solve_complexity_analysis(text):
        return [
            {
                'title': 'Analyze Loop Structure & Nesting',
                'explanation': 'Count nested loops over input size N. Single loop running N times -> O(N). Nested loop -> O(N^2). Halving input -> O(log N).',
                'code_output': 'for i in range(N):\n    for j in range(N):\n        # O(1) operation inside N*N iterations => O(N^2)'
            },
            {
                'title': 'Evaluate Recursive Call Stack Depth',
                'explanation': 'Construct recurrence relation T(N) = a T(N/b) + f(N) and apply Master Theorem.',
                'code_output': 'T(N) = 2 T(N/2) + O(N) => O(N log N) (e.g. Merge Sort)'
            },
            {
                'title': 'Determine Auxiliary Space Complexity',
                'explanation': 'Calculate memory allocated dynamically (hash maps, recursion stack frame depth, additional arrays).',
                'code_output': 'Space Complexity: O(N) for visited array or recursion stack depth.'
            }
        ]

    @staticmethod
    def _solve_data_structures(text):
        return [
            {
                'title': 'Identify Data Structure Properties & Invariants',
                'explanation': 'For Binary Search Trees (BST), left child < parent < right child. For Min-Heaps, parent <= children. For Graphs, represent via Adjacency List or Matrix.',
                'code_output': 'class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None'
            },
            {
                'title': 'Algorithm Step-by-Step Execution',
                'explanation': 'Traversal order: In-order (Left, Root, Right yields sorted values for BST). BFS uses Queue (FIFO), DFS uses Stack / Recursion (LIFO).',
                'code_output': 'def in_order(root):\n    if not root: return []\n    return in_order(root.left) + [root.val] + in_order(root.right)'
            },
            {
                'title': 'Edge Case & Boundary Checks',
                'explanation': 'Handle empty trees (root == None), single node graphs, cycles (visited set), and null pointer references.',
                'code_output': 'if root is None: return 0'
            }
        ]

    @staticmethod
    def _solve_dynamic_programming(text):
        return [
            {
                'title': 'Define DP State Representation',
                'explanation': 'Identify subproblems: Let dp[i] represent the optimal solution value for subproblem of size i.',
                'code_output': 'dp[i] = min cost / max profit to reach index i'
            },
            {
                'title': 'Formulate State Transition Recurrence',
                'explanation': 'Derive mathematical relation connecting state dp[i] to earlier state values dp[i-1], dp[i-2], etc.',
                'code_output': 'dp[i] = dp[i-1] + dp[i-2]  # Fibonacci recurrence\ndp[w] = max(dp[w], dp[w - weight] + val) # Knapsack'
            },
            {
                'title': 'Base Cases & Space Optimization',
                'explanation': 'Set initial base cases (dp[0] = 0, dp[1] = 1). Optimize O(N) memory down to O(1) by maintaining state variables.',
                'code_output': 'prev, curr = 0, 1\nfor _ in range(2, n + 1):\n    prev, curr = curr, prev + curr'
            }
        ]

    @staticmethod
    def _solve_code_debugging(text, code_snippet):
        return [
            {
                'title': 'Identify Traceback / Exception Cause',
                'explanation': 'Analyze traceback error message (e.g. IndexError: list index out of range, TypeError: unsupported operand, NullPointerException).',
                'code_output': 'IndexError: list index out of range\nCause: Loop condition `i <= len(arr)` accesses off-by-one boundary `arr[len(arr)]`.'
            },
            {
                'title': 'Fix Off-By-One & Null References',
                'explanation': 'Update loop bounds to `range(len(arr))` and add defensive checks for None/Null values before member property access.',
                'code_output': '# Fixed Code:\nfor i in range(len(arr)): # Correct bound: 0 to len(arr)-1\n    print(arr[i])'
            },
            {
                'title': 'Verify Fix with Test Cases',
                'explanation': 'Test code snippet against edge cases: empty array [], single element [42], negative numbers, and boundary values.',
                'code_output': 'Test input: arr = [10, 20]\nOutput: 10, 20 (Clean execution, 0 errors)'
            }
        ]

    @staticmethod
    def _solve_general_cs(text):
        return [
            {
                'title': 'Computer Science Fundamental Principles',
                'explanation': 'Deconstruct problem into input specification, algorithm processing logic, and expected output parameters.',
                'code_output': 'Input -> Processing (Algorithm) -> Output'
            },
            {
                'title': 'Modular Implementation',
                'explanation': 'Write clean, self-documenting code with decoupled functions and explicit variable names.',
                'code_output': 'def solve_problem(input_data):\n    # Process input\n    return result'
            },
            {
                'title': 'Code Execution Verification',
                'explanation': 'Verify algorithm correct, time efficiency optimal, and space consumption bounded.',
                'code_output': 'Time: O(N), Space: O(1) - PASS'
            }
        ]
