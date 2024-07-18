python checkIfAnyBondsBroken.py bondbefore$1.dat bondafter$1.dat | awk '{print $2}' | grep -E "Before" | sed -E 's/Before=//g' | sed -E 's/eV,//' | awk 'BEGIN {sum=0} {sum+=$0} END {print sum/NR}'
