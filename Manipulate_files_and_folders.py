# create a file
"""
steps->
	#open a file

	#give name+extension
	#click enter """

import shutil
import os
fo = open("D:\\file.txt", 'w')
fo.write("Hello!!!")

# to write multiple lines
# create a list of item.
line_list = ["How are you? \n", "How is the weather there? \n"]
fo.writelines(line_list)

# update a file
"""
steps->
	To update a file, we use same steps
	but open the file in appned mode. """

fo = open("D:\\file.txt", 'a')
fo.write("Hello all. Welcome to Piyush's github.")

# to update with multiple lines
# create a list of item.
line_list = ["It is really hot in Gujarat.\n", "BTW what about yours\n"]
fo.writelines(line_list)

# use case1
# one file has data for starting 15 days of a month
# other file has data for next 15 days of a month
# you want to update the data in the older file.

# open the first file in append mode
ff = open("D:\\example.txt", 'a')

# open the second file in read mode
sf = open("D:\\file.txt", 'r')
# read data from second file
info = sf.read()
# append the info data in the first file
ff.write(info)
# close both the files
ff.close()
sf.close()

# moving a file
# steps->
# change the location of a file.

# importing useful libray
# new directory formation-> os.mkdir("new_directiry_path")
os.mkdir("D:\\Piyush\\")
shutil.move("D:\\ABC", "D:\\Piyush\\")


# to copy a file or folder
shutil.copy("D:\\4th Semester Result.pdf",
            "D:\\Piyush\\4th Semester Result.pdf")

# to copy multiple files.
# steps
# for every file , copy it.

file_list = ["D:\\4th Semester Result.pdf",
             "D:\\5th Semester Result.pdf", "D:\\6th Semester Result.pdf"]
for file in file_list:
    shutil.copy(file, "D:\\Piyush\\")

# to rename a file
# steps->
    # change the location from old to new

os.rename("D:\\1st Sem_res.jpeg", "D:\\1st Semester Result.jpeg")


# use case 2
# for 2nd Sem_res.jpeg and 3rd Sem_res.jpeg rename it to 2nd Semester Result.jpeg & 3rd Semester Result.jpeg
# we need to make
# Sem_res.jpeg->  Semester Result.jpeg
# that means we need to make
# D:\\2nd Sem_res.jpeg->D:\\2nd Semester Result.jpeg

# creating a list of the files
re_files = ["D:\\2nd Sem_res.jpeg", "D:\\3rd Sem_res.jpeg"]
for i in re_files:
    j = i.split(" ")  # splitting across a space
    # concatenating to get the new path
    new_path = j[0]+' Semester Result.jpeg'
    # print(new_path)
    os.rename(i, new_path)  # renaming


# to delete a file
# steps->
    # make the location available.
os.remove("D:\\Piyush\\ABC")
