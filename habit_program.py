
focus_file= open("habit_focus","r")
focus_contents = focus_file.read()
counter = 1

import time
import datetime
import os.path
ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
file_counter = 0
file_path = "."
while (os.path.exists(file_path)):
    file_counter += 1
    file_path = st + "_" + str(file_counter)
    if (file_counter == 1):
       file_path = st
    file_path = "logs/" + file_path

log_file= open(file_path,"w+")
    
print("\n"*50)
#print("The goal is to move all habits into 'integrated' and problems into 'in progress'. 2-3 ideas I can try to make that happen faster.")
print("Deep thought process: address core of the problem. When I conclude, return to beginning with fresh understanding.")

section = "none"
for habit in focus_contents.splitlines():
    if (len(habit) < 2): 
        continue
    if (habit[0] == "#"):
        break
    if (habit[0] == "!"):
        if (section == "problem"):
            section = "habit"
            counter = 0
            print("\nhabits:")
        elif (section == "none"):
            section = "problem"
            print("\nproblems:")
        continue

    display = "\n#" + str(counter) + ": " + habit 

    print(display)
    if (section == "problem"):

        action = input("\n> ")
        display += "\n\n> " + action + "\n\n"
    log_file.write(display)
    counter += 1

log_file.close()
    
print("\nWrite these down, repeatedly check throughout the day.\n")
