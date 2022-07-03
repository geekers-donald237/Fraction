class Fraction:
    num=1
    den=1
    signe=0
    def __init__(self,numerateur=1,denominateur=1):
        if (denominateur ==0):
            print("ValueError:le dénominateur doit etre different de  0")
        else :
            self.num=int(numerateur)
            self.den=int(denominateur)
            if (numerateur * denominateur < 0) :
                self.signe=-1
            else :
                self.signe=0


    def PGCD(self):
        x,y = self.num, self.den
        while y :
            x,y = y, x%y
        return x


    def simpliFrac(self):
        valeur=self.PGCD()
        self.den//=valeur
        self.num//=valeur

   
    def __str__ (self):
        self.simpliFrac()
        if (self.signe<0) :
            self.den= abs(self.den)
            self.num = abs(self.num)
            self.num=-self.num*-1
        return ("({},{})".format(self.num,self.den))


    def __neg__(self) :
        val= -1*self.num
        return Fraction((val), self.den)

        
    def __add__(self, other) :
        nume = ((self.num * other.den) + (self.den * other.num))
        deno = (self.den*other.den)
        somme= Fraction(nume,deno)
        return somme


    def __sub__(self, other) :
        nume = ((self.num * other.den) - (self.den * other.num))
        deno = (self.den*other.den)
        somme= Fraction(nume,deno)
        return somme


    def __mul__(self, other) :
        nume = ((self.num * other.num))
        deno = (self.den*other.den)
        somme= Fraction(nume,deno)
        return somme


    def __truediv__(self, other) :
        
        nume = ((self.num * other.den))
        deno = (self.den*other.num)
        somme= Fraction(nume,deno)
        return somme


    def __floordiv__(self, other) :
        nume = ((self.num * other.den))
        deno = (self.den*other.num)
        somme= nume//deno
        return somme





if __name__ == '__main__':
    f= Fraction()
    print("Constructeur par defaut : f =", f)
    # print("\n Fraction interdite:") A tester une fois
    #frac = Fraction(2,0)
    g = Fraction(10,30)
    print("\ng =", g)
    print("\nopposée :",g.__neg__())
    print("\ng.num =",g.num)
    print("\ng.den =",g.den)
    h = Fraction(7, -14)
    print("\nh =",h)
    print("\ng + h =",g.__add__(h))
    print("\ng - h =",g.__sub__(h))
    print("\ng * h =",g.__mul__(h))
    print("\ng / h =",g.__truediv__(h))
