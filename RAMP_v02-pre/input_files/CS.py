# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''

from core import User, np, pd
User_list = []


'''
This example input file represents Italian households' cooking behaviour.
'''

#Create new user classes
Family_type1a_br = User("family type 1a breakfast", 500, 0, ([0.11,0.12,0.14,0.07,0.19,0.37]), ([1,0.5,0.214,0.007,0.005,0]), 18264)
User_list.append(Family_type1a_br)

Family_type1a_lu = User("family type 1a lunch",500, 0, ([0.11,0.13,0.14,0.07,0.23,0.33]), ([1,0.5,0.214,0.007,0.005,0]), 18264)
User_list.append(Family_type1a_lu)

Family_type1a_di = User("family type 1a dinner",500, 0, ([0.02,0.05,0.13,0.1,0.32,0.38]), ([1,0.5,0.214,0.007,0.005,0]), 18264)
User_list.append(Family_type1a_di)

Family_type1b_br = User("family type 1b breakfast",500, 0, ([0.11,0.12,0.14,0.07,0.19,0.37]), ([1,0.5,0.214,0.007,0.005,0]), 18264)
User_list.append(Family_type1b_br)

Family_type1b_lu = User("family type 1b lunch",500, 0, ([0.11,0.13,0.14,0.07,0.23,0.33]), ([1,0.5,0.214,0.007,0.005,0]), 18264)
User_list.append(Family_type1b_lu)

Family_type1b_di = User("family type 1b dinner",500, 0, ([0.02,0.05,0.13,0.1,0.32,0.38]), ([1,0.5,0.214,0.007,0.005,0]), 18264)
User_list.append(Family_type1b_di)


Family_type2a_br = User("family type 2a breakfast",500, 0, ([0.11,0.12,0.14,0.07,0.19,0.37]), ([1,0.5,0.214,0.007,0.005,0]), 5117)
User_list.append(Family_type2a_br)

Family_type2a_lu = User("family type 2a lunch",500, 0, ([0.11,0.13,0.14,0.07,0.23,0.33]), ([1,0.5,0.214,0.007,0.005,0]), 5117)
User_list.append(Family_type2a_lu)

Family_type2a_di = User("family type 2a dinner",500, 0, ([0.02,0.05,0.13,0.1,0.32,0.38]), ([1,0.5,0.214,0.007,0.005,0]), 5117)
User_list.append(Family_type2a_di)

Family_type2b_br = User("family type 2b breakfast",500, 0, ([0.11,0.12,0.14,0.07,0.19,0.37]), ([1,0.5,0.214,0.007,0.005,0]), 5117)
User_list.append(Family_type2b_br)

Family_type2b_lu = User("family type 2b lunch",500, 0, ([0.11,0.13,0.14,0.07,0.23,0.33]), ([1,0.5,0.214,0.007,0.005,0]), 5117)
User_list.append(Family_type2b_lu)

Family_type2b_di = User("family type 2b dinner",500, 0, ([0.02,0.05,0.13,0.1,0.32,0.38]), ([1,0.5,0.214,0.007,0.005,0]), 5117)
User_list.append(Family_type2b_di)

#Create new appliances

breakfast_w1 = [360,600]
breakfast_w2 = [17*60,18*60]
breakfast_w3 = [21*60,1440]
lunch = [750,960]
dinner = [1110,1230]

#Familiy type 1a
breakfast_1 = Family_type1a_br.Appliance(Family_type1a_br,1,850,3,15,0.1,3, fixed_cycle=0, thermal_P_var = 0.2)
breakfast_1.windows(breakfast_w1,breakfast_w2,0.2,breakfast_w3)

lunch_1 = Family_type1a_lu.Appliance(Family_type1a_lu,1,1500,1,20,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch_1.windows(lunch,[0,0],0.3)
lunch_1.specific_cycle_1(850,20,0,0,0.1) 
lunch_1.cycle_behaviour([11*60,13*60],[0,0])

lunch2_1 = Family_type1a_lu.Appliance(Family_type1a_lu,1,1500,1,15,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch2_1.windows(lunch,[0,0],0.3)
lunch2_1.specific_cycle_1(1050,15,0,0,0.1)
lunch2_1.cycle_behaviour([11*60,13*60],[0,0])

dinner_1 = Family_type1a_di.Appliance(Family_type1a_di,1,1500,1,18,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner_1.windows(dinner,[0,0],0.3)
dinner_1.specific_cycle_1(2100,8,850,10,0.1)
dinner_1.cycle_behaviour([18*60,20*60],[0,0])

dinner2_1 = Family_type1a_di.Appliance(Family_type1a_di,1,1500,1,15,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner2_1.windows(dinner,[0,0],0.3)
dinner2_1.specific_cycle_1(1250,10,0,0,0.1)
dinner2_1.cycle_behaviour([18*60,20*60],[0,0])

#Family type 1b
breakfast_1 = Family_type1b_br.Appliance(Family_type1b_br,1,850,3,15,0.1,3, fixed_cycle=0, thermal_P_var = 0.2)
breakfast_1.windows(breakfast_w1,breakfast_w2,0.2,breakfast_w3)

dinner_1 = Family_type1b_di.Appliance(Family_type1b_di,1,1500,1,20,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner_1.windows(dinner,[0,0],0.3)
dinner_1.specific_cycle_1(850,20,0,0,0.1) 
dinner_1.cycle_behaviour([18*60,20*60],[0,0])

dinner2_1 = Family_type1b_di.Appliance(Family_type1b_di,1,1500,1,15,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner2_1.windows(dinner,[0,0],0.3)
dinner2_1.specific_cycle_1(1050,15,0,0,0.1)
dinner2_1.cycle_behaviour([18*60,20*60],[0,0])

lunch_1 = Family_type1b_lu.Appliance(Family_type1b_lu,1,1500,1,18,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch_1.windows(lunch,[0,0],0.3)
lunch_1.specific_cycle_1(2100,8,850,10,0.1)
lunch_1.cycle_behaviour([11*60,13*60],[0,0])

lunch2_1 = Family_type1b_lu.Appliance(Family_type1b_lu,1,1500,1,15,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch2_1.windows(lunch,[0,0],0.3)
lunch2_1.specific_cycle_1(1250,10,0,0,0.1)
lunch2_1.cycle_behaviour([11*60,13*60],[0,0])


#Family type 2a
breakfast_1 = Family_type2a_br.Appliance(Family_type2a_br,1,900,3,24,0.1,3, fixed_cycle=0, thermal_P_var = 0.2)
breakfast_1.windows(breakfast_w1,breakfast_w2,0.2,breakfast_w3)

lunch_1 = Family_type2a_lu.Appliance(Family_type2a_lu,1,1500,1,20,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch_1.windows(lunch,[0,0],0.3)
lunch_1.specific_cycle_1(1100,20,0,0,0.1) 
lunch_1.cycle_behaviour([11*60,13*60],[0,0])

lunch2_1 = Family_type2a_lu.Appliance(Family_type2a_lu,1,1500,1,15,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch2_1.windows(lunch,[0,0],0.3)
lunch2_1.specific_cycle_1(1500,15,0,0,0.1)
lunch2_1.cycle_behaviour([11*60,13*60],[0,0])

dinner_1 = Family_type2a_di.Appliance(Family_type2a_di,1,1500,1,18,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner_1.windows(dinner,[0,0],0.3)
dinner_1.specific_cycle_1(3600,8,1100,10,0.1)
dinner_1.cycle_behaviour([18*60,20*60],[0,0])

dinner2_1 = Family_type2a_di.Appliance(Family_type2a_di,1,1500,1,10,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner2_1.windows(dinner,[0,0],0.3)
dinner2_1.specific_cycle_1(1900,10,0,0,0.1)
dinner2_1.cycle_behaviour([18*60,20*60],[0,0])

#Family type 2b
breakfast_1 = Family_type2b_br.Appliance(Family_type2b_br,1,900,3,24,0.1,3, fixed_cycle=0, thermal_P_var = 0.2)
breakfast_1.windows(breakfast_w1,breakfast_w2,0.2,breakfast_w3)

dinner_1 = Family_type2b_di.Appliance(Family_type2b_di,1,1500,1,20,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner_1.windows(dinner,[0,0],0.3)
dinner_1.specific_cycle_1(1100,20,0,0,0.1) 
dinner_1.cycle_behaviour([18*60,20*60],[0,0])

dinner2_1 = Family_type2b_di.Appliance(Family_type2b_di,1,1500,1,15,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
dinner2_1.windows(dinner,[0,0],0.3)
dinner2_1.specific_cycle_1(1500,15,0,0,0.1)
dinner2_1.cycle_behaviour([18*60,20*60],[0,0])

lunch_1 = Family_type2b_lu.Appliance(Family_type2b_lu,1,1500,1,18,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch_1.windows(lunch,[0,0],0.3)
lunch_1.specific_cycle_1(3600,8,1100,10,0.1)
lunch_1.cycle_behaviour([11*60,13*60],[0,0])

lunch2_1 = Family_type2b_lu.Appliance(Family_type2b_lu,1,1500,1,10,0.2,5, fixed_cycle = 1, thermal_P_var = 0.2)
lunch2_1.windows(lunch,[0,0],0.3)
lunch2_1.specific_cycle_1(1900,10,0,0,0.1)
lunch2_1.cycle_behaviour([11*60,13*60],[0,0])


