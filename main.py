#!/usr/bin/env python3 
 """ 
  ▁ ▂ ▄ ▅ ▆ ▇ █ נＤ_ａŇ𝓞𝕟ч𝔪ᗝ █ ▇ ▆ ▅ ▄ ▂ ▁ 
 """ 
  
### Importing 
 # Importing Inbuilt-Packages 
 import os 
  
 # Importing Dev Defined Script 
 import src.checker 
  
 tag = """ 
____                       _                     _ _
             / ___|_ __ _   _ _ __   ___| |__  _   _ _ __ ___ | | |
            | |   | '__| | | | '_ \ / __| '_ \| | | | '__/ _ \| | |
            | |___| |  | |_| | | | | (__| | | | |_| | | | (_) | | |
             \____|_|   \__,_|_| |_|\___|_| |_|\__, |_|  \___/|_|_|
                                               |___/
                       ____ _               _
                      / ___| |__   ___  ___| | _____ _ __
                     | |   | '_ \ / _ \/ __| |/ / _ \ '__|
                     | |___| | | |  __/ (__|   <  __/ |
                      \____|_| |_|\___|\___|_|\_\___|_|  
                          𝕯𝖊𝖘𝖆𝖗𝖗𝖔𝖑𝖑𝖆𝖉𝖔𝖗 = 𝕵𝕯_𝕬𝕹𝕺𝕹𝖄𝕸𝕺                          
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
