my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
in_to_cm = 2.54
lb_to_kg = 2.2

print "Let's talk about %s." % my_name
print "He's %d inches or %f centimeters tall." % (my_height, my_height*in_to_cm)
print "He's %d pounds or %f kilograms heavy." % (my_weight, my_weight/lb_to_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
print "Or in MKS/CGS hybrid metric %f." % (my_age + my_height*in_to_cm + my_weight/lb_to_kg)

"""
Extra Credit
Python format characters:
d Signed integer decimal.
i Signed integer decimal.
o Unsigned octal.
u Unsigned decimal.
x Unsigned hexadecimal (lowercase).
X Unsigned hexadecimal (uppercase).
e Floating point exponential format (lowercase).
E Floating point exponential format (uppercase).
f Floating point decimal format.
F Floating point decimal format.
g Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise.
G Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise.
c Single character (accepts integer or single character string).
r String (converts any python object using repr()).
s String (converts any python object using str()).
% No argument is converted, results in a "%" character in the result.

Added variables to convert inches to centimeters and pounds to kilos
"""