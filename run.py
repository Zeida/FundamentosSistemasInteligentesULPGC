# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
lh = search.GPSProblem('L', 'H', search.romania)
no = search.GPSProblem('N', 'O', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
ca = search.GPSProblem('C', 'A', search.romania)


print search.Branch_and_Bound(ab).path()
print search.Branch_and_Bound_Heuristic(ab).path()

print "--------------------------------------------"

print search.Branch_and_Bound(lh).path()
print search.Branch_and_Bound_Heuristic(lh).path()

print "--------------------------------------------"

print search.Branch_and_Bound(no).path()
print search.Branch_and_Bound_Heuristic(no).path()

print "--------------------------------------------"

print search.Branch_and_Bound(gz).path()
print search.Branch_and_Bound_Heuristic(gz).path()

print "--------------------------------------------"

print search.Branch_and_Bound(ca).path()
print search.Branch_and_Bound_Heuristic(ca).path()

