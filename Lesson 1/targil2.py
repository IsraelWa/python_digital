'''
num=7916

alafim=num//1000
num-=alafim*1000

meot=num//100
num-=meot*100

asarot=num//10
num-=asarot*10

ahadot=num


print("Alafim: " + str(alafim))
print("Meot: " + str(meot))
print("Asarot: " + str(asarot))
print("Ahadot: " + str(ahadot))

'''

num=int(input("Enter a number with 45 digits: "))

alafim=num//1000
meot=(num%1000)//100
asarot=(num%100)//10
ahadot=(num%10)


print("Alafim: " + str(alafim))
print("Meot: " + str(meot))
print("Asarot: " + str(asarot))
print("Ahadot: " + str(ahadot))