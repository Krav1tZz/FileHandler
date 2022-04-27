import re
import smtplib

x = open("BibleHandler.txt", "r")
x2 = x.read()


class handler:
    

    def __init__(self, x: str):
        self.txt = x

    def how_many(self, smbl: str):
        a1 = input((str))
        return len(re.findall(a1, self.txt))
        
    
    def get_number_sum(self):
        x_sum = re.findall("[0-9]+", self.txt)
        for x in range(len(x_sum)):
            x_sum[x] = int(x_sum[x])
        
        return sum(x_sum)
            
    def get_number_occ(self):
        return len(re.findall("[0-9]+", self.txt))






a = handler(x2)
print(a.how_many(a))
print(a.get_number_sum())
print(a.get_number_occ())