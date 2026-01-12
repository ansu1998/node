import random 

#randint = Returns a random number between the given range (include 7)
# a<=x<=b
a = random.randint(1,7)
print(a)


# randrange=Returns a random number between the given range
# a<=x<b
# random.randrange(start, stop, step)
# a= random.randrange(1,6) 
a= random.randrange(1,6,2)
print(a)
# 1,3,5


# Returns a random float number between 0 and 1
a= random.random()
print(a)

# Returns a random float number between two given 
# parameters
a=random.uniform(1,3)
print(a)


# Takes a sequence and returns the sequence in a 
# random order
l= [12,83,14,50]
random.shuffle(l)
print(l)



