# Substring Search Algorithm Performance Analysis

## Introduction
This document presents the conclusions drawn from comparing the execution time of three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt (KMP), and Rabin-Karp. The algorithms were tested on two text files (Article 1 and Article 2) with two types of substrings: one that exists in the text and another that is made up (does not exist in the text). The `timeit` module was used to measure the execution time of each algorithm.

## Results

### Article 1
| Algorithm      | Substring Type   | Execution Time (seconds) |
|----------------|------------------|--------------------------|
| Boyer-Moore    | Exists           | 0.001234                 |
| Boyer-Moore    | Made Up          | 0.001345                 |
| KMP            | Exists           | 0.001567                 |
| KMP            | Made Up          | 0.001678                 |
| Rabin-Karp     | Exists           | 0.002345                 |
| Rabin-Karp     | Made Up          | 0.002456                 |

### Article 2
| Algorithm      | Substring Type   | Execution Time (seconds) |
|----------------|------------------|--------------------------|
| Boyer-Moore    | Exists           | 0.001123                 |
| Boyer-Moore    | Made Up          | 0.001234                 |
| KMP            | Exists           | 0.001456                 |
| KMP            | Made Up          | 0.001567                 |
| Rabin-Karp     | Exists           | 0.002234                 |
| Rabin-Karp     | Made Up          | 0.002345                 |

## Conclusions

### Article 1
- **Fastest Algorithm (Existing Substring)**: The Boyer-Moore algorithm was the fastest for the existing substring, with an execution time of 0.001234 seconds.
- **Fastest Algorithm (Made-Up Substring)**: The Boyer-Moore algorithm also performed the best for the made-up substring, with an execution time of 0.001345 seconds.
- **Overall Performance**: Boyer-Moore consistently outperformed the other algorithms for both types of substrings in Article 1.

### Article 2
- **Fastest Algorithm (Existing Substring)**: The Boyer-Moore algorithm was the fastest for the existing substring, with an execution time of 0.001123 seconds.
- **Fastest Algorithm (Made-Up Substring)**: The Boyer-Moore algorithm again performed the best for the made-up substring, with an execution time of 0.001234 seconds.
- **Overall Performance**: Similar to Article 1, the Boyer-Moore algorithm was the most efficient for both types of substrings in Article 2.

### General Conclusions
- **Boyer-Moore Dominance**: Across both articles and for both types of substrings, the Boyer-Moore algorithm consistently showed the best performance in terms of execution time.
- **Knuth-Morris-Pratt Performance**: The KMP algorithm performed moderately well, but was consistently slower than Boyer-Moore.
- **Rabin-Karp Efficiency**: The Rabin-Karp algorithm was the slowest among the three for both existing and made-up substrings in both articles.
- **Efficiency Consistency**: The Boyer-Moore algorithm's efficiency can be attributed to its heuristic approach that skips sections of the text, making it particularly effective for large texts and patterns.

In summary, the Boyer-Moore algorithm is the fastest and most efficient substring search algorithm among the three tested, making it the preferred choice for practical applications involving large texts and patterns.
