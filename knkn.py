kr1,min1=map(int,raw_input().split())
kr2,min2=map(int,raw_input().split())
x1=kr1*60+min1
x2=kr2*60+min2
d=abs(x1-x2)
t=d%60
t1=(d-t)//60
print t1,t
