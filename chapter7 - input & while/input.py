'''
Author: LotusFoundAnotherWorld
Date: 2023-07-17 23:01:08
LastEditors: LotusFoundAnotherWorld
LastEditTime: 2023-07-18 21:11:26
Description: 
'''
car_name = input('what car do you want?')
print(f"let me see if i can find you a {car_name}.")

person_count = int(input("how many people？"))
if(person_count > 8):
    print('no enough seats')
else: 
    print('enough seats') 
    