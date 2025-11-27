import sys

if len(sys.argv) > 1:
    scores = list(map(float, sys.argv[1:]))
    print("User provided scores:")
else:
    scores = [80, 70, 75, 60, 50]
    print("No input provided — using default scores:")

total = sum(scores)
avg = total / len(scores)

maximum = max(scores)
minimum = min(scores)

print("\nScores:", scores)
print("Sum:", total)
print("Average:", round(avg, 2))
print("Maximum:", maximum)
print("Minimum:", minimum)
