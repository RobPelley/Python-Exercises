# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 07:10:26 2015

@author: rob

"""

print('|---------------------------------------------------|')
print('| Temperature Converter : Version 1.0 : Rob Pelley  |')
print('|---------------------------------------------------|')
print('| Conversions :                                     |')
print('|---------------------------------------------------|')
print('| 1 : Fahrenheit                                    |')
print('| 2 : Celcius                                       |')
print('| 3 : Kelvin                                        |')
print('| 4 : Rankine                                       |')
print('|---------------------------------------------------|')

convf =   int(input('| Enter Source Conversion [1-4]  : '))
convt =   int(input('| Enter Target Conversion [1-4]  : '))
lower = float(input('| Enter Range from               : '))
upper = float(input('| Enter Range to                 : '))
step  = float(input('| Enter Increment                : '))

print('|---------------------------------------------------|')
print('| Destinations :                                    |')
print('|---------------------------------------------------|')
print('| 1 : Terminal                                      |')
print('| 2 : File                                          |')
print('|---------------------------------------------------|')

dest  =   int(input('| Enter Output Destination [1-2] : '))

print('|---------------------------------------------------|')

if dest == 2 :
    fname = str(input('| CSV File Name            : '))

names = ['Fahrenheit', 'Celcius', 'Kelvin', 'Rankine']
temps = [0.0,0.0,0.0,0.0]

def hdr (d, cf, ct) :
    if d == 1 :
        print('\n---------------------------')
        print('| ' + names[cf].rjust(10) 
           + ' | ' + names[ct].rjust(10) + ' |')
        print('---------------------------')
    else :
        file.write(names[cf] + ',' + names[ct] + '\n')

def lines (d, cf, ct) :
    if d == 1 :
        print('| %10.2f | %10.2f |' % (temps[cf],temps[ct]))
    else :
        file.write(str(temps[cf]) + ',' + str(temps[ct]) + '\n')
    

if convf in [1,2,3,4] and convt in [1,2,3,4] and dest in [1,2] and lower <= upper and step > 0 :
    
    lc = 0

    if dest == 2 : file = open(fname,'w')
    
    if convf == 1 :
        
        hdr(dest, convf - 1, convt - 1)        
    
        f = lower
    
        while f <= upper :
            
            fo = f
            co = (5 * (f - 32)) / 9
            ko = ((f + 459.67) * 5) / 9
            ro = f + 459.67
    
            temps = [fo,co,ko,ro]

            lines(dest, convf - 1, convt - 1)
                   
            lc += 1
            
            f = f + step
                
    elif convf == 2 :
    
        hdr(dest, convf - 1, convt - 1)        
    
        c = lower
    
        while c <= upper :
    
            co = c
            fo = ((9 * c) / 5) + 32
            ko = c + 273.15
            ro = ((c + 273.15) * 9 / 5)
            
            temps = [fo,co,ko,ro]

            lines(dest, convf - 1, convt - 1)
            
            lc += 1
            
            c = c + step
      
    elif convf == 3 :
    
        hdr(dest, convf - 1, convt - 1)        
    
        k = lower
    
        while k <= upper :
    
            co = k - 273.15
            fo = ((k * 9 / 5) - 459.67)
            ko = k
            ro = (k * 9) / 5
            
            temps = [fo,co,ko,ro]

            lines(dest, convf - 1, convt - 1)

            lc += 1
            
            k = k + step
    
    elif convf == 4 :
    
        hdr(dest, convf - 1, convt - 1)        

        r = lower
    
        while r <= upper :
    
            co = ((r - 491.67) * 5) / 9
            fo = r - 459.67
            ko = (r * 5) / 9
            ro = r
            
            temps = [fo,co,ko,ro]

            lines(dest, convf - 1, convt - 1)

            lc += 1
            
            r = r + step
    
    if dest == 1 :
        
        print('---------------------------')
        
    else :
        
        file.close()

        print('-----------------------------------------------------')
        print('| 1 header and ' + str(lc) + ' records written')
        print('-----------------------------------------------------')

else :
    
    print('|---------------------------------------------------|')
    print('| Error : Invalid input                             |')
    print('|---------------------------------------------------|')
 