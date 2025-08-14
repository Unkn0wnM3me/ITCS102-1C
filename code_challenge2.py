deposit = eval(input("Enter amount to deposit: "))


ot = deposit // 1000
deposit %=1000 

fh = deposit // 500
deposit %=500

th = deposit // 200
deposit %=200

oh = deposit // 100
deposit %=100

fy = deposit // 50
deposit %=50

ty = deposit // 20
deposit %=20

tn = deposit // 10
deposit %=10

fe = deposit // 5
deposit %=5

oe = deposit


print(ot, "- 1000 pesos")
print(fh, "- 500 pesos")
print(th, "- 200 pesos")
print(oh, "- 100 pesos")
print(fy, "- 50 pesos")
print(ty, "- 20 pesos")
print(tn, "- 10 pesos")
print(fe, "- 5 pesos")
print(oe, "- 1 peso(s)")
