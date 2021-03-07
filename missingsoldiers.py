# Write your code here
a = int(input())

#a list to hold the barriers coordinates
barriers = []

#The user provides coordinates
for i in range(a):
    [x,y,d] = [int(c)
    for c in input().split()] 
    barriers.append([x,x+d])

# we use the sort method to sort the barriers
barriers.sort()

#the counter for total number of ants to be blocked
count = 0
antsblocked = 0

# for loop to block ants in the coordinates
for barrier in barriers:
    if(barrier[0] >= count):
        count = barrier[0]
        if(count < barrier[1]):
            antsblocked = antsblocked + (barrier[1] - count)+1
            count = barrier[1]+1
    elif(count <= barrier[1]):
            antsblocked = antsblocked + (barrier[1] - count)+1
            count = barrier[1]+1

# the total number of blocked ants
print (antsblocked)

