python checkIfAnyBondsBroken.py bondbefore$1.dat bondafter$1.dat | awk '{print $3}' | grep -E "After" | sed -E 's/After=//g' | sed -E 's/eV,//' | awk 'BEGIN {sum=0} {sum+=$0} END {print sum/NR}'
