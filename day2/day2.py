OPTION_SCORES =  {'X':1, 'Y':2, 'Z':3}
D = {'A':'X', 'B':'Y', 'C':'Z'}
L = {'A':'Z', 'B':'X', 'C':'Y'}
W = {'A':'Y', 'B':'Z', 'C':'X'}

RESULT_SCORES =  {'X':0, 'Y':3, 'Z':6}
D_OPTION = {'A':1, 'B':2, 'C':3}
L_OPTION = {'A':3, 'B':1, 'C':2}
W_OPTION = {'A':2, 'B':3, 'C':1}

def main():
    with open('guide.txt') as file:
        rounds = [line.strip() for line in file]
    
    score1 = 0
    score2 = 0
    for round in rounds:
        score1 += OPTION_SCORES[round[2]]
        score1 += check_result(round[0], round[2])

        score2 += RESULT_SCORES[round[2]]
        score2 += get_option(round[0], round[2])

    print(score1)
    print(score2)

def check_result(opp, me):
    if me == D[opp]:
        return 3
    elif me == L[opp]:
        return 0
    elif me == W[opp]:
        return 6

def get_option(opp, outcome):
    if outcome == 'X':
        return L_OPTION[opp]
    elif outcome == 'Y':
        return D_OPTION[opp]
    elif outcome == 'Z':
        return W_OPTION[opp]

if __name__ == "__main__":
    main()