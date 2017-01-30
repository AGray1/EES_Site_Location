PiA = 3.283 #sets abitrary values for the three times 
PiB = 4.309
PiC = 3

PiADistance = 6#PiA * float(2.99792458) #uses speed=dist/time to calculate distance from time given.
PiBDistance = 12#PiB * float(2.99792458) #NOTE: s=d/t calculations disabled for accuracy when testing
PiCDistance = 8.5#PiC * float(2.99792458)

b1 = [6,6] #stores the x,y co-ords of each beacon in an array
b2 = [20,9]
b3 = [4,19]

d = (((b1[0]-b2[0])**2)+((b1[1]-b2[1])**2))**0.5 #pythoagoras theorem to calculate distance between b1 and b2
print ('distance= ', d)

if d > abs(PiADistance + PiBDistance): #Checks that the beacons aren't further apart than the sum of the distances
        print ('error, zones are seperate')
else:
        s = (PiADistance + PiBDistance + d) /2 #Herons Formula
        area = (s*(s - PiADistance)*(s - PiBDistance)*(s - d))**0.5 
        height = (2*area) / d
        print ('height= ', height)
        print ('s= ', s)
        print ('area= ', area) 
        a = (PiADistance**2 - height**2)**0.5 #Calculates a, the distance from b1 to the centre point
        print ('a= ', a)
        grad = (b1[1] - b2[1]) / (b1[0] - b2[0]) #dy/dx to find gradient between b1 and b2
        print ('grad= ', grad)
        if grad == 0: #calculates perpendicular gradient with clause to stop division by 0
                pgrad = 1
        else:
                pgrad = (-1)/grad
        print ('perpendicular grad= ', pgrad)
        #centre
        centre = [b1[0]+a*(1+grad**2)**0.5, b1[1]+grad*((a/d)*b2[0])] #Need to fully test this section
        
        #Change in x
        xchange = (height**2/(pgrad**2 + 1))**0.5
        
        #one of the two circle intersections
        intersection1 = [centre[0] + xchange, centre[1] + pgrad*xchange]

        #the second intersection
        intersection2 = [centre[0] - xchange, centre[1] - pgrad*xchange]
        
        print ('centre= ', centre)
        print ('intersection1= ', intersection1)
        print ('xchange= ', xchange)
        print ('intersection2= ', intersection2)
        
        """intersection is found by using y=mx then rearranging pythoagoras' theorem
        to give a value to the amount the x co-ord has changed from the centre point,
        then sub back into y=mx to find the amount the y co-ord has changed:
        x=(h^2/(m^2+1))^0.5"""
        #After finding the 2 points of intersection, this finds which point is closer to the circumference of the circle within +_5%
        b3i1 = ((b3[0]-intersection1[0])**2 + (b3[1]-intersection1[1])**2)**0.5
        b3i2 = ((b3[0]-intersection2[0])**2 + (b3[1]-intersection2[1])**2)**0.5
        if abs(b3i1 - PiCDistance) > 0.05*PiCDistance and abs(b3i2 - PiCDistance) > 0.05*PiCDistance: #think this line works but need to make sure...
                print ('Insufficient Accuracy, > +_ 5%')
        elif abs(b3i1-PiCDistance)> abs(b3i2-PiCDistance):
                print ('User is at point', intersection2)
        elif abs(b3i2-PiCDistance)> abs(b3i1-PiCDistance):
                print ('User is at point', intersection1)
        else:
                print ('error')
print (abs(b3i1 - PiCDistance))
print (abs(b3i2 - PiCDistance))
print (b3i2)
print ('PiA= ', PiA)
print ('PiB=', PiB)
print ('PiC= ', PiC)
print ('PiADistance= ', PiADistance)
print ('PiBDistance= ', PiBDistance)
print ('PiCDistance= ', PiCDistance)
"""
NB: height of scalene triangle:
Use Heron's formula to calc. area, then rearrange a=(b/2)*h.
Heron's formula s=(A+B+C)/2; Area= sqrt(S(S-A)(S-B)(S-C))
"""
#lines to test:
        #35 (defining centre)
        #38 (change in x co-ord from b1 to centre point)
        #58 (testing if either intersection is within +_ 5% of the radius of PiCDistance)
