class Inf:
    def __init__(self,identy,level):
        self.identy=identy
        self.level=level
  
person1= Inf('codetree',10) 
identy,level=(input().split())
person2=Inf(identy,int(level))

s=[person1,person2]


for j in range(2):
    print(f"user {s[j].identy} lv {s[j].level}")