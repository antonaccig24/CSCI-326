from copy import copy
import functools
import math

def count2(filename, num):
    l = open(filename, 'r').read().splitlines()
    house_list = []
    for line in l:
        fields=line.split(" ")
        house_list.append([int(fields[0]), int(fields[1])])

    x= 0  #so that we can call  an x coord of a pair instead of 0
    y = 1 # supposed to be more readable

    size_list = [0]*len(house_list)

    neighbors = list(map(lambda house1 : filter(lambda house2 : math.sqrt(((house1[x] - house2[x])**2 + (house1[y] - house2[y])**2))<=25, house_list), house_list))
    neighbors = list(map(list, neighbors))
    size_list = list(map(len, neighbors))

    biggest_list = []
    for i in range(0, 10):
        ind = size_list.index(max(size_list))
        biggest_list.append(house_list[ind])
        size_list[ind] = 0

    cover_list = []
    new_list = copy(house_list)
    count = 0
    for neighborhood in neighbors:
        isInCover = False
        for house in neighborhood:
            if isInCover == True:
                if house in house_list:
                    house_list.remove(house)
            if house in house_list:
                isInCover = True
                house_list.remove(house)
                cover_list.append(new_list[count])
        count += 1

    #print(cover_list)
    #print(len(cover_list))

    file1 = open("cover_"+num+".txt", "w")
    for i in cover_list:
        file1.write(str(i) + "\n")
    file1.close()
    
count2("numbers1.txt", "1")
count2("numbers2.txt", "2")
