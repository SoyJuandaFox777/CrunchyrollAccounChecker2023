#!/usr/bin/env python3
"""
𝕮𝖗𝖚𝖓𝖈𝖍𝖞𝖗𝖔𝖑𝖑 𝖈𝖍𝖊𝖈𝖐𝖊𝖗
𝕯𝖊𝖘𝖆𝖗𝖗𝖔𝖑𝖑𝖆𝖉𝖔 𝖇𝖞 = @𝕵𝖉_𝕬𝖓𝖔𝖓𝖞𝖒𝖔
"""

### Importing
# Importing Inbuilt-Packages
import os

# Importing Dev Defined Script
import src.checker

tag = """
𝕮𝖗𝖚𝖓𝖈𝖍𝖞𝖗𝖔𝖑𝖑 𝖈𝖍𝖊𝖈𝖐𝖊𝖗
𝕯𝖊𝖘𝖆𝖗𝖗𝖔𝖑𝖑𝖆𝖉𝖔 𝖇𝖞 = @𝕵𝖉_𝕬𝖓𝖔𝖓𝖞𝖒𝖔
"""

def main():
    print(tag)
    if not os.path.exists('result'):
        os.makedirs('result')
        
    filename = input("Enter the name or path of file: ")
    if os.path.isfile(filename):
        src.checker.CrunchyrollChecker.create(filename)
    else:
        print("File not found.")


### yeaaahhhh!!!!
if __name__ == "__main__":
    main()
