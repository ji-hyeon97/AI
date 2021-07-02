"""
#boolean_type
b=True
print(b)
print(type(b))

#integer_type
i=10
print(i)
print(type(i))

#binary
b=0b010
print(b)
print(type(b))

#octal
o=0o130
print(o)
print(type(o))

#hexadecimal
h=0xABC
print(h)
print(type(h))

#float_type
f=12.34
print(f)
print(type(f))
f=.123
print(f)
print(type(f))
e = 1234e-2
print(e)
print(type(e))

#complex_type
c=1+23j
print(c)
print(c.real)
print(c.imag)
print(type(c))

#string_type
string = "seo"
print(string)
print(type(string))

#list_type
i=[1,2,3]
print(i)
print(type(i))
i=[1,"one",2,"two",3,"three"]
print(i)
print(type(i))

#tuple_type
t=(1,2,3)
print(t)
print(type(t))

#range_type
r=range(10)
print(r)
print(type(r))

#set_type
s={2,3,1}
print(s)
print(type(s))

fs = frozenset(s)
print(fs)
print(type(fs))

#dictionary type
d={1:"one",2:"two"}
print(d)
print(type(d))
"""
"""
#byte_sequence_type
byte = b"\x00"
print(byte)
print(type(byte))
byte=b"Hello"
print(byte)
print(type(byte))
ba=bytearray(byte)
print(ba)
print(type(ba))
mv=memoryview(ba)
print(mv)
print(type(mv))

#bool()
print(bool(True))
print(bool(False))
print(bool(0))
print(bool(10))
print(bool(15.45))
print(bool("seo"))
print(bool(0b010))

#int()
print(int(True))
print(int(False))
print(int(0))
print(int('10'))
print(int(15.45))
print(int(0b010))

#float()
print(float(True))
print(float(False))
print(float(0))
print(float('10'))
print(float(15.45))
print(float(0b010))

#complex()
print(complex(True))
print(complex(False))
print(complex(0))
print(complex('10'))
print(complex(15.45))
print(complex(0b010))

#str()
print(str(True))
print(str(False))
print(str(0))
print(str('10'))
print(str(15.45))
print(str(0b010))
print(str([1,2,3]))

#eval()
print("1+2")
print(eval("1+2"))

#tuple()
print(tuple("seo"))
print(tuple([1,2,3]))

#list()
print(list("seo"))
print(list([1,2,3]))
print(list({1:"one",2:"two"}))

#set()
print(set("seo"))
print(set([1,2,3]))
"""
"""
#frozenset()
print(frozenset("seo"))
print(frozenset([1,2,3]))

#dict()
print(dict({1:"one",2:"two"}))
print(dict({"one":1,"two":2}))

#chr()
print(chr(97))
print(chr(65))

#ord()
print(ord('a'))
print(ord('A'))

#bin()
print(bin(True))
print(bin(False))
print(bin(10))

#oct()
print(oct(True))
print(oct(False))
print(oct(10))

#hex()
print(hex(True))
print(hex(False))
print(hex(10))

#bytes()
print(bytes(True))
print(bytes(False))
print(bytes(10))

#min()
print(min(1,2,3))

#max()
print(max(1,2,3))

#sum()
print(sum((1,2,3)))

#divmod()
print(divmod(3,5))
print(divmod(11,5))

#abs()
print(abs(-4))
print(abs(4))

#pow()
print(pow(2,3))

#len(s)
print(len("string"))
print(len((1,2,3)))
"""
#round()
print(round(3.14))
print(round(3.141592,2))
print(round(0.6))

#all()
print(all(()))
print(all((False,False,True)))

#any()
print(any(()))
print(any((False,False,True)))

#산술연산자
a=2
b=5
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

#비교연산자
a=2
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#할당연산자
a=2
b=5
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a**=b
print(a)
a//=b
print(a)

#비트연산자
a=2
b=5
print(a&b,bin(a&b))
print(a|b,bin(a|b))
print(a^b,bin(a^b))
print(a<<b,bin(a<<b))
print(a>>b,bin(a>>b))

#논리연산자
print(True and True)
print(True and False)
print(True or True)
print(not True)

#멤버연산자
a=2
b=5
i=[2,4,8]
print(a in i)
print(b in i)
print(a not in i)
print(b not in i)

#식별연산자
a=2
b=5
print(a is b)
print(a is not b)

#연산자 우선순위









