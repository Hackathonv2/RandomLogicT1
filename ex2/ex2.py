def prevoir_tempete(s1, s2):
    communs = set(s1) & set(s2)

    ordre_s1 = [c for c in s1 if c in communs]
    ordre_s2 = [c for c in s2 if c in communs]

    if ordre_s1 == ordre_s2:
        print("TEMPETE")
        print("".join(ordre_s1))
    else:
        print("NORMAL")

s1 = input().strip()
s2 = input().strip()

prevoir_tempete(s1, s2)

