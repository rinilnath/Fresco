
    #Create an empty list 'emplist1' using list operation.
emplist1=list()
    #Print 'emplist1'
print(emplist1)
    #Append to empty list 'emplist1' created above with element 9.
emplist1.append(9)
    #Append another element 10 to 'emplist1'
emplist1.append(10)
    #Print 'emplist1'
print(emplist1)
    #Create an empty list 'emplist2' using [].
emplist2=[]
    #Print 'emplist2'
print(emplist2)
    #Extend the empty list 'emplist2' created above with elements 'a', 'b', 'c'.
emplist2.extend(['a','b','c'])
    #Print 'emplist2'
print(emplist2)
    #Extract the last element of 'emplist2' and assign it to variable 'e'.
e=emplist2[-1]
    #Print 'emplist2'
print(emplist2)
    #Print the variable 'e'.
print(e)

############################################################################


    #Generate the list 'k1' having five continuous numbers starting from 0.
k1 = list(range(0,5))
    #Print 'k1'
print(k1)
    #Generate the list 'k2' having five continuous numbers starting from 10.
k2 =list(range(10,15))
    #Print 'k2'
print(k2)
    #Generate the list 'k3' having even numbers between 10 and 20 (including both of them too).
k3 =list(range(10,21,2))
    #Print 'k3'
print(k3)
    #Generate the list 'k4' having numbers from 100 to 1 in decreasing order, which are also multiple of 25.
k4 =list(range(100,0,-25))
    #Print 'k4'
print(k4)

########################################################################################
#Create two sets 'a', and 'b' with following values.
a = set(('10','20','30','40'))
#
#a = ('10','20','30','40')
#
b = set(('30','60'))
#b = ('30','60')
#
#Determine the following
#
#    Union; store the output in variable 'u' and print it.
u = a.union(b)
print(u)
#    Intersection; store the output in variable 'i' and print it.
i = a.intersection(b)
print(i)
#    Difference between set 'a' and 'b'; store the output in variable 'd' and print it.
d =a.difference(b)
print(d)
#    Symmetric difference; store the output in variable 'sd' and print it.
sd = a.symmetric_difference(b)
print(sd)

#
#    Create an empty Dictionary, 'd1' using 'dict' function
d1 =dict()
#    print 'd1'
print(d1)
#    Create a Dictionary 'd2' with Key values p-play , t-talk
d2 ={'p' : 'play', 't' : 'talk'}
#    print 'd2'.
print(d2)
#    Add two new key values : v-vibe, d-docs
d2.update({'v':'vibe','d':'docs'})
#    print 'd2'
print(d2)
#    Remove the key value pair, 'v' - vibe, from 'd2'
del d2['v']
#    print 'd2'
print(d2)
#
#
