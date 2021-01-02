num=int(input("Enter a number with 4 digits: "))
'''
alafim=4
meot=5
asarot=6
ahadot=7
'''
#This is alafim
print("alafim=" + str(num//1000))

#This is meot
print("meot=" + str((num%1000)//100))

#This is asarot
print("asarot=" + str((num%100)//10))

#This is ahadot
print("ahadot=" + str(num%10))


