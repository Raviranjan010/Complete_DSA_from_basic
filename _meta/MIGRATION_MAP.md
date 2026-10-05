# DSA Repository Master Migration Map (`MIGRATION_MAP.md`)

Strict adherence to Non-Negotiable Rule R2: **Preserve Before Replacing**. Nothing is deleted until it is recorded in this map with a decision (`KEEP` / `MOVE` / `MERGE` / `REWRITE` / `REMOVE`) and justification.

## 1. Decision Summary
- **Total Files Audited**: 253
- **KEEP**: 1 files
- **MOVE**: 67 files (`git mv` to preserve commit history)
- **MERGE**: 134 files (consolidating redundant notes and problem sets)
- **REWRITE**: 11 files (overhauling stubs and root index files)
- **REMOVE**: 40 files (compiled binaries, temp runner files, 0-byte files, and empty stub READMEs)

---

## 2. Complete File Migration Registry (All 253 Original Files)

| # | Original Path | Decision | New Canonical Path | Justification | Migration Status |
|---|---|---|---|---|---|
| 1 | `00-MASTER-PROMPT.md` | **MERGE** | `_meta/ARCHITECTURE.md` | Legacy planning prompt; absorbed into official architecture and style guide | `PLANNED` |
| 2 | `00-prerequisites/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 3 | `01-REPO-STRUCTURE-AND-NAMING.md` | **MERGE** | `_meta/ARCHITECTURE.md` | Legacy planning prompt; absorbed into official architecture and style guide | `PLANNED` |
| 4 | `01-complexity-analysis/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 5 | `02-COMPLETE-DSA-CURRICULUM.md` | **MERGE** | `_meta/ARCHITECTURE.md` | Legacy planning prompt; absorbed into official architecture and style guide | `PLANNED` |
| 6 | `02-arrays-and-strings/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 7 | `03-CONTENT-STANDARDS-AND-TEMPLATE.md` | **MERGE** | `_meta/ARCHITECTURE.md` | Legacy planning prompt; absorbed into official architecture and style guide | `PLANNED` |
| 8 | `03-recursion-and-backtracking/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 9 | `04-EXECUTION-PLAN-AND-PROMPTS.md` | **MERGE** | `_meta/ARCHITECTURE.md` | Legacy planning prompt; absorbed into official architecture and style guide | `PLANNED` |
| 10 | `04-linked-list/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 11 | `05-stack-and-queue/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 12 | `06-hashing/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 13 | `07-trees/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 14 | `08-heaps-and-priority-queue/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 15 | `09-graphs/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 16 | `10-greedy/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 17 | `11-dynamic-programming/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 18 | `12-advanced-strings/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 19 | `13-bit-manipulation-and-math/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 20 | `14-advanced-topics/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 21 | `15-interview-prep/README.md` | **REMOVE** | `NA` | Empty placeholder README stub from unfinished earlier attempt; superseded by full topic hub READMEs | `PLANNED` |
| 22 | `CHEATSHEETS/complexity-cheatsheet.md` | **REWRITE** | `33-Cheat-Sheets/complexity-cheatsheet.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 23 | `CHEATSHEETS/cpp-stl-cheatsheet.md` | **REWRITE** | `33-Cheat-Sheets/cpp-stl-cheatsheet.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 24 | `CHEATSHEETS/dp-patterns-cheatsheet.md` | **REWRITE** | `33-Cheat-Sheets/dp-patterns-cheatsheet.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 25 | `CHEATSHEETS/graph-algorithms-cheatsheet.md` | **REWRITE** | `33-Cheat-Sheets/graph-algorithms-cheatsheet.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 26 | `CHEATSHEETS/interview-last-minute-revision.md` | **REWRITE** | `33-Cheat-Sheets/interview-last-minute-revision.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 27 | `CHEATSHEETS/recursion-cheatsheet.md` | **REWRITE** | `33-Cheat-Sheets/recursion-cheatsheet.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 28 | `CHEATSHEETS/sorting-cheatsheet.md` | **REWRITE** | `33-Cheat-Sheets/sorting-cheatsheet.md` | Existing stub replaced with complete, dense, high-yield cheat sheet | `PLANNED` |
| 29 | `DSA_ac-main/02_Cpp_Control_Flow_Conditional_Statements_DSA_Notes.md` | **MERGE** | `00-Getting-Started/02-cpp-control-flow-conditional-statements-dsa-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 30 | `DSA_ac-main/Array/01_Arrays_Complete_DSA_Notes.md` | **MERGE** | `03-Arrays/01-arrays-complete-dsa-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 31 | `DSA_ac-main/Array/02_Cpp_Vectors_and_Advanced_Array_DSA_Notes.md` | **MERGE** | `00-Getting-Started/02-cpp-vectors-and-advanced-array-dsa-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 32 | `DSA_ac-main/Array/03_DSA_Pair_Sum_Majority_Element_Brute_Better_Optimal.md` | **MERGE** | `03-Arrays/03-dsa-pair-sum-majority-element-brute-better-optimal.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 33 | `DSA_ac-main/Array/03_DSA_Time_and_Space_Complexity_Notes.md` | **MERGE** | `01-Complexity-Analysis/03-dsa-time-and-space-complexity-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 34 | `DSA_ac-main/Array/04_DSA_Binary_Exponentiation_and_Stock_Problem_Notes.md` | **MERGE** | `03-Arrays/04-dsa-binary-exponentiation-and-stock-problem-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 35 | `DSA_ac-main/Array/05_DSA_Container_With_Most_Water_Notes.md` | **MERGE** | `03-Arrays/05-dsa-container-with-most-water-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 36 | `DSA_ac-main/Array/06_DSA_Product_of_Array_Except_Self_LeetCode_238.md` | **MERGE** | `03-Arrays/06-dsa-product-of-array-except-self-leetcode-238.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 37 | `DSA_ac-main/Array/07_DSA_CPP_Pointers_Complete_Notes.md` | **MERGE** | `00-Getting-Started/07-dsa-cpp-pointers-complete-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 38 | `DSA_ac-main/Array/08_DSA_Binary_Search_Complete_Notes.md` | **MERGE** | `05-Searching/08-dsa-binary-search-complete-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 39 | `DSA_ac-main/C++ Fundamentals for DSA.md` | **MERGE** | `00-Getting-Started/c++ fundamentals for dsa.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 40 | `DSA_ac-main/README.md` | **MERGE** | `00-Getting-Started/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 41 | `DSA_final-main/01_Basics_Of_Cpp/01_introcution.md` | **MERGE** | `00-Getting-Started/01-introcution.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 42 | `DSA_final-main/01_Basics_Of_Cpp/02_Type_Casting.md` | **MERGE** | `00-Getting-Started/02-type-casting.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 43 | `DSA_final-main/01_Basics_Of_Cpp/03_Operators.md` | **MERGE** | `00-Getting-Started/03-operators.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 44 | `DSA_final-main/01_Basics_Of_Cpp/04_Conditional.md` | **MERGE** | `00-Getting-Started/04-conditional.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 45 | `DSA_final-main/01_Basics_Of_Cpp/05_loop.md` | **MERGE** | `00-Getting-Started/05-loop.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 46 | `DSA_final-main/01_Basics_Of_Cpp/05_pattern.md` | **MERGE** | `00-Getting-Started/05-pattern.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 47 | `DSA_final-main/01_Basics_Of_Cpp/06__functions.md` | **MERGE** | `00-Getting-Started/06--functions.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 48 | `DSA_final-main/01_Basics_Of_Cpp/06_functions.cpp` | **MOVE** | `14-Recursion/code/06-functions/06_functions.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 49 | `DSA_final-main/01_Basics_Of_Cpp/07_BinaryNumber_system.md` | **MERGE** | `00-Getting-Started/07-binarynumber-system.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 50 | `DSA_final-main/01_Basics_Of_Cpp/08_pointers.md` | **MERGE** | `00-Getting-Started/08-pointers.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 51 | `DSA_final-main/01_Basics_Of_Cpp/operators.cpp` | **MOVE** | `00-Getting-Started/03-operators-guide.md` | Misnamed markdown file renamed with proper .md extension | `PLANNED` |
| 52 | `DSA_final-main/02_Arrays/01_basics.md` | **MERGE** | `00-Getting-Started/01-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 53 | `DSA_final-main/02_Arrays/02_PassedByValue_and_PassedByReference.md` | **MERGE** | `03-Arrays/02-passedbyvalue-and-passedbyreference.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 54 | `DSA_final-main/02_Arrays/03_Binary Search.md` | **MERGE** | `03-Arrays/03-binary search.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 55 | `DSA_final-main/02_Arrays/04_Pointers_and_Arrays.md` | **MERGE** | `00-Getting-Started/04-pointers-and-arrays.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 56 | `DSA_final-main/02_Arrays/05_Subarrays_and_Kadanes_Algorithm.md` | **MERGE** | `03-Arrays/05-subarrays-and-kadanes-algorithm.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 57 | `DSA_final-main/README.md` | **MERGE** | `00-Getting-Started/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 58 | `DSA_final-main/commit.txt` | **REMOVE** | `NA` | Legacy scratch status file; superseded by _meta/ tracking | `PLANNED` |
| 59 | `DSA_final-main/index.html` | **REMOVE** | `NA` | Static HTML table of contents superseded by root README and topic hubs | `PLANNED` |
| 60 | `DSA_server-main/CLAUDE.md` | **REMOVE** | `NA` | 12-byte stub redirect file; not part of DSA curriculum | `PLANNED` |
| 61 | `DSA_server-main/DSA-MasterCourse/00_Prerequisites/00_mcqs.md` | **MOVE** | `00-Getting-Started/mcqs/00-mcqs.md` | Preserve comprehensive multiple choice assessment bank | `PLANNED` |
| 62 | `DSA_server-main/DSA-MasterCourse/00_Prerequisites/00_notes.md` | **MERGE** | `00-Getting-Started/00-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 63 | `DSA_server-main/DSA-MasterCourse/01_Complexity_Analysis/01_mcqs.md` | **MOVE** | `01-Complexity-Analysis/mcqs/01-mcqs.md` | Preserve comprehensive multiple choice assessment bank | `PLANNED` |
| 64 | `DSA_server-main/DSA-MasterCourse/01_Complexity_Analysis/01_notes.md` | **MERGE** | `01-Complexity-Analysis/01-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 65 | `DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/01_Array_Basics.md` | **MERGE** | `00-Getting-Started/01-array-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 66 | `DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/02_Memory_Model.md` | **MERGE** | `03-Arrays/02-memory-model.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 67 | `DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/03_Operations_Complexity.md` | **MERGE** | `01-Complexity-Analysis/03-operations-complexity.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 68 | `DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/04_Vector_vs_Array.md` | **MERGE** | `03-Arrays/04-vector-vs-array.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 69 | `DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/05_Easy_Problems.md` | **MERGE** | `03-Arrays/05-easy-problems.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 70 | `DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Mistakes.md` | **MERGE** | `00-Getting-Started/mistakes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 71 | `DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Notes.md` | **MERGE** | `00-Getting-Started/notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 72 | `DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Patterns.md` | **MERGE** | `00-Getting-Started/patterns.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 73 | `DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Easy.md` | **MERGE** | `00-Getting-Started/easy.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 74 | `DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Hard.md` | **MERGE** | `00-Getting-Started/hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 75 | `DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Medium.md` | **MERGE** | `00-Getting-Started/medium.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 76 | `DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Mistakes.md` | **MERGE** | `08-Sliding-Window/mistakes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 77 | `DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Notes.md` | **MERGE** | `08-Sliding-Window/notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 78 | `DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Patterns.md` | **MERGE** | `08-Sliding-Window/patterns.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 79 | `DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Easy.md` | **MERGE** | `08-Sliding-Window/easy.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 80 | `DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Hard.md` | **MERGE** | `08-Sliding-Window/hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 81 | `DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Medium.md` | **MERGE** | `08-Sliding-Window/medium.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 82 | `DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Mistakes.md` | **MERGE** | `09-Prefix-Sum-and-Difference-Array/mistakes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 83 | `DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Notes.md` | **MERGE** | `09-Prefix-Sum-and-Difference-Array/notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 84 | `DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Patterns.md` | **MERGE** | `09-Prefix-Sum-and-Difference-Array/patterns.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 85 | `DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Problems/Easy_Medium.md` | **MERGE** | `09-Prefix-Sum-and-Difference-Array/easy-medium.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 86 | `DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Problems/Hard.md` | **MERGE** | `09-Prefix-Sum-and-Difference-Array/hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 87 | `DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Mistakes.md` | **MERGE** | `03-Arrays/mistakes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 88 | `DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Notes.md` | **MERGE** | `03-Arrays/notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 89 | `DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Patterns.md` | **MERGE** | `03-Arrays/patterns.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 90 | `DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Problems/Medium_Hard.md` | **MERGE** | `03-Arrays/medium-hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 91 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Mistakes.md` | **MERGE** | `05-Searching/mistakes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 92 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Notes.md` | **MERGE** | `05-Searching/notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 93 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Patterns.md` | **MERGE** | `05-Searching/patterns.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 94 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/2D_Arrays.md` | **MERGE** | `05-Searching/2d-arrays.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 95 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Easy.md` | **MERGE** | `05-Searching/easy.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 96 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Hard.md` | **MERGE** | `05-Searching/hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 97 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Medium.md` | **MERGE** | `05-Searching/medium.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 98 | `DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Medium_Hard.md` | **MERGE** | `05-Searching/medium-hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 99 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Medium_Problems/Complete_Solutions.md` | **MERGE** | `03-Arrays/complete-solutions.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 100 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Mistakes.md` | **MERGE** | `03-Arrays/mistakes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 101 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Notes.md` | **MERGE** | `03-Arrays/notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 102 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Patterns.md` | **MERGE** | `03-Arrays/patterns.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 103 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Easy.md` | **MERGE** | `03-Arrays/easy.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 104 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Easy_Medium_Hard.md` | **MERGE** | `03-Arrays/easy-medium-hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 105 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Hard.md` | **MERGE** | `03-Arrays/hard.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 106 | `DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Medium.md` | **MERGE** | `03-Arrays/medium.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 107 | `DSA_server-main/DSA-MasterCourse/02_Arrays/07_Hard_Problems/Complete_Solutions.md` | **MERGE** | `03-Arrays/complete-solutions.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 108 | `DSA_server-main/DSA-MasterCourse/02_Arrays/08_Pattern_Recognition/Complete_Guide.md` | **MERGE** | `03-Arrays/complete-guide.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 109 | `DSA_server-main/DSA-MasterCourse/02_Arrays/09_Common_Mistakes/Complete_Guide.md` | **MERGE** | `03-Arrays/complete-guide.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 110 | `DSA_server-main/DSA-MasterCourse/02_Arrays/10_MCQs/Arrays_MCQs.md` | **MOVE** | `03-Arrays/mcqs/arrays-mcqs.md` | Preserve comprehensive multiple choice assessment bank | `PLANNED` |
| 111 | `DSA_server-main/DSA-MasterCourse/02_Arrays/11_Interview_Prep/Arrays_Interview.md` | **MERGE** | `03-Arrays/arrays-interview.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 112 | `DSA_server-main/DSA-MasterCourse/02_Arrays/ARRAY_MASTER_NOTES.md` | **MERGE** | `03-Arrays/array-master-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 113 | `DSA_server-main/DSA-MasterCourse/02_Arrays/PROBLEM_INDEX.md` | **MERGE** | `03-Arrays/problem-index.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 114 | `DSA_server-main/DSA-MasterCourse/02_Arrays/README.md` | **MERGE** | `03-Arrays/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 115 | `DSA_server-main/DSA-MasterCourse/02_Arrays/REORGANIZATION_COMPLETE.md` | **MERGE** | `03-Arrays/reorganization-complete.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 116 | `DSA_server-main/DSA-MasterCourse/03_Strings/03_mcqs.md` | **MOVE** | `04-Strings/mcqs/03-mcqs.md` | Preserve comprehensive multiple choice assessment bank | `PLANNED` |
| 117 | `DSA_server-main/DSA-MasterCourse/03_Strings/03_notes.md` | **MERGE** | `04-Strings/03-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 118 | `DSA_server-main/DSA-MasterCourse/03_Strings/code/basics.cpp` | **MOVE** | `04-Strings/code/basics/basics.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 119 | `DSA_server-main/DSA-MasterCourse/03_Strings/code/pattern_matching.cpp` | **MOVE** | `04-Strings/code/pattern-matching/pattern_matching.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 120 | `DSA_server-main/DSA-MasterCourse/03_Strings/code/string_manipulation.cpp` | **MOVE** | `04-Strings/code/string-manipulation/string_manipulation.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 121 | `DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/04_mcqs.md` | **MOVE** | `14-Recursion/mcqs/04-mcqs.md` | Preserve comprehensive multiple choice assessment bank | `PLANNED` |
| 122 | `DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/04_notes.md` | **MERGE** | `14-Recursion/04-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 123 | `DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/code/backtracking.cpp` | **MOVE** | `14-Recursion/code/backtracking/backtracking.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 124 | `DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/code/basics.cpp` | **MOVE** | `14-Recursion/code/basics/basics.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 125 | `DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/05_mcqs.md` | **MOVE** | `06-Sorting/mcqs/05-mcqs.md` | Preserve comprehensive multiple choice assessment bank | `PLANNED` |
| 126 | `DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/05_notes.md` | **MERGE** | `06-Sorting/05-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 127 | `DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/code/binary_search.cpp` | **MOVE** | `14-Recursion/code/binary-search/binary_search.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 128 | `DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/code/sorting.cpp` | **MOVE** | `14-Recursion/code/sorting/sorting.cpp` | C++ implementation preserved in canonical topic code folder | `PLANNED` |
| 129 | `DSA_server-main/DSA-MasterCourse/06_Linked_List/06_notes.md` | **MERGE** | `11-Linked-List/06-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 130 | `DSA_server-main/DSA-MasterCourse/07_Stack/07_notes.md` | **MERGE** | `12-Stack/07-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 131 | `DSA_server-main/DSA-MasterCourse/08_Queue_and_Deque/08_notes.md` | **MERGE** | `13-Queue-and-Deque/08-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 132 | `DSA_server-main/DSA-MasterCourse/09_Hashing/09_notes.md` | **MERGE** | `10-Hashing/09-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 133 | `DSA_server-main/DSA-MasterCourse/10_Trees/10_notes.md` | **MERGE** | `17-Binary-Trees/10-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 134 | `DSA_server-main/DSA-MasterCourse/11_Binary_Search_Tree/11_notes.md` | **MERGE** | `05-Searching/11-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 135 | `DSA_server-main/DSA-MasterCourse/12_Heaps_and_Priority_Queue/12_notes.md` | **MERGE** | `13-Queue-and-Deque/12-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 136 | `DSA_server-main/DSA-MasterCourse/13_Tries/13_notes.md` | **MERGE** | `24-Trie/13-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 137 | `DSA_server-main/DSA-MasterCourse/14_Graphs/14_notes.md` | **MERGE** | `22-Graphs/14-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 138 | `DSA_server-main/DSA-MasterCourse/15_Dynamic_Programming/15_notes.md` | **MERGE** | `23-Dynamic-Programming/15-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 139 | `DSA_server-main/DSA-MasterCourse/16_Greedy_Algorithms/16_notes.md` | **MERGE** | `20-Greedy/16-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 140 | `DSA_server-main/DSA-MasterCourse/17_Divide_and_Conquer/17_notes.md` | **MERGE** | `00-Getting-Started/17-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 141 | `DSA_server-main/DSA-MasterCourse/18_Bit_Manipulation/18_notes.md` | **MERGE** | `16-Bit-Manipulation/18-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 142 | `DSA_server-main/DSA-MasterCourse/19_Segment_Tree_and_BIT/19_notes.md` | **MERGE** | `16-Bit-Manipulation/19-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 143 | `DSA_server-main/DSA-MasterCourse/20_Advanced_Graphs/20_notes.md` | **MERGE** | `22-Graphs/20-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 144 | `DSA_server-main/DSA-MasterCourse/21_Advanced_DP/21_notes.md` | **MERGE** | `23-Dynamic-Programming/21-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 145 | `DSA_server-main/DSA-MasterCourse/22_Competitive_Programming_Extras/22_notes.md` | **MERGE** | `29-Competitive-Programming/22-notes.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 146 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Adobe.md` | **MERGE** | `31-Company-Wise/adobe.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 147 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Amazon.md` | **MERGE** | `31-Company-Wise/amazon.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 148 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Flipkart.md` | **MERGE** | `31-Company-Wise/flipkart.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 149 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Google.md` | **MERGE** | `31-Company-Wise/google.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 150 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Meta.md` | **MERGE** | `31-Company-Wise/meta.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 151 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Microsoft.md` | **MERGE** | `31-Company-Wise/microsoft.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 152 | `DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/TCS_Infosys_Wipro.md` | **MERGE** | `31-Company-Wise/tcs-infosys-wipro.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 153 | `DSA_server-main/DSA-MasterCourse/README.md` | **MERGE** | `00-Getting-Started/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 154 | `DSA_server-main/DSA-MasterCourse/ROADMAP.md` | **MERGE** | `00-Getting-Started/roadmap.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 155 | `DSA_server-main/DSA-MasterCourse/STUDY_PLAN.md` | **MERGE** | `00-Getting-Started/study-plan.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 156 | `DSA_server-main/DSA-MasterCourse/status.txt` | **REMOVE** | `NA` | Legacy scratch status file; superseded by _meta/ tracking | `PLANNED` |
| 157 | `GLOSSARY.md` | **REWRITE** | `GLOSSARY.md` | Overhauled to eliminate broken phantom links, align with L0-L6 scale and 3-level tree | `PLANNED` |
| 158 | `PATTERNS.md` | **REWRITE** | `PATTERNS.md` | Overhauled to eliminate broken phantom links, align with L0-L6 scale and 3-level tree | `PLANNED` |
| 159 | `PROGRESS-TRACKER.md` | **REWRITE** | `PROGRESS-TRACKER.md` | Overhauled to eliminate broken phantom links, align with L0-L6 scale and 3-level tree | `PLANNED` |
| 160 | `README.md` | **REWRITE** | `README.md` | Overhauled to eliminate broken phantom links, align with L0-L6 scale and 3-level tree | `PLANNED` |
| 161 | `Summer_pep_DSA-main/00-Start-Here-Basics.md` | **MERGE** | `00-Getting-Started/00-start-here-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 162 | `Summer_pep_DSA-main/01-Git-And-GitHub.md` | **MERGE** | `00-Getting-Started/01-git-and-github.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 163 | `Summer_pep_DSA-main/02-Arrays-Basics.md` | **MERGE** | `00-Getting-Started/02-arrays-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 164 | `Summer_pep_DSA-main/03-Two-Pointers.md` | **MERGE** | `00-Getting-Started/03-two-pointers.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 165 | `Summer_pep_DSA-main/04-Binary-Search.md` | **MERGE** | `05-Searching/04-binary-search.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 166 | `Summer_pep_DSA-main/05-Strings.md` | **MERGE** | `04-Strings/05-strings.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 167 | `Summer_pep_DSA-main/06-Recursion.md` | **MERGE** | `14-Recursion/06-recursion.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 168 | `Summer_pep_DSA-main/07-Hashing.md` | **MERGE** | `10-Hashing/07-hashing.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 169 | `Summer_pep_DSA-main/08-Prefix-Sum.md` | **MERGE** | `09-Prefix-Sum-and-Difference-Array/08-prefix-sum.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 170 | `Summer_pep_DSA-main/09-Sliding-Window.md` | **MERGE** | `08-Sliding-Window/09-sliding-window.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 171 | `Summer_pep_DSA-main/10-Linked-List.md` | **MERGE** | `11-Linked-List/10-linked-list.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 172 | `Summer_pep_DSA-main/11-Stack.md` | **MERGE** | `12-Stack/11-stack.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 173 | `Summer_pep_DSA-main/12-Queue.md` | **MERGE** | `13-Queue-and-Deque/12-queue.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 174 | `Summer_pep_DSA-main/Daily problems/Practice-Problems.md` | **MERGE** | `00-Getting-Started/practice-problems.md` | Problem solutions restructured and registered into canonical problem files | `PLANNED` |
| 175 | `Summer_pep_DSA-main/Language-Basics/Cpp-Basics.md` | **MERGE** | `00-Getting-Started/cpp-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 176 | `Summer_pep_DSA-main/Language-Basics/Java-Basics.md` | **MERGE** | `00-Getting-Started/java-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 177 | `Summer_pep_DSA-main/Language-Basics/Python-Basics.md` | **MERGE** | `00-Getting-Started/python-basics.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 178 | `Summer_pep_DSA-main/Language-Basics/README.md` | **MERGE** | `00-Getting-Started/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 179 | `Summer_pep_DSA-main/README.md` | **MERGE** | `00-Getting-Started/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 180 | `dsa-main/.gitignore` | **KEEP** | `.gitignore` | Essential git configuration; preserve and standardize to ignore *.exe, *.o, build/ | `PLANNED` |
| 181 | `dsa-main/10_remove_Occurence(a).cpp` | **MOVE** | `03-Arrays/code/remove-occurence(a)/remove-occurence(a).cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 182 | `dsa-main/10sum_interval.cpp` | **MOVE** | `03-Arrays/code/sum-interval/sum-interval.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 183 | `dsa-main/11_Matrix_muktiplication.cpp` | **MOVE** | `03-Arrays/code/matrix-multiplication/matrix-muktiplication.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 184 | `dsa-main/11_Matrix_muktiplication.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 185 | `dsa-main/11_Palindrome.cpp` | **MOVE** | `04-Strings/code/palindrome/palindrome.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 186 | `dsa-main/12_printing_numbers.cpp` | **MOVE** | `03-Arrays/code/printing-numbers/printing-numbers.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 187 | `dsa-main/13_k_Multiple_of_n.cpp` | **MOVE** | `03-Arrays/code/k-multiple-of-n/k-multiple-of-n.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 188 | `dsa-main/14_sum_of_natural_num_with_alternateign.cpp` | **MOVE** | `03-Arrays/code/sum-of-natural-num-with-alternateign/sum-of-natural-num-with-alternateign.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 189 | `dsa-main/15_GCD_recursion.cpp` | **MOVE** | `14-Recursion/code/gcd-recursion/gcd-recursion.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 190 | `dsa-main/16_Armstrong_Number_check.cpp` | **MOVE** | `03-Arrays/code/armstrong-number-check/armstrong-number-check.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 191 | `dsa-main/17_Frog_jump.cpp` | **MOVE** | `14-Recursion/code/frog-jump/frog-jump.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 192 | `dsa-main/1_basic.cpp` | **MOVE** | `03-Arrays/code/basic/basic.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 193 | `dsa-main/1_factorial.cpp` | **MOVE** | `14-Recursion/code/factorial/factorial.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 194 | `dsa-main/2_valueAtAddreaa.cpp` | **MOVE** | `03-Arrays/code/valueataddreaa/valueataddreaa.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 195 | `dsa-main/3_updatingValueUsingPointer.cpp` | **MOVE** | `00-Getting-Started/code/updatingvalueusingpointer/updatingvalueusingpointer.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 196 | `dsa-main/4_recursive_sum_of_Digitts.cpp` | **MOVE** | `14-Recursion/code/recursive-sum-of-digitts/recursive-sum-of-digitts.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 197 | `dsa-main/4_swaping_value.cpp` | **MOVE** | `00-Getting-Started/code/swaping-value/swaping-value.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 198 | `dsa-main/5_firstAndLastOccurence.cpp` | **MOVE** | `03-Arrays/code/firstandlastoccurence/firstandlastoccurence.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 199 | `dsa-main/5_p_to_the_power_q_UsingRecursion.cpp` | **MOVE** | `03-Arrays/code/p-to-the-power-q-usingrecursion/p-to-the-power-q-usingrecursion.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 200 | `dsa-main/5_sort_zero_One.cpp` | **MOVE** | `06-Sorting/code/sort-zero-one/sort-zero-one.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 201 | `dsa-main/6_IncrementDecrement.cpp` | **MOVE** | `03-Arrays/code/incrementdecrement/incrementdecrement.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 202 | `dsa-main/6_even_int_move2.cpp` | **MOVE** | `03-Arrays/code/even-int-move2/even-int-move2.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 203 | `dsa-main/7_array_recursive.cpp` | **MOVE** | `14-Recursion/code/array-recursive/array-recursive.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 204 | `dsa-main/7_prepostArithematic.cpp` | **MOVE** | `03-Arrays/code/prepostarithematic/prepostarithematic.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 205 | `dsa-main/7_sort_Squared_array.cpp` | **MOVE** | `06-Sorting/code/sort-squared-array/sort-squared-array.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 206 | `dsa-main/7_sort_Squared_array.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 207 | `dsa-main/8_increment_address.cpp` | **REMOVE** | `NA` | 0-byte empty file | `PLANNED` |
| 208 | `dsa-main/8_max_ele_inArray_recursive.cpp` | **MOVE** | `14-Recursion/code/max-ele-inarray-recursive/max-ele-inarray-recursive.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 209 | `dsa-main/8_prefix_sum.cpp` | **MOVE** | `09-Prefix-Sum-and-Difference-Array/code/prefix-sum/prefix-sum.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 210 | `dsa-main/9_check_prefix_sum.cpp` | **MOVE** | `09-Prefix-Sum-and-Difference-Array/code/check-prefix-sum/check-prefix-sum.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 211 | `dsa-main/9_sum_array_ele_usingRecursion.cpp` | **MOVE** | `03-Arrays/code/sum-array-ele-usingrecursion/sum-array-ele-usingrecursion.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 212 | `dsa-main/Count_occurence.cpp` | **MOVE** | `03-Arrays/code/count-occurence/count-occurence.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 213 | `dsa-main/LibraryManagement.cpp` | **MOVE** | `03-Arrays/code/librarymanagement/librarymanagement.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 214 | `dsa-main/README.md` | **MERGE** | `00-Getting-Started/readme.md` | Rich concept notes merged into canonical topic notes | `PLANNED` |
| 215 | `dsa-main/adding_removing.cpp` | **MOVE** | `03-Arrays/code/adding-removing/adding-removing.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 216 | `dsa-main/adding_removing.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 217 | `dsa-main/arr_manipulation.cpp` | **MOVE** | `03-Arrays/code/arr-manipulation/arr-manipulation.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 218 | `dsa-main/arr_manipulation.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 219 | `dsa-main/arr_manipulation1.cpp` | **MOVE** | `03-Arrays/code/arr-manipulation1/arr-manipulation1.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 220 | `dsa-main/basic_array.cpp` | **MOVE** | `03-Arrays/code/basic-array/basic-array.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 221 | `dsa-main/build.bat` | **REMOVE** | `NA` | Ad-hoc student batch build script; superseded by tools/ test harness | `PLANNED` |
| 222 | `dsa-main/check_sorted_or_not.cpp` | **MOVE** | `06-Sorting/code/check-sorted-or-not/check-sorted-or-not.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 223 | `dsa-main/delete_add.cpp` | **MOVE** | `03-Arrays/code/delete-add/delete-add.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 224 | `dsa-main/deploy.bat` | **REMOVE** | `NA` | Ad-hoc student batch build script; superseded by tools/ test harness | `PLANNED` |
| 225 | `dsa-main/even-odd.cpp` | **MOVE** | `03-Arrays/code/even-odd/even-odd.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 226 | `dsa-main/even_int_move.cpp` | **MOVE** | `03-Arrays/code/even-int-move/even-int-move.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 227 | `dsa-main/even_int_move.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 228 | `dsa-main/even_int_move2.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 229 | `dsa-main/frequency_query.cpp` | **MOVE** | `03-Arrays/code/frequency-query/frequency-query.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 230 | `dsa-main/frequency_query.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 231 | `dsa-main/largest.cpp` | **MOVE** | `03-Arrays/code/largest/largest.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 232 | `dsa-main/largest.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 233 | `dsa-main/launch.json` | **MOVE** | `.vscode/launch.json` | VS Code workspace configuration moved to standard .vscode/ directory | `PLANNED` |
| 234 | `dsa-main/linear_search2.cpp` | **MOVE** | `05-Searching/code/linear-search2/linear-search2.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 235 | `dsa-main/linear_search2.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 236 | `dsa-main/linerr_search.cpp` | **MOVE** | `05-Searching/code/linerr-search/linerr-search.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 237 | `dsa-main/linerr_search.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 238 | `dsa-main/matrix_Transpose.cpp` | **MOVE** | `03-Arrays/code/matrix-multiplication/matrix-transpose.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 239 | `dsa-main/matrix_Transpose.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 240 | `dsa-main/occurence.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 241 | `dsa-main/printing_elements.cpp` | **MOVE** | `03-Arrays/code/printing-elements/printing-elements.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 242 | `dsa-main/reverse_arr.cpp` | **MOVE** | `03-Arrays/code/reverse-arr/reverse-arr.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 243 | `dsa-main/second_largest.cpp` | **MOVE** | `03-Arrays/code/second-largest/second-largest.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 244 | `dsa-main/serve.bat` | **REMOVE** | `NA` | Ad-hoc student batch build script; superseded by tools/ test harness | `PLANNED` |
| 245 | `dsa-main/settings.json` | **MOVE** | `.vscode/settings.json` | VS Code workspace configuration moved to standard .vscode/ directory | `PLANNED` |
| 246 | `dsa-main/target_sum.cpp` | **MOVE** | `03-Arrays/code/target-sum/target-sum.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 247 | `dsa-main/target_sum2.cpp` | **MOVE** | `03-Arrays/code/target-sum2/target-sum2.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 248 | `dsa-main/tempCodeRunnerFile.cpp` | **REMOVE** | `NA` | VS Code temporary runner artifact; generated junk | `PLANNED` |
| 249 | `dsa-main/tempCodeRunnerFile.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 250 | `dsa-main/user_input_vector.cpp` | **MOVE** | `03-Arrays/code/user-input-vector/user-input-vector.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 251 | `dsa-main/user_input_vector.exe` | **REMOVE** | `NA` | Compiled binary artifact; must not be tracked in git repository | `PLANNED` |
| 252 | `dsa-main/vector_basic.cpp` | **MOVE** | `03-Arrays/code/vector-basic/vector-basic.cpp` | Verified standalone C++ algorithm moved to canonical topic code directory | `PLANNED` |
| 253 | `dsa-main/verify.bat` | **REMOVE** | `NA` | Ad-hoc student batch build script; superseded by tools/ test harness | `PLANNED` |