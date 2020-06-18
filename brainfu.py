#!/usr/bin/python
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-f",help="Interpret a brainfuck file")
args = parser.parse_args()

open_file = args.f


def get_symbols(file_name):

    with open(file_name , 'r') as file:

        return [char for char in file.read() if char != '\n']


def interpret(code):
    i=0
    memory = [0]
    pointer_location = 0
    string = ""

    while i < len(code):
        if(code[i]=='<'):
            if pointer_location > 0:
                pointer_location-= 1
        elif(code[i]=='>'):
            pointer_location +=1
            if(len(memory)<=pointer_location):
                memory.append(0)
        elif(code[i]=='+'):
            memory[pointer_location] += 1
        elif(code[i]=='-'):
            if(memory[pointer_location] > 0):
                memory[pointer_location] -= 1
        elif(code[i]=='.'):
           string = string +chr(memory[pointer_location])
        elif(code[i]==','):
            inp = int(input("Input :"))
            memory[pointer_location]= inp

        elif(code[i]=='['):
            if(memory[pointer_location]==0):

                open_bracket = 1
                while open_bracket > 0:
                    i+=1
                    if(code[i]==']'):
                        open_bracket -=1
                    elif(code[i]=='['):
                        open_bracket +=1
        elif(code[i]==']'):
            closed_bracket =1
            while closed_bracket > 0:
                i-=1
                if code[i] == '[':
                    closed_bracket-=1
                elif code[i] == ']':
                    closed_bracket+=1
            i-=1
                    
        i+=1
    print(string)


symbols = get_symbols(open_file)
interpret(symbols)



                
