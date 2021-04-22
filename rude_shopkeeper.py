# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:13:27 2021

@author: Angel
"""
import pandas as pd

player_wallet = 1000

print ('Find what you need and scram. \n')

inventory_data = [['Fish', 5],['Bread', 10],['Wine', 21]]
shopinventory_df = pd.DataFrame(inventory_data,columns=['Item','Cost'])
print (shopinventory_df)

player_input = input("You gonna buy somethin' or what? (y/n): ")

if player_input == 'y':
    purchase_inquiry= input('Enter item name followed by quantity (e.g., "fish 2"): ')
elif player_input == 'n':
    print ("Great, then what're you still doin' here?")
else:
    player_input = input("You gonna buy somethin' or what? (y/n): ")
    
purchase_inquiry = purchase_inquiry.capitalize()
split_string = purchase_inquiry.split()

ask_item = split_string[0]
ask_quantity = int(split_string[1])

if ask_item in shopinventory_df.values:
    print ("\nWe've got that!")

cost_item = shopinventory_df.loc[shopinventory_df['Item'] == ask_item]['Cost'].values[0]
transaction_total = cost_item * ask_quantity

if transaction_total <= player_wallet:
    print ("That'll be ", transaction_total, "krumples.")
    player_wallet = player_wallet - transaction_total
    print ("You currently have ", player_wallet, "in your wallet.")
else:
    print ("You're need more krumples to buy that.")

if ask_item not in shopinventory_df.values:
    print ("\nC'mon, talk straight! Whaddya need?")