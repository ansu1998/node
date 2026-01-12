'''
file_object = open(file_name, mode)

Read mode ('r'): Opens a file for reading. 

Write mode ('w'): Opens a file for writing. 

Append mode ('a'): Opens a file for appending. 
Binary mode ('b'): Opens the file in binary mode. 


 
'''
f2 = open('abel.txt', 'w')
f2.write("Good")
f2.close()
print("completed")

f1 = open('anil.txt', 'w')
f1.write("hii...it's me")
f1.close()
print('completed')



f0 = open('anil.txt','r')
print(f0.read())
f0.close()

# F0 = open("dinto.txt",'w')
# F0.write("He is a Good Boy")
# F0.close()
# print("it is Working")


# f0 = open('abel.txt','w')
# f0.write("he is a good boy")
# f0.close()
# print("check test files...")


# for i in range(0,10):
#     print(i, end="")

# f0 = open('text7.txt','wb')
# f0.write('1.Apple\n2.orange\n3.pineapple'.encode())
# f0.close()
# print("check the files....")


# f0 = open('text7.txt','rb')
# data = f0.read()
# f0.close()
# print(data.decode())

# python program to print 1 to 10 in file (pratical)

fn = open('product.txt1','w')
for i in range(1,11):
    fn.write(str(i)+'\n')
fn.close()

# using with statement
# with open('myfile.txt', 'w') as f:
#     f.write('DataCamp Black Friday Sale!!!')

# with open('myfile.txt', 'r') as f:
#     print(f.read())

# lst = ['pineapple','banana','orange']
# fn = open('product.txt1','a')
# for i in lst:
#     fn.write(f'{i}\n')
# fn.close()

# f0 = open("test6.txt","w")
# f0.write("Teacher: Why are you late, Frank?\nFrank: Beacause of the sign\nTeacher: What sign.\nTeacher: What sign?\nFrank: The one that says \"School Ahead, Go Slow\" ")
# f0.close()

# f1 = open("test6.txt", "r")
# # print(f1.read())
# print(f1.read(4)) 

# print(f1.readline())


# f = open("myfile.txt", "x")
# f1 = open("myfile.txt", "w")
# f1.write("hiiii...")
# f1.close()   


# print(f1.read(4)) 

# f1 = open("myfile.txt", "r")
# data= f1.read(2)
# print(data)
# f1.close()

# problem 2

# f0 = open("test1.txt","w")
# f0.write("Teacher: Why are you late, Frank?\nFrank: Beacause of the sign\nTeacher: What sign.\nTeacher: What sign?\nFrank: The one that says \"School Ahead, Go Slow\" ")
# f0.close()

# wordcount:6 Teacher: Why are you late, Frank?
# wordcount:5 Frank: Beacause of the sign
# wordcount:3 Teacher: What sign.
# wordcount:3 Teacher: What sign?
# wordcount:10 Frank: The one that says "School Ahead, Go Slow" 



# f0 = open("test1.txt","r")
# for i in f0:
#     print(i)
# f0.close()

# f0 = open("test1.txt","r")
# for i in f0:
#     tokens = i.split(" ")
#     print(len(tokens))
# f0.close()


# f0 = open("test1.txt","r")
# f_out = open("test3.txt","w")
# for i in f0:
#     tokens = i.split(" ")
#     f_out.write("wordcount:"+str(len(tokens))+" "+ i)
# f0.close()
# f_out.close()

