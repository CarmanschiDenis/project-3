#array = [2,"Info"True,"General Culture"]

#array.append(3.14) pentru a adauga in lista
#array.sort()#merge doar daca tipurile de date sunt la fel

#print(array)

#int_array = [2,4,9]
#float_array = [3.4,4.9,8.6]
#str_array = ["English","Math"]
#ool_array = [True,False,False,True]

#int_array.sort(reverse=True)#pentru a inversa lista
#print(int_array)
#Print(float_array)
#print(str_array)
#print(bool_array)

#array = []
#array_lenght = int(input("Enter list Lenght\n"))
#for i in range(0, array_lenght):
#    element = int(input("Enter Element\n"))
 #   array.append(element)
#else:
   # print(list)
   # list.sort()
   # print(list)
 #   print(list.sort(reverse=True))
 #   print(list)

#list = ["12", "56", "2465", "547", "245", "876"]
#print(list[3])
#if "56" in list:
 #   print(True)
#else:
 #   print(False)
# print (list)  #print list

 #for i in range(0, len(list)):
  #   print(list[i]) #print list by index

# for e in list:
 #       print(e)    #print element


#tuple = ("A", "B", "C", "D")
#print(tuple + ("E", "Finish"))


#int_array = [1, 2, 3, 4, 5, 6, 6, 3]
#int_array = set(int_array)
#set_array = {1, 1, 2, 3, 3, 4, 5, 6, 6, 7}
#print(set_array)
#print(int_array)

dex = {"Cod":"Python", "Extend" : ".py", "Less":"3"}
print(dex.get("Cod")) #use key to display value with the key
dex.update({"Less":3})#update the value where key is less

print(dex)#print dex
for i in dex:
    print(i)#display key
    print(dex.get(i))#displey value with key (i)
#diferenta array tuple