#6001
print("Hello")

#6002
print("Hello World")

#6003
print("Hello")
print("World")

#6004
print("'Hello'")

#6005
print('"Hello World"')

#6006
print("\"!@#$%^&*()'")

#6007
print('"C:\\Download\\\'hello\'.py"')

#6008
print('''print("Hello\\nWorld")''')

#6009
c = input()
print(c)

#6010
n = input()
n = int(n)
print(n)

#6011
f = input()
f = float(f)
print(f)

#6012
a = input() 
b = input()
a=int(a)
b=int(b)
print(a)
print(b)

#6013
a = input() 
b = input()
print(b)
print(a)

#6014
f = input()
f = float(f)
print(f)
print(f)
print(f)


#6015
a, b  = input().split( )
a = int(a)
b = int(b)
print(a)
print(b)


#6016
a, b = input().split()
print(b, a)

#6017
s = input()
print(s, s, s)

#6018
a, b = input().split(':')
print(a, b, sep = ':')

#6019
y, m, d = input().split('.')
print(d, m, y, sep = '-')

#6020
a, b = input().split('-')
print(a, b, sep = '')

#6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#6022
s=input()
print(s[0:2], s[2:4], s[4:6], sep = ' ')

#6023
s = input()
print(s[s.find(':')+1:s.rfind(':')])

#6024
w1, w2 = input().split()
s = w1 + w2
print(s)

#6025
a, b = input().split()
s = int(a)+int(b)
print(s)

#6026
a = input()
b = input()
af = float(a)
bf = float(b)
s = af+bf
print(s)


#6027
a = input()
n = int(a)
print('%x'% n) 

#6028
a = input()
n = int(a)
print('%X'% n) 

#6029
a = input()
n = int(a, 16)    
print('%o' % n)  

#6030
n = ord(input())
print(n)

#6031
c = int(input())
print(chr(c)) 

#6032
c = int(input())
print(-c) 

#6033
n = ord(input())
print(chr(n+1))

#6034
a, b = input().split()
c = int(a) - int(b)
print(c)

#6035
a, b = input().split()
c = float(a)*float(b)
print(c)

#6036
w, n = input().split()
print(w*int(n))

#6037
n = input()
w = input()
print(w*int(n))

#6038
a, b = input().split()
print(int(a)**int(b))

#6039
a, b = input().split()
print(float(a)**float(b))

#6040
a, b = input().split()
print(int(a)//int(b))

#6041
a, b = input().split()
print(int(a)%int(b))

#6042
a=input()
a=float(a)
print(format(a, ".2f"))

#6043
a, b = input().split()
c = float(a)/float(b)
print(format(c, ".3f"))

#6044
a, b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))
c = int(a)/int(b)
print(format(c, ".2f"))

#6045
a, b, c = input().split()
d = int(a)+int(b)+int(c)
e = d/3
print(d, format(e, ".2f"))

#6046
n = input()
print(int(n)<<1)

#6047
a, b = input().split()
print(int(a)<<int(b))

#6048
a, b = input().split()
c = int(a) - int(b)
print(c<0)

#6049
a, b = input().split()
print(a==b)

#6050
a, b = input().split()
c = int(a) - int(b)
print(c<=0)
