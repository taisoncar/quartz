import math
R0 = 5.1e3 #Ohm
C0 = 53.9e-12 #Farad
R = 199 #Ohm
L = 1.20 #Henry
C = 5.2775e-15 #Farad
V0 = 500 #mV
Ws = math.sqrt(1/(L*C))
a = R/L

def input_to_int(text):
    inpt = input(text)
    try:
        inpt = int(inpt)
        return inpt
    except ValueError:
        print("That's not an integer! Try again.")
        return input_to_int(text)

def range_input(text, low, high):
    inpt = input_to_int(text)
    while(inpt < low or inpt > high):
        print("Input value out of range! Try again.")
        inpt = input_to_int(text)
    return int(inpt)
    
#main
'''
with open("demon.csv", "w") as filee:
    filee.write("del_f(Hz)")
    filee.write(",")
    filee.write("V2(mV)")
    filee.write(",")
    filee.write("del_t(ns)")
    filee.write(",")
    filee.write("|Z|(Ohm)")
    filee.write(",")
    filee.write("phi")
    filee.write(",")
    filee.write("phifake")
    filee.write(",")
    filee.write("Zfake")
    filee.write("\n")
'''
print("-------------------------------------------------------------------------------------------------------------------")
while True:
    print("=======")
    print(" INPUT")
    print("=======")
    Cext = range_input("Cext (pF):", 0, 100) * 1e-12
    Wp = math.sqrt((1+C/(C0+Cext))/(L*C))
    f = 2e6 + range_input("Δf (Hz):", -200, 200)
    W = 2*math.pi*f
    Z = (Ws**2 - W**2 + 1j*W*a)/(1j*W*C0*(Wp**2 - W**2 +1j*W*a))
    V2 = V0*(Z/(Z+R0))
    phi = math.atan((V0/V2).imag/(V0/V2).real)
    del_t = phi / W * 1e9 
    print()
    print("========")
    print(" OUTPUT")
    print("========")
    print("U2 (mV):", "{:.1f}".format(abs(V2)))
    print("Δt (ns):", "{:.0f}".format(del_t))
    '''
    print()
    print("========")
    print(" SECRET ")
    print("========")
    print("f_res:", Wp/(2*math.pi)-2e6)
    print("f_anti:",Ws/(2*math.pi)-2e6)
    print("|Z|:", abs(Z))
    print("phi:", phi)
    '''
    print("-------------------------------------------------------------------------------------------------------------------")
    '''
    for i in range(-200,201):
        f = 2e6 + i
        W = 2*math.pi*f
        Z = (Ws**2 - W**2 + 1j*W*a)/(1j*W*C0*(Wp**2 - W**2 +1j*W*a))
        V2 = V0*(Z/(Z+R0))
        phi = math.atan((V0/V2).imag/(V0/V2).real)
        del_t = phi / W * 1e9 
        phifake = 2*math.pi*(i+2e6)*del_t*1e-9
        Zfake = R0/math.sqrt((V0/abs(V2)-math.cos(phifake))**2+math.sin(phifake)**2)
        with open("demon.csv", "a") as filee:
            filee.write("{:.0f}".format(i))
            filee.write(",")
            filee.write("{:.1f}".format(abs(V2)))
            filee.write(",")
            filee.write("{:.0f}".format(del_t))
            filee.write(",")
            filee.write("{:.0f}".format(abs(Z)))
            filee.write(",")
            filee.write("{:.5f}".format(phi))
            filee.write(",")
            filee.write("{:.5f}".format(phifake))
            filee.write(",")
            filee.write("{:.1f}".format(Zfake))
            filee.write("\n")   
    '''    