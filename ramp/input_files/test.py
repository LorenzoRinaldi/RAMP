# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''


from ramp.core.core import User
User_list = []

'''
This example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a 
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles. 
For examples related to "thermal loads", see the "input_file_2".
'''

#Create new user classes
Casa_Golinucci = User("Casa_Golinucci",1)
User_list.append(Casa_Golinucci)

#Create new appliances

#Church
Lampadine_a_LED = Casa_Golinucci.Appliance(user = Casa_Golinucci,
                                           n = 20,
                                           P = 10,
                                           w = 2,
                                           t = 100,
                                           r_t = 0.2,
                                           c = 60,
                                           fixed = 'no',
                                           flat = 'yes')
Lampadine_a_LED.windows(w1 = [360,480],
                        w2 = [1000,1300],
                        r_w = 0.2)