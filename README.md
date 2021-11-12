drive function
	activate robot's motors 
	after a setted time stop robot's motor
	
turn function 
	activate robot's motor in opposite directions
	after a setted time stop  robot's motor
	
find silver token function 
	set color to g
	set distance to 100
	for all the token the robot sees
		if the token is golden and it is the nearest in front of the robot
			save distance and angle of the token
			set color to g
		if the token is silver and it is the nearest in front of the robot
			save distance and angle of the token
			set color to s
	if color is s
		return distance and angle of the token
	else
		return negative values

find golden token function 
	set distance to 100
	for all the token the robot sees
		if the golden token is the nearest
			save his dist and his angle
	if the distance is 100
		return negative values
	else
		return distance and angle

find golden token on the side function
	set distance to 100
	for all the token the robot sees
		if the token is the nearest on the side
			save angle and distance
	if distance is 100
		return negative values
	else
		return distance and angle
			
turn back function
	set distance to 100
	for all the token the robot sees
		if the token has code 0
			save distance and angle
	if the angle is positive
		turn 180 degrees clockwise
	else
		turn 180 degrees counterclockwise
		
		
main function
	while true
		call find siilver token function
		if the fuction doesen't find silver token
			call golden token function
			if the robot isn't perpendicular to the golden token 
				turns a little bit to become
			if the nearest golden token is in front of the robot
				call find golden token on the side
				if positive angle turn left
				else turn right
		else
			if enough closer to the silver token
				grab the toke
				call turn back function
				release
				recall turn back function
			else if the robot is weel aligned
				proceed straight
			else if isn't weel aligned 
				turn right
			else 
				turn left
				
				
				
				

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
************************************************IMPROVEMENTS***********************************************************************************
*merge find silver token and find golden token functions (less clear code)
*make a more accurate function to turn back (exactly 180 degrees)

				
				
		
			
