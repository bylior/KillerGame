#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:08:25 2019

Jeu du killer

@author: naylor
"""


import os
import numpy as np
import random2
from utils.action import Action
from utils.playerNames import playerNames

#clear = lambda: os.system('clear') #on Linux System

#test pour versioning git

#insertion commentaire pour realisation switch windows


class Game(object):
    
    def __init__(self):
        self.playersNames = playerNames
        self.actions = Action
        self.list_namesInOrder = self.randomize_player()
#        self.Dict_action_name = self.choose_action()
        self.Dict_action_name = self.choose_action_w_cards()
        
        
    def randomize_player(self):
        list_names = self.playersNames[:]
        random2.shuffle(list_names)
        return list_names
    

    def choose_action(self):
        Dict_action_name = {}
        ListNumAction = list(self.actions.keys())
        for i in range(len(self.list_namesInOrder)):
            rand_num = np.random.randint(len(ListNumAction))
            numAction = ListNumAction[rand_num]
            try:
                Dict_action_name[self.list_namesInOrder[i]] = [self.list_namesInOrder[i+1],self.actions[numAction]]
            except IndexError:
                Dict_action_name[self.list_namesInOrder[i]] = [self.list_namesInOrder[0],self.actions[numAction]]
                
            del ListNumAction[rand_num]
        
        return Dict_action_name
    
    
    def choose_action_w_cards(self):
        Dict_action_name = {}
        ListNumAction = list(range(10))
        for i in range(len(self.list_namesInOrder)):
            rand_num = np.random.randint(len(ListNumAction))
            numAction = ListNumAction[rand_num]
            try:
                Dict_action_name[self.list_namesInOrder[i]] = [self.list_namesInOrder[i+1],"Tu as l'action numéro {}".format(numAction+1)]
            except IndexError:
                Dict_action_name[self.list_namesInOrder[i]] = [self.list_namesInOrder[0],"Tu as l'action numéro {}".format(numAction+1)]
                
            del ListNumAction[rand_num]
        
        return Dict_action_name
    
    
    def display_action(self,name):
        try:
            print('')
            print('Tu es le joueur {}'.format(name))
            input("Press enter to continue ")
            print('Ta cible est :   {}'.format(self.Dict_action_name[name][0]))
            print('Ton action est :   {}'.format(self.Dict_action_name[name][1]))
        except KeyError:
            print("Ton nom n'est pas dans la liste. Les noms acceptées sont : {}".format(self.playersNames))
            
    def quit_game(self):
        with open('savefile.txt','a') as file:
            file.write('\n\n       New Game      \n\n')
            for name in self.list_namesInOrder:
                file.write(name + ' : ')
                file.write('Victime : ' + self.Dict_action_name[name][0] + ' et ' + self.Dict_action_name[name][1])
                file.write('\n')
    
    
if __name__=='__main__':
    Game = Game()
    string = ''
    while string.lower() != 'quit':
        string = input("What is your name? ")
        if string.lower()  == 'quit':
            print('You are existing the game. See you soon for more murders !')
            input("Press enter to continue ")
            Game.quit_game()
            continue
        Game.display_action(string)
        input("Press enter to continue ")
        #clear()
        os.system('cls')
