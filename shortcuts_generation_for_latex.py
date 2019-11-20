'''
 Creation of shortcuts for LaTex
'''

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("% -- with mathbb")
for c in alphabet:
    print("\DeclareMathOperator{\\"+c+"}{\mathbb{"+c+"}}")

print("")
print("% -- with mathcal")
for c in alphabet:
    print("\DeclareMathOperator{\m"+c+"}{\mathcal{"+c+"}}")


print("")
print("% -- with \\texttt")
for c in alphabet:
    print("\DeclareMathOperator{\c"+c+"}{\\texttt{"+c+"}}")
