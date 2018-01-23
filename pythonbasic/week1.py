print('hello world')
print("hello world 2")
print('Hello world'+'Hello Hong Kong')
print(1+1)
print(3-1)
print(3*4)
print(12/4)
print('iphone'+'4')
#print('iphone'+4)


print(int('2')+3)   
print(int(1.9))     
print(float('1.2')+3)  



print(3**2)  
print(3**3)  
print(3**4)  


print(8%3)  

apple = 1
print(apple)

apple = 'ipgone 7 plus'  
print(apple)

a,b,c = 11,12,13  
print(a,b,c)


condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1

condition = 10
while condition:
    print(condition)
    condition -= 1

a = range(10)

while a:
    print(a[-1])
    a = a[:len(a)-1]


example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)
    
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')


for i in range(1,10):
    print(i)


tup = ('python',2.7,64)
for i in tup:
    print(i)

dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key,dic[key])


s = set(['python','python2','python3','python'])

for item in s:
    print(item)


# define a Fib class
class Fib(object):
    def _init_(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def _iter_(self):
        return self

    def _next_(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n =self.n + 1
            return r
        raise StopIteration()

# using Fib object
for i in Fib(5):
    print(i)

def fib(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a+b
        max -= 1
        yield r

#using generator
for i in fib(5):
    print(i)
