# Definition of Function Recursion in Python
# Recursion in Python is a process where a function calls itself directly or indirectly to solve a problem. 
# It is a common technique used to break down complex problems into smaller, more manageable sub-problems.

# Key Components of Recursion:
# Base Case:
# A condition that stops the recursion to avoid infinite loops. It defines the simplest case of the problem.

# Recursive Case:
# The part of the function where it calls itself with a smaller or simpler input to reduce the problem size.

# def recursive_function(parameters):
#     # Base case: Stop recursion when a condition is met
#     if base_condition:
#         return result

#     # Recursive case: Call the function with modified parameters
#     return recursive_function(modified_parameters)


# def abcd():
#     print("hai")
#     abcd()
# abcd()

# factorials =1
# num=5
# for i in range(1, num+1):
#     factorials = factorials*i
# print(factorials)

def facts(num):
    if num==0 or num==1:
        return 1
    else:
        return num * facts(num-1)
    
print(facts(5))


'''
step-4 2*facts(1)=2
step-3 3*facts(2) =3*2=6
step-2 4*facts(3) = 4*6=24
step-1 5*facts(4)

'''
# fibanocci series pratical 0,1,1,2,3,5,8......


# def fibonacci_iterative(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     # Initialize the first two numbers of the sequence
#     a, b = 0, 1
#     for i in range(2, n+1):
#         a, b = b, a + b  # Update values
#     return b

# # Example usage
# print(fibonacci_iterative(6))

  # Output: 8

def fibanoci(num):
    if num==0 or num==1:
        return num
    else:
        return fibanoci(num-1)+ fibanoci(num-2)
    
fibanoci(6)



'''
F(6)=F(5)+F(4)         
F(5)=F(4)+F(3)
F(4)=F(3)+F(2) 
F(3)=F(2)+F(1) 
F(2)=F(1)+F(0) 
F(1)=1F(0) =0


F(2)=1+0=1
𝐹(3)=1+1=2
F(3)=1+1=2
F(4)=2+1=3
𝐹(5)=3+2=5
𝐹(6)=5+3=8


'''

# step-4  2*fact(1)   
# step-3  3*fact(2)
# step-2  4*fact(3)
# step-1  5*fact(4)






























'''
step=5  
step=4  2*facts(1)   = 2*1=2
stet=3  3*facts(2)   = 3*2 =6
step=2   4*facts(3)  =  4*6= 24 
step =1  5*facts(4)  = 5*24 =120


'''