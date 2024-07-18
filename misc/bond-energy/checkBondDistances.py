from __future__ import annotations
import sys
import argparse

def main(file1Name : str, file2Name: str) -> None:

    currentCarbonAtom1 = 2
    currentCarbonAtom2 = 3

    sumBefore = 0
    sumAfter = 0
    count = 0
    with open(file1Name, 'r') as file1, open(file2Name, 'r') as file2:
        for line1, line2 in zip(file1, file2):

            distanceBefore = float(line1.split()[-1])
            distanceAfter = float(line2.split()[-1])
            print(f'C({currentCarbonAtom1}, {currentCarbonAtom2}) Distance before: {distanceBefore}, Distance After:{distanceAfter}, Difference: {distanceAfter - distanceBefore}')
            sumBefore += distanceBefore
            sumAfter += distanceAfter
            count += 1

            currentCarbonAtom2 += 1
            if currentCarbonAtom2 == 62:
                currentCarbonAtom2 = 0
                currentCarbonAtom1 += 1
        print(f'Average distance before : {sumBefore/count:.5f}, Average distance after : {sumAfter/count:.5f}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file1')
    parser.add_argument('file2')
    args = parser.parse_args()
    file1 = vars(args)['file1']
    file2 = vars(args)['file2']

    main(file1, file2)
