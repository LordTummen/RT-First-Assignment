from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0

d_th = 0.4

silver = True

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    
    #this function check if the nearest token is a silver one
    color="g"
    dist=100
    for token in R.see():
        #the robot looks straight ahead, takes the distance from the token and his color. If the color is golden the variable color is setted as "g"
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.rot_y >= -90 and token.rot_y <= 90 :
            dist=token.dist
            color="g"
            rot_y=token.rot_y
        #if the color is golden the variable color is setted as "s"
        elif token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.rot_y >= -90 and token.rot_y <= 90:
            dist=token.dist
            color="s"
            rot_y=token.rot_y
    #if color is "s" the function returns the distance and the angle
    if(color=="s"):
        return dist, rot_y
    #if color is "g" the function returns negative values
    else:
        return -1, -1

def find_golden_token():
    dist=100
    for token in R.see():
        #search for golden token in front of the robot
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD :
            dist=token.dist
            rot_y=token.rot_y
    if dist==100:
	    return -1, -1
    else:
   	    return dist, rot_y

def find_golden_token_on_the_side():
    #this function looks only for the token on the sides of the robot 
    dist=100
    for token in R.see():
        #the function looks only for tokens that forms an angle beetween 80 and 100 degrees with the robot
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and ((token.rot_y >=-100 and token.rot_y <= -80)or(token.rot_y >=80 and token.rot_y <= 100)):
            dist=token.dist
            rot_y=token.rot_y
    if dist==100:
	    return -1, -1
    else:
   	    return dist, rot_y


def turn_back():
    dist=100                                                                    #set dist to 100
    for token in R.see():                                                       #for all tokens the robot sees
        if token.info.code == 0:                                                #choose the token with code 0
            angle=token.rot_y                                                   #save his angle and distance
            dist=token.dist
    if angle>0:                                                                 #if the angle is positive
        finalangle=angle-175                                                    #turn clockwise until the angle is greater than 175 degrees from the initial angle
        while angle>finalangle:
            turn(20,0.1)
            for token in R.see():
                if token.info.code == 0:
                    angle=token.rot_y
    else:                                                                       #if the angle is negative turn counterclockwise
        finalangle=angle+175
        while angle<finalangle:
            turn(-20,0.1)
            for token in R.see():
                if token.info.code == 0:
                    angle=token.rot_y




def main():

    while 1:                                                              
        dists, angles = find_silver_token()                                     #call the function to find if there is a silver token near the robot
        if(dists==-1):                                                          #if there isn't a silver token near the robot
            distg, angleg = find_golden_token()                                 #call the function to search for the nearest golden token 
            if(angleg>-82 and angleg<=-10):                                     #if the robot isn't perpendicular with the nearest golden token it turns to become
                turn(20,0.1)
            elif(angleg>=10 and angleg<82):
                turn(-20,0.1)
            elif(angleg<10 and angleg>-10):                                     #if there is a golden token in front of the robot
                ditgft, anglegft = find_golden_token_on_the_side()              #call the function to find golden token on the side, in order to decide if the robot must turn to left or turn to right
                if(anglegft>80 and anglegft<100):                               #if the block is on the right the robot turns left
                    turn(-20,0.5)
                else:                                                           #else the robot turns right   
                    turn(20,0.5)
            else:
                drive(50,0.1)                                                   #if the robot is well aligned it goes straight ahead
        else:                                                                   #if the nearest token is a silver token
            if dists <d_th:                                                     #if the robot is close enough it grab the token 
                print("Found it!")
                R.grab()
                turn_back()                                                     #call the function to to turn 
                drive(20,1)                         
                R.release()                                                     #release it
                drive(-20,1)
                turn_back()                                                     #call the function to to turn
            elif -a_th<= angles <= a_th:                                        # if the robot is well aligned with the token, we go forward
                print("Ah, here we are!.")
                drive(50, 0.1)
            elif angles < -a_th:                                                # if the robot is not well aligned with the token, we move it on the left or on the right
                print("Left a bit...")
                turn(-2, 0.5)
            elif angles > a_th:
                print("Right a bit...")
                turn(+2, 0.5)


main()
