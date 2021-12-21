batteryCHARGE = 90  # %
consumRATE = 5      # %/m
steps = 0
step = 1
while batteryCHARGE > consumRATE:
    steps += step
    batteryCHARGE -= consumRATE
    print("STEP:", steps, "CHARGE", batteryCHARGE, "%" )
    if batteryCHARGE <= consumRATE:
        print("WARNING!!!", "Need to charge", sep="\n")