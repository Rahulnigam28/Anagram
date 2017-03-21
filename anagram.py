#~/usr/bin/python

# function to input strings and check if they are anagram
def is_anagram (s1, s2):
        if s1 == s2:
                return False
        elif len(s1) == len(s2):
                 x = list(s1)
                 y = list(s2)
                 for i in range(0 , len (x)):
                        for j in range (0 , len (y)):
                                if x[i] == y[j]:
                                        del y[j]
                                        break

                 if len(y) == 0:
                        return True
                 else:
                        return False

        else:
                return False
t = int(input("Enter number of files to read\n"))
filename = []
r = []

for files in range(0, t):
# function to read file and put the words in list
        filename.append(raw_input("Enter name of the file:\r\t\t\t"))
        r.append( open(filename[files] ,"r").read().split())

# main function
for files in range(0 , t):
        x = r[files]
        anagram = {}
        for i in range(0, len(x)):
            for j in range(1, len (x)):
                        if x[i] != "" or x[j] != "":
                                result =  is_anagram(x[i],x[j])
                                if result == True:
                                   del x[j]
                                   x.insert(j,"")
                                   val = len(x[i])
                                   key =  x[i]
                                   anagram[key] = val






        print("\n \t\t\t %s" %filename[files])
        print("Total Number of Words    : %d "  %len(x))
        print ("Numer of Unique Anagrams : %d " %len(anagram))
        print("Length of the Longest Anagram: %s \n" %max(anagram.values()))

~                                                                                                                                                                                                            
                                                                                                                                                                                           1,1           All
