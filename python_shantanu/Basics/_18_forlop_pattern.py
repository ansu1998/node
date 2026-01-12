'''
nested loop= a loop within loop (outer, inner)
outer loop:
    inner loop
'''

#  print("hi", end="")
# print("hello")
# print("hello")

for i in range(5):
    for j in range(4):
        print("hello", end=" ")
    print()
'''
i=0 j=0,4 hello hello hello hello
i=1 j=0,4 hello hello hello hello
i=2 j=0,4 hello hello hello hello
i=3

'''
# for i in range(0,4):
#     for j in range(4):
#         print("hello", end=' ')
#     print()

# for i in range(3):
#     for j in range(3):
#         print("*", end=' ')
#     print()


'''
i=0 j=0 hello hello  hello  hello
i=1 j=0 to 4    hello hello  hello  hello
i=2 j=0 to 4    hello hello  hello  hello
i=3 j=0 to 4    hello hello  hello  hello
i=4  j=0 to 4    hello hello  hello  hello 


***
***
***
***
***
***
'''

# for i in range(6):
#     for j in range(3):
#         print('*', end=' ')
#     print()


'''
* * * * * 
* * * * * 
'''


# for x in range(0,2):
#     for y in range(1,6):
#         print('*', end=" ")
#     print()

'''

x=0 y=0,1,2,3,4,5
x=1 y=0,1,2,3,4,5
------------------------------------------------
'''



'''
i=1 j=1 (1,1)(1,2)(1,3)
i=2 (2,1)(2,2)(2,3)
i=3  (3,1),(3,2(3,3))
""
""
'''

# for i in range(1,6):
#     for j in range(1,4):
#         print((i,j) , end="")
#     print()



# 1,
'''
* 
* *
* * *
* * * *
* * * * *

'''

num=5
for i in range(0,num):
    for j in range(i+1):
        print('*', end=" ")
    print()

# num=5
# for i in range(1,num+1):
#     for j in range(i):
#         print('*', end=" ")
#     print()


'''
1, 
concept
i=1, j=(1,2)  *
i=2  j=(1,3)  **
i=3  j=(1,4)  ***
i=4  j=(1,5)  ****
i=5  j=(1,6)  *****
i=6  j=(1,7)  ******

'''

# num=6
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('*', end=" ")
#     print()

'''
2,Next question

*
***
*****
*******
*********
 
i=(1,6)


# '''


# num=5
# k=1
# for i in range(1, num+1):
#     for j in range(k):
#         print('*', end="")
#     k=k+2
#     print()
    

# num=int(input("enter the number of rows: "))
# k=1
# for i in range(1,num+1):
#     for j in range(1,k+1):
#         print("*", end="")
#     k=k+2
#     print()
   

# 3,
'''

space   star 
j=4       *
j=3      *  *
j=2    *   *  *
j=1   *  *  *   *
j=0  *  *  *   *  *


'''

# num = int(input("enter the rows: "))
# num=5
# for i in range(1, num+1):
#     for j in range(num-i):
#         print(end=" ")
#     for j in range(i):
#         print('*', end=" ")
#     print()



# num = int(input("Enter the number of rows: "))
# for i in range(0,num):
#     for j in range(0, num-i-1):
#         print(end=" ")
#     for k in range(0, i+1):
#         print("*", end=' ')
#     print()


# Excercise

'''

    *
   ***
  *****
 *******
*********



* * * * *
 * * * *
  * * *
   * *
    *


* * * * * *
* * * * *
* * * *
* * *
* *
*

   * 
  * *
 * * *
* * * *
 * * *
  * *
   *
'''


'''

    *
   ***
  *****
 *******
*********

'''
# row = 5
# k=1
# for i in range(1,row+1):
#     for j in range(0,row-i):
#         print(" ",end="")
#     for n in range(1,k+1):
#         print("*", end="")
#     k=k+2
#     print()
    
        
# num= int(input("enter the number of rows: "))
# for i in range(0,num):
#     for j in range(0, num-i-1):
#         print(end=" ")
#     for j in range(0,2*i+1):
#         print("*", end="")
#     print()


# 5,
'''     
* * * * *
 * * * *
  * * *
   * *
    *

i=1  j1=0  j2=5
i=2  j1=1  j2=4
i=3  j1=2  j2=3
i=4  j1=3  j2=2
i=5  j1=4  j2=1 

'''

# num= int(input("enter the rows: "))
# for i in range(0,num):
#     for j in range(0,i):
#         print(" ",end="")
#     for j in range(0,num-i):
#         print("*",end=" ")
#     print()



# num = int(input("Enter the number of rows: "))
# for i in range(num,0,-1):
#     for j in range(0, num-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("*", end=' ')
#     print()


# excercise
# 6,

'''
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''




'''
   * 
  * *
 * * *
* * * *
 * * *
  * *
   *
'''

# def pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1)+'* '*(i+1))
#     for j in range(rows-1,0,-1):
#         print(" "*(rows-j)+"* "*(j))
# pyramid(4)


# 7, 
'''
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
# num=int(input("enter the number of rows: "))
# for i in range(num,0,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()




# or

# num=6
# for i in  range(0,num):
#     for j in range(num-i):
#         print("*", end="")
#     print()
''' 
num=5 i=(5,0)  * * * * *
i=5 j=(0,5)    * * * *
i=4 j=(0,4)    * * *
i=3 j=(0,3)    * *
i=2  j=(0,2)   *
i=1  j=(0,1)
'''


# 8,
'''
    01234
0    *** 
    *   *
    *   *
    *****
    *   *
    *   *
    *   *

'''
# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4 )):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


'''
*   * 
*   *
*   *
*****
*   *
*   *
*   *
'''
# for row in range(8):
#     for col in range(6):
#         if (((col==0 or col==4) and row!=0) or ((row==4) and (col>0 and col<4))):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


'''
* * *
*
* * *
*
*
'''

# for row in range(6):
#     for col in range(3):
#         if (((col==0)) or ((row==0 or row==2) and (col>=0 and col<=3))):
#             print("* ", end="")
#         else:
#             print(end=" ")
#     print()


