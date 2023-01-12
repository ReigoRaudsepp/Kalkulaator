# Reigo Raudsepp

class Calculator: # klass calculator tegemine
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def liitmine (self):
        return self.num1 + self.num2
    def lahutamine (self):
        return self.num1 - self.num2
    def korrutamine (self):
        return self.num1 * self.num2
    def jagamine (self):
        return self.num1/self.num2
    def ruutjuur(self):
        return self.num1 ** self.num2
    def jaak(self):
        return self.num1 % self.num2

print ("*******Valige toiming:*********\n"\
           " 1. Liitmine\n "\
           " 2. Lahutamine\n"\
           " 3. Korrutamine\n"\
           " 4. Jagamine\n"\
           " 5. Ruutjuur\n"\
           " 6. Jääk\n"\
)


select = int(input("***Vali toiming******\n")) # sisestad oma valiku

num1 = float(input("Sisesta esimene number:\n")) # küsib esimest numbrit
num2 = float (input("Sisesta teine number:\n")) # küsib teist numbrit
my_Result = Calculator(num1,num2)

if select == 1: # liitmise tehe
       print (num1, "+", num2, "=",my_Result.liitmine())
elif (select == 2): # lahutamise tehe
    print (num1, "-", num2, "=",my_Result.lahutamine())
elif (select == 3): # korrutamise tehe
    print (num1, "*", num2, "=",my_Result.korrutamine())
elif(select ==4): # jagamise tehe
    print (num1, "/", num2, "=",my_Result.jagamine())
elif (select == 5): # ruutjuure leidmise tehe
    print (num1, "^", num2, "=",my_Result.ruutjuur())
elif (select == 6): # jäägi leidmise tehe
    print(num1, "%", num2, "=",my_Result.jaak())
else: # kui ei sobi prindib kehtetu
  print ("Kehtetu")
