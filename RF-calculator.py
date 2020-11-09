from math import log10, pow

"""
This Program has a purpose that makes easier to understand of RF/Microwave Terms given bellow
- RL    Return Loss
- VSWR  Voltage Standing Wave Ratio
- Γ     Reflection Coefficient
- ML    Mismatch Loss
"""

def main_program(selection):
    """ All functions works here"""

    # input:RL | outputs:VSWR Reflection Coefficient(Γ) ML
    if selection == "1":
        print("RL range is [0,100] dB")
        try:
            rl = float(input("Return Loss(dB): "))
        except ValueError as e:
            print("Wrong Input Value. Error: " + str(e))
            main_program("1")
        else:
            if rl == 0:
                print("RL= 0 dB | VSWR= ∞ | Reflection Coefficient(Γ)= 1.0 | ML= ∞")
            elif rl > 0 and rl <= 100:
                vswr = rl_to_vswr(rl)
                gama = rl_to_gama(rl)
                ml = rl_to_ml(rl)
                print("RL= {} dB | VSWR= {:f} | Reflection Coefficient(Γ)= {:f} | ML= {:f} dB".format(
                    rl, vswr, gama, ml))
            else:
                print("Out of Range,please try again.")
                main_program("1")

    # input:VSWR | outputs:RL Reflection Coefficient(Γ) ML
    elif selection == "2":
        print("VSWR range is [1,1000]")
        try:
            vswr = float(input("VSWR: "))
        except ValueError as e:
            print("Wrong Input Value. Error: " + str(e))
            main_program("2")
        else:
            if vswr == 1:
                print("VSWR=1 | RL= ∞ dB | Reflection Coefficient(Γ)= ∞ | ML=0 dB")
            elif vswr > 1 and vswr <= 1000:
                rl = vswr_to_rl(vswr)
                gama = vswr_to_gama(vswr)
                ml = vswr_to_ml(vswr)
                print("VSWR= {:f} | RL= {:f} dB | Reflection Coefficient(Γ)= {:f} | ML= {:f} dB".format(
                    vswr, rl, gama, ml))
            else:
                print("Out of Range,please try again.")
                main_program("2")

    # input:Reflection Coefficient(Γ) | outputs:VSWR RL ML
    elif selection == "3":
        print("Reflection Coefficient(Γ) range is [1,1000]")
        try:
            gama = float(input("Reflection Coefficient(Γ): "))
        except ValueError as e:
            print("Wrong Input Value. Error: " + str(e))
            main_program("2")
        else:
            if gama == 1:
                print("Reflection Coefficient(Γ)= 1 | VSWR= ∞ | RL= 0 dB | ML= ∞")
            elif gama > 1 and gama <= 1000:
                rl = gama_to_rl(gama)
                vswr = gama_to_vswr(gama)
                ml = gama_to_ml(gama)
                print("Reflection Coefficient(Γ)= {:f} |VSWR= {:f} | RL= {:f} dB | ML= {:f} dB".format(
                    gama, vswr, rl, ml))
            else:
                print("Out of Range,please try again.")
                main_program("3")
    elif selection == "e":
        print("Thank you and goodbye.")
        exit()
    else:
        print("You entered wrong input.")


def gama_to_rl(gama):
    """Calculate RL from gama/Reflection Coefficient(Γ) RL"""
    rl = -20 * log10(gama)
    return rl


def gama_to_vswr(gama):
    """Calculate VSWR from gama/Reflection Coefficient(Γ) RL"""
    vswr = (1 + abs(gama))/(1-abs(gama))
    return vswr


def gama_to_ml(gama):
    """Calculate ML from gama/Reflection Coefficient(Γ) RL"""
    ml = -10 * log10(abs(1 - gama**2))
    return ml


def vswr_to_rl(vswr):
    """Calculate RL from VSWR"""
    rl = -20 * log10(((vswr-1)/(vswr+1)))
    return rl


def vswr_to_gama(vswr):
    """Calculate Gama (Reflection Coefficient) from VSWR"""
    gama = (vswr-1)/(vswr+1)
    return gama


def vswr_to_ml(vswr):
    """Calculate ML from VSWR"""
    ml = -10 * log10(1 - pow(((vswr-1)/(vswr+1)), 2))
    return ml


def rl_to_vswr(rl):
    """Calculate VSWR from RL"""
    vswr = (1 + pow(10, -(rl/20)))/(1 - pow(10, -(rl/20)))
    return vswr


def rl_to_gama(rl):
    """Calculate Reflection Coefficient from RL"""
    gama = pow(10, -(rl/20))
    return gama


def rl_to_ml(rl):
    """Calculate ML from RL"""
    ml = -10 * log10(1-(pow(10, -pow((rl/20), 2))))
    return ml


def main_program_info():
    """Show the text for user about stdin"""

    print("""
    This Program has a purpose that makes easier to understand of RF/Microwave Terms given bellow
    
    Choose Mode For Calculation
    - (1) RL    Return Loss 
    - (2) VSWR  Voltage Standing Wave Ratio
    - (3) Γ     Reflection Coefficient
    - For exit enter: e
    """)

#İnfinite Loop is Main Mechanism for working program on terminal. Easy to break it :)
while True:
    main_program_info()
    selection = input()
    main_program(selection)
