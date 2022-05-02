import functools
import math

def count(filename, num):
    l = open(filename, 'r').read().splitlines()
    house_list = []
    for line in l:
        fields=line.split(" ")
        house_list.append([int(fields[0]), int(fields[1])])

#print(len(house_list))

    x= 0  #so that we can call  an x coord of a pair instead of 0
    y = 1 # supposed to be more readable

    size_list = [0]*len(house_list)

#print(len(size_list))

    neighbors = list(map(lambda house1 : filter(lambda house2 : math.sqrt(((house1[x] - house2[x])**2 + (house1[y] - house2[y])**2))<=25, house_list), house_list))
    neighbors = list(map(list, neighbors))
    size_list = list(map(len, neighbors))
#print(size_list)

#Find the average size of the neighborhoods of each point
#print("Average size: ", sum(size_list)/len(size_list))
#Find the size of the largest neighborhood
#print("Maximum size: ", max(size_list))
#Find the top 10 points with the largest neighborhoods
#print("Top 10 points: ", biggest_list)

    file1 = open("summary_"+num+".txt", "w")
    file1.write("Average size: " + str(sum(size_list)/len(size_list)))
    file1.write("\nMaximum size: " + str(max(size_list)))
    biggest_list = []
    for i in range(0, 10):
        ind = size_list.index(max(size_list))
        biggest_list.append(house_list[ind])
        size_list[ind] = 0
    file1.write("\nTop 10 points: " + str(biggest_list))
    file1.close()

count("numbers1.txt", "1")
count("numbers2.txt", "2")


