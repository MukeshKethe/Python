#Memory Alocation Example - 1
a = 100
b = 200
print(id(a))
print(id(b))
'''In Example - 1 a, b variables store different value
   so, a, b refers to different block in memory
   Therefore a, b variables contains different block address'''

#Memory Alocation Example - 2
a = 100
b = 100
print(id(a))
print(id(b))
'''In Example - 2 a, b variables store same value
   so, a, b refers to same block in memory
   Therefore a, b variables contains same block address'''

'''In Example - 2 a, b variables contains same block address
   because python follows object oriented approach''' 
