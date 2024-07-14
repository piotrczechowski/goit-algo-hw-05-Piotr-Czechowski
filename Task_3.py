import timeit
import random

# Boyer-Moore algorithm
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1
    
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip.setdefault(pattern[m - 1], m)
    
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            return k + 1
        i += skip.get(text[i], m)
    return -1

# Knuth-Morris-Pratt algorithm
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m, n = len(pattern), len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Rabin-Karp algorithm
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for _ in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Reading the contents of the provided text files
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Load articles
article1 = read_file('article_1.txt')
article2 = read_file('article_2.txt')

# Select substrings
substring_exists = "Dijkstra algorithm"
substring_made_up = "nonexistent substring"

# Function to measure execution time
def measure_time(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__}, text, pattern"
    test_code = f"{func.__name__}(text, pattern)"
    time = timeit.timeit(test_code, setup=setup_code, number=1000)
    return time

# Measure execution time for each algorithm and substring
algorithms = [boyer_moore, kmp_search, rabin_karp]
articles = [(article1, "Article 1"), (article2, "Article 2")]
substrings = [(substring_exists, "exists"), (substring_made_up, "made up")]

results = {}

for article, article_name in articles:
    text = article
    results[article_name] = {}
    for func in algorithms:
        results[article_name][func.__name__] = {}
        for substring, substring_type in substrings:
            pattern = substring
            time_taken = measure_time(func, text, pattern)
            results[article_name][func.__name__][substring_type] = time_taken

# Print results
for article_name in results:
    print(f"\nResults for {article_name}:")
    for func_name in results[article_name]:
        for substring_type in results[article_name][func_name]:
            time_taken = results[article_name][func_name][substring_type]
            print(f"{func_name} ({substring_type}): {time_taken:.6f} seconds")

# Analyze and determine the fastest algorithm
def determine_fastest_algorithm(results):
    summary = {}
    for article_name in results:
        summary[article_name] = {}
        for substring_type in substrings:
            min_time = float('inf')
            fastest_algo = None
            for func_name in results[article_name]:
                time_taken = results[article_name][func_name][substring_type[1]]
                if time_taken < min_time:
                    min_time = time_taken
                    fastest_algo = func_name
            summary[article_name][substring_type[1]] = (fastest_algo, min_time)
    return summary

fastest_algorithms = determine_fastest_algorithm(results)

# Print summary of fastest algorithms
print("\nSummary of Fastest Algorithms:")
for article_name in fastest_algorithms:
    print(f"\n{article_name}:")
    for substring_type in fastest_algorithms[article_name]:
        fastest_algo, time_taken = fastest_algorithms[article_name][substring_type]
        print(f"Fastest for {substring_type} substring: {fastest_algo} with {time_taken:.6f} seconds")
