# Habit program is used for reminders of what my habits are
# It also logs issues I've encountered.
# I also use it to deal with recurring problems.

import time
import datetime
import os.path

# open 'habit_focus' file. Contains habits I want to develop.
focus_file= open("habit_focus","r")
focus_contents = focus_file.read()



# todo: rename variable
# ts is time stamp
ts = time.time()

# st is...? stamp time? Terrible.
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
file_counter = 0
file_path = "."

# generates a name for our log by checking what already exists
# this way if we use the program more than once a day it will
# be numbered in order, but still have a date stamp. 
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

# goes from none -> problems -> habits
section = "none"

# increments by one whenever we increase a newline
# resets when we enter our problems section
counter = 1 

#habits are separated by newlines
#first char being # signals we're done, text after that isn't read and so can be used for comments
#first char being ! signals change of section
for habit in focus_contents.splitlines():
    #empty line counts as being done
    if (len(habit) < 2): 
        continue
    # signals we've hit comments, so we're done
    if (habit[0] == "#"):
        break
    # signals we're changing section
    if (habit[0] == "!"):
        if (section == "problem"):
            section = "habit"
            counter = 0
            print("\nhabits:")
        elif (section == "none"):
            section = "problem"
            print("\nproblems:")
        continue
    # display habit or problem to user
    display = "\n#" + str(counter) + ": " + habit 
    print(display)
    
    # if it is a problem, detail what you're doing about it today
    if (section == "problem"):
        action = input("\n> ")
        display += "\n\n> " + action + "\n\n"
    log_file.write(display)
    counter += 1

log_file.close()
    
print("\nWrite these down, repeatedly check throughout the day.\n")
