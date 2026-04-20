A ={1,2,3}
B ={3,4,5}
union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)

with open("set.txt", "w") as file:
    file.write("Set A: " + str(A) + "\n")
    file.write("Set B: " + str(B) + "\n")
    file.write("Union: " + str(union_set) + "\n")
    file.write("Intersection: " +str(intersection_set) + "\n")
    file.write("Difference(A - B): " +str(difference_set) + "\n")

with open("set.txt", "a") as file:
        file.write("\nLog : operations completed successfully.\n")


with open("set.txt", "r") as file:
        content = file.read()
        print("File content :\n")
        print(content)


    
    