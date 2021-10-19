#!/usr/bin/env python
# coding: utf-8

# # Lista 1


class Frac():
    """
    n - licznik
    d - mianownik
    c - całe częsci
    Klasa tworzy ułamki, daje możliwość porównywania z typem int.
    także da się porównać ułamki pomiędzy sobą
    Ułamki można dodawać odejmować dzielić oraz mnożyć
    """
    def __init__(self,n, d):
        self.n = n
        self.d = d
        if not d != 0: raise ZeroDivisionError
        if type(n) != int: raise ValueError
        if type(d) != int: raise ValueError
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
        greatest = gcd(abs(self.n), abs(self.d))
        self.n = (int(self.n/greatest))
        self.d = int(self.d/greatest)
    
    
    def get_num(self):
        """
        Metoda zwracajaca licznik ulamku
        """
        return self.n
    
    def get_den(self):
        """
        Metoda zwracajaca mianownik ulamku
        """
        return self.d
    

    def __neg__(self):
        """
        Metoda umozliwiajaca na negowanie ulamku 
        po stworzeniu obiektu
        """
        return Frac(-self.n , self.d)

        
    def __str__(self):
        """
        Metoda pozwalajaca na reprezencje ulamku w postaci napisu
        """
        return str(self.n) + "/" + str(self.d)
    
    
    def __eq__(self, x):
        """
        Metoda pozwalajaca na sprawdzenie rownosci (==) ulamkow
        @x - ulamek z ktorym porownujemy
        Zwraca True albo False
        """
        x = check_int(x)
        a = self.__str__()
        b = x.__str__()
        return a == b
        
    def __ne__(self, x):
        """
        Metoda pozwalajaca na sprawdzenie nierownosci (!=) ulamkow
        @x - ulamek z ktorym porownujemy
        Zwraca True albo False
        """
        y = self
        x = check_int(x)
        return not y.__eq__(x)
    
    def __lt__(self, x):
        """
        Metoda pozwalajaca na sprawdzenie mneijszosci (<) ulamkow
        @x - ulamek z ktorym porownujemy
        Zwraca True albo False
        """
        y = self
        x = check_int(x)
        return y.get_num() * x.get_den() < y.get_den() * x.get_num()
    
    def __le__(self, x):
        """
        Metoda pozwalajaca na sprawdzenie mneijszosci i rownosci (<=) ulamkow
        @x - ulamek z ktorym porownujemy
        Zwraca True albo False
        """
        y = self
        x = check_int(x)
        return not y.__gt__(x)
    
    def __gt__(self, x):
        """
        Metoda pozwalajaca na sprawdzenie wieksosci i rownosci (>=) ulamkow
        @x - ulamek z ktorym porownujemy
        Zwraca True albo False
        """
        y = self
        x = check_int(x)
        return y.get_num() * x.get_den() > y.get_den() * x.get_num()
    
    def __ge__(self, x):
        """
        Metoda pozwalajaca na sprawdzenie wiekszosci (>) ulamkow
        @x - ulamek z ktorym porownujemy
        Zwraca True albo False
        """
        y = self
        x = check_int(x)
        return not y.__lt__(x)
    
    def __add__(self, x):
        """
        Metoda pozwalajaca na dodawanie ulamkow
        @x - ulamek do dodania
        Zwraca obiekt klasy Frac
        """
        y = self
        x = check_int(x)
        n = y.get_num() * x.get_den() + x.get_num() * y.get_den()
        d = y.get_den() * x.get_den()
        return Frac(n, d) #Tworzymy obiekt naszej klasy z nowymi danymi
    
    def __sub__(self, x):
        """
        Metoda pozwalajaca na dodawanie ulamkow
        @x - ulamek do odejmowanie
        Zwraca obiekt klasy Frac
        """
        y = self
        x = check_int(x)
        n = y.get_num() * x.get_den() - x.get_num() * y.get_den()
        d = y.get_den() * x.get_den()
        return Frac(n, d)
    
    def __mul__(self, x):
        """
        Metoda pozwalajaca na mnozenie ulamkow
        @x - ulamek do dodania
        Zwraca obiekt klasy Frac
        """
        y = self
        x = check_int(x)
        n = y.get_num() * x.get_num() 
        d = y.get_den() * x.get_den()
        return Frac(n, d)
    
    def __rmul__(self, x):
        """
        Metoda pozwalajaca na mnozenie ulamkow przez int z prawej strony
        @x - ulamek do dodania
        Zwraca obiekt klasy Frac
        """
        y = self
        x = check_int(x)
        n = y.get_num() * x.get_num() 
        d = y.get_den() * x.get_den()
        return Frac(n, d)
    
    def __truediv__(self, x):
        """
        Metoda pozwalajaca na dzielenie ulamkow
        @x - ulamek do dodania
        Zwraca obiekt klasy Frac
        """
        y = self
        x = check_int(x)
        n = y.get_num() * x.get_den()
        d = y.get_den() * x.get_num()
        return Frac(n, d)
        
def check_int(x):
    """
    Funkcja spradzajaca czy argument jest liczba typu int
    Jesli jest to przeksztalca ta liczbe w obiekt klasy Frac
    Umozliwia to mnozenie oraz porownywanie ulamkow z liczbami typu int
    """
    if isinstance(x, int):
        x = Frac(x, 1)  
    return x

def gcd(a, b):
    """
    Znajduje najwiekszy wspolny dzielnik 2 liczb
    Umozliwia to skracanie ulamkow
    """
    if b > 0:
        return gcd(b, a%b)
    return a


