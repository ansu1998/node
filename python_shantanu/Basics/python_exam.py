# a= students.objects.all()
# a= students.objects.get(name='ansu')
# s= 'aaaabbbccd"
# ouput = '4a3b2c1d'


s= 'aaaabbbccd'
str2=''
out=''
count=1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count = count+1
    else:
        out += str(count) + s[i-1]
        count=1
        # print(count)
out += str(count) + s[-1]
print(out)