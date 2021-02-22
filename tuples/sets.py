s = {2,3,4}
print(s)

l = [1,2,3,4,5]
l2 = [6,7,8,9,2]

S = set(l)
print(S)
S1 = set(l2)
print(S1)

print("union: ", S|S1)
print("Intersection: ",S&S1)
print("Difference: ", S - S1)
print("Symmtric diff: ", S^S1)


#Set Quantification
#For all values in set S,values > 0:
#returns true only if all elements qualify
k = all(x > 0 for x in S)
print(k)

#There exist
#returns true when any element in a list /set is true
e = any(x>0 for x in S)
print(e)