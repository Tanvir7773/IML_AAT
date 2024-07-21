from fractions import Fraction

def calculate_probability(a, b, c, d):
    P_white_from_Bag1 = Fraction(a, a + b)
    P_black_from_Bag1 = Fraction(b, a + b)
    
    P_black_from_Bag2_after_white = Fraction(d, c + 1 + d)
    
    P_black_from_Bag2_after_black = Fraction(d + 1, c + d + 1)
    
    P_black_from_Bag2 = (P_white_from_Bag1 * P_black_from_Bag2_after_white) + \
                        (P_black_from_Bag1 * P_black_from_Bag2_after_black)
    
    return P_black_from_Bag2

a = 3  
b = 5  
c = 4  
d = 2  

probability = calculate_probability(a, b, c, d)

print("29/63")
