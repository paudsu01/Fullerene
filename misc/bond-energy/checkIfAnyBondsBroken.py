from __future__ import annotations
import sys

class InsufficientArgumentsProvided(Exception):
    pass

# bondbefore.dat has bond energies before the simulation
# bondafter.dat has bond energies after the simulation

# line 1: bond between carbon (2,3) 
# line 2: bond between carbon (2,4) 
# ...
# line 59: bond between carbon (2,61) 
# line 60: bond between carbon (3,4) 
# and so on

# 60 choose 2 combinations = 1770

def compareFiles(firstFileName: str, secondFileName: str) -> None:

    # Variables declaration
    currentCarbonAtom1 = 2
    currentCarbonAtom2 = 3
    numberOfLines = 0
    unmatchedCount = 0

    print('PRINTING OUT CARBON BONDS THAT DO NOT MATCH :')
    with open(firstFileName, 'r') as bondBeforeFile, open(secondFileName, 'r') as bondAfterFile:

        for bondBeforeValue, bondAfterValue in zip(bondBeforeFile, bondAfterFile):

            if float(bondBeforeValue) != 0.0 and float(bondBeforeValue) != float(bondAfterValue):
                before = float(bondBeforeValue)* 27.21
                after = float(bondAfterValue)* 27.21
                print(f'C({currentCarbonAtom1},{currentCarbonAtom2}): Before={before:.3f}eV, After={after:.3f}eV, Difference={abs(after-before):.1f}')
                unmatchedCount += 1

            currentCarbonAtom2 += 1

            if currentCarbonAtom2 == 62:
                currentCarbonAtom1 +=1
                currentCarbonAtom2 = currentCarbonAtom1 + 1
            numberOfLines +=1

    print(f'Out of {numberOfLines} different carbon atom combinations, {unmatchedCount} don\'t have the same bond energy values before and after')

if __name__ == "__main__":
    DIFFERENT_LINES = 0

    if len(sys.argv) != 3:
        raise InsufficientArgumentsProvided("Need to provide bondbefore.dat and bondafter.dat as arguments")

    firstFileName = sys.argv[1]
    secondFileName = sys.argv[2]
    compareFiles(firstFileName, secondFileName)

