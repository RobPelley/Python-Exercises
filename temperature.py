# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 07:10:26 2015

@author: rob

"""

print('|---------------------------------------------------|')
print('| Temperature Converter : Version 1.0 : Rob Pelley  |')
print('|---------------------------------------------------|')
print('| 1 : Fahrenheit                                    |')
print('| 2 : Celcius                                       |')
print('| 3 : Kelvin                                        |')
print('| 4 : Rankine                                       |')
print('|---------------------------------------------------|')

conv  =   int(input('| Convert     [1-4] : '))
lower = float(input('| Range from        : '))
upper = float(input('| Range to          : '))
step  = float(input('| Increment         : '))

print('|---------------------------------------------------|')
print('| 1 : Terminal                                      |')
print('| 2 : File                                          |')
print('|---------------------------------------------------|')

dest  =   int(input('| Destination [1-2] : '))

if dest == 2 :
    fname = str(input('| File Name         : '))

names = ['Fahrenheit', 'Celcius', 'Kelvin', 'Rankine']

def hdr (d, c1, c2, c3, c4) :
    if d == 1 :
        print('-----------------------------------------------------')
        print('| ' + names[c1].rjust(10) 
           + ' | ' + names[c2].rjust(10)
           + ' | ' + names[c3].rjust(10)
           + ' | ' + names[c4].rjust(10) + ' |')
        print('-----------------------------------------------------')
    else :
        file.write(names[c1] + ',' + names[c2] + ',' + names[c3] + ',' + names[c4] + '\n')

if conv in [1,2,3,4] and dest in [1,2] and lower <= upper and step > 0 :
    
    if dest == 2 : file = open(fname,'w')
    
    if conv == 1 :
        
        hdr(dest, 0, 1, 2, 3)        
    
        lc = 1

        f = lower
    
        while f <= upper :
            
            fo = f
            co = (5 * (f - 32)) / 9
            ko = ((f + 459.67) * 5) / 9
            ro = f + 459.67
    
            if dest == 1 :
                print('| %10.2f | %10.2f | %10.2f | %10.2f |' % (fo,co,ko,ro))
            else :
                file.write(str(fo) + ',' + str(co) + ',' + str(ko) + ',' + str(ro) + '\n')
                   
            lc += 1
            
            f = f + step
                
    elif conv == 2 :
    
        hdr(dest, 1, 0, 2, 3)
    
        lc = 1

        c = lower
    
        while c <= upper :
    
            co = c
            fo = ((9 * c) / 5) + 32
            ko = c + 273.15
            ro = ((c + 273.15) * 9 / 5)
            
            if dest == 1 :
                print('| %10.2f | %10.2f | %10.2f | %10.2f |' % (co,fo,ko,ro))
            else :
                file.write(str(co) + ',' + str(fo) + ',' + str(ko) + ',' + str(ro) + '\n')
            
            lc += 1
            
            c = c + step
      
    elif conv == 3 :
    
        hdr(dest, 2, 3, 0, 1)
    
        lc = 1
        
        k = lower
    
        while k <= upper :
    
            co = k - 273.15
            fo = ((k * 9 / 5)- 459.67)
            ko = k
            ro = (k * 9) / 5
            
            if dest == 1 :
                print('| %10.2f | %10.2f | %10.2f | %10.2f |' % (ko,ro,fo,co))
            else :
                file.write(str(ko) + ',' + str(ro) + ',' + str(fo) + ',' + str(co) + '\n')

            lc += 1
            
            k = k + step
    
    elif conv == 4 :
    
        hdr(dest, 3, 2, 0, 1)

        lc = 1
        
        r = lower
    
        while r <= upper :
    
            co = ((r - 491.67) * 5) / 9
            fo = r - 459.67
            ko = (r * 5) / 9
            ro = r
            
            if dest == 1 :
                print('| %10.2f | %10.2f | %10.2f | %10.2f |' % (ro,ko,fo,co))
            else :
                file.write(str(ro) + ',' + str(ko) + ',' + str(fo) + ',' + str(co) + '\n')
            
            lc += 1
            
            r = r + step
    
    print('-----------------------------------------------------')
        
    if dest == 2 : 
        file.close()
        print('| ' + str(lc) + ' records witten')
        print('-----------------------------------------------------\n')

else :
    
    print('\nError : Invalid input');
 