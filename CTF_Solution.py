for i in range(1,8090): # try all values 1-p
    if (823 ** i) % 8089 == 1228: # if g^i mod p = A
        print(str((6820 ** i) % 8089)) # print B^a mod p (the shared secret)

Solution: 5115


Public Mod: 9834
Public Base: 825
A Secret: 4191
B Secret: 2805
A Public: 5841
B Public: 627
