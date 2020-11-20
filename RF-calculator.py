from math import log10, pow

"""
Dev Note: 11.11.2020 - ozyalhan
This Program has a purpose that makes easier to understand of RF/Microwave Terms given bellow

    - RL    Return Loss
    - VSWR  Voltage Standing Wave Ratio
    - Γ     Reflection Coefficient
    - ML    Mismatch Loss

    For example, choose RL mode, enter the value and get results of VSWR, Reflection Coefficient and ML.

Program has also RL calculator that get inputs of Pi(Incident Power) and Pr(reflected power) as Watt or dBm, calculate the return loss value as dB.
"""


def program():
    """All program works under this function"""

    # Infinite Loop is Main Mechanism for working program on terminal. Easy to break it :)
    while True:
        main_program_info()
        selection = input()
        main_program(selection)


def main_program_info():
    """Show the text for user about stdin"""

    print("""
    This Program has a purpose that makes easier to understand of RF/Microwave Terms given bellow

    Choose Mode For Calculation
    - (1) RL    Return Loss
    - (2) VSWR  Voltage Standing Wave Ratio
    - (3) Γ     Reflection Coefficient
    - (4) RL Calculator with Watt Inputs
    - (5) RL Calculator with dBm Inputs
    (For exit enter: e)
    Selection: """)


def main_program(selection):
    """ All functions works here"""

    # input:RL | outputs:VSWR Reflection Coefficient(Γ) ML
    if selection == "1":
        main_rl_function()
        work_again()

    # input:VSWR | outputs:RL Reflection Coefficient(Γ) ML
    elif selection == "2":
        main_vswr_function()
        work_again()

    # input:Reflection Coefficient(Γ) | outputs:VSWR RL ML
    elif selection == "3":
        main_gama_function()
        work_again()

    # RL Calculator with Watt Inputs
    elif selection == "4":
        rl = return_loss_calc_watt()
        main_rl_calc(rl)  # Detail info makes program better
        work_again()
    # RL Calculator with dBm Inputs
    elif selection == "5":
        rl = return_loss_calc_dBm()
        main_rl_calc(rl)  # Detail info makes program better
        work_again()
    elif selection == "e":
        exit_program()
    else:
        print("You entered wrong input.")


def work_again():
    """After the calculation ask user that continue to program"""
    try:
        w_quest = input("Do you want work again?(y/n)").lower()
    except ValueError as e:
        print("Wrong Input Value. Error: " + str(e))
        work_again()
    else:
        if w_quest == "y" or w_quest == "yes" or w_quest == "yeah":
            program()
        elif w_quest == "n" or w_quest == "no" or w_quest == "nope":
            exit_program()
        else:
            print("Wrog input.")
            work_again()


def exit_program():
    """Close the program"""
    print("#######################")
    print("Thank you and goodbye.")
    exit()


def main_rl_function():
    """Calculates all values from RL input"""

    print("RL range is [0,100] dB")

    try:
        rl = float(input("Return Loss(dB): "))
    except ValueError as e:
        print("Wrong Input Value. Error: " + str(e))
        main_program("1")
    else:
        main_rl_calc(rl)


def main_rl_calc(rl):
    """Exact calculation of RL"""

    if rl == "infinite":
        print("RL= ∞ | VSWR= 1 | Reflection Coefficient(Γ)= ∞ | ML= 0 dB")
    elif rl == 0:
        print("RL= 0 dB | VSWR= ∞ | Reflection Coefficient(Γ)= 1.0 | ML= ∞")
    elif int(rl) > 0 and int(rl) <= 100:
        vswr = rl_to_vswr(rl)
        gama = rl_to_gama(rl)
        ml = rl_to_ml(rl)
        print("RL= {} dB | VSWR= {:f} | Reflection Coefficient(Γ)= {:f} | ML= {:f} dB".format(
            rl, vswr, gama, ml))
    else:
        print("Out of Range,please try again.")
        main_program("1")


def main_vswr_function():
    """Calculates all values from VSWR input"""
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


def main_gama_function():
    print("Absolute value of Reflection Coefficient(|Γ|) range is [0,1]")
    try:
        gama = float(input("Reflection Coefficient(Γ): "))
    except ValueError as e:
        print("Wrong Input Value. Error: " + str(e))
        main_program("3")
    else:
        if gama == 1:
            print("Reflection Coefficient(Γ)= 1 | VSWR= ∞ | RL= 0 dB | ML= ∞")
        elif gama == 0:
            print("Reflection Coefficient(Γ)= 0 | VSWR= 1 | RL= ∞ dB | ML= 0 dB")
        elif gama < 1 and gama > 0:
            rl = gama_to_rl(gama)
            vswr = gama_to_vswr(gama)
            ml = gama_to_ml(gama)
            print("Reflection Coefficient(Γ)= {:f} |VSWR= {:f} | RL= {:f} dB | ML= {:f} dB".format(
                gama, vswr, rl, ml))
        else:
            print("Out of Range,please try again.")
            main_program("3")


def return_loss_calc_watt():
    """Calculate the RL from Pi Incident Power and Pr Reflected Power as Watt, Power ranges are between [-1000,1000]"""

    print(
        "Calculate the RL from Pi Incident Power and Pr Reflected Power as Watt, Power ranges are between [-1000,1000]")

    try:
        pi = float(input("Pi:Incident Power(W):"))
        pr = float(input("Pr:Reflected Power(W):"))
    except ValueError as e:
        print("Wrong Input Value. Error: " + str(e))
        return_loss_calc_watt()
    else:
        if (pi >= -1000 and pi <= 1000) and ((pr >= -1000 and pr <= 1000)):
            if(pi == 0):
                print(
                    "Pincident equal zero means, no power input in the system. RL cant calculated in this situation.")
                return_loss = 0
                return return_loss
            elif(pr == 0):
                print(
                    "Preflected equal zero means, no reflection from load. RL is infinite in this situation.")
                return_loss = "infinite"
                return return_loss

            elif(pi >= pr):
                return_loss = 10 * log10(pi/pr)
                print("Return Loss: -" + str(return_loss)+" dB")
                return return_loss
            else:
                print("\n##################################################")
                print("Error: Pi cant be smaller than Pr")
                print("##################################################\n")
                return_loss_calc_watt()

        else:
            print("##################################################")
            print("Wrong input: Power ranges are between [-1000,1000]")
            print("##################################################\n")
            return_loss_calc_watt()


def return_loss_calc_dBm():
    """Calculate the RL from Pi Incident Power and Pr Reflected Power as dBm, Power ranges are between [0,100]"""

    print(
        "Calculate the RL from Pi Incident Power and Pr Reflected Power as dBm, Power ranges are between [0,100]")

    try:
        pi = float(input("Pi:Incident Power(dBm):"))
        pr = float(input("Pr:Reflected Power(dBm):"))
    except ValueError as e:
        print("Wrong Input Value. Error: " + str(e))
        return_loss_calc_dBm()
    else:
        if (pi >= 0 and pi <= 100) and ((pr >= 0 and pr <= 100)):

            if(pi >= pr):
                return_loss = pi - pr
                print("Return Loss: -" + str(return_loss)+" dB")
                return return_loss
            else:
                print("\n##################################################")
                print("Error: Pi cant be smaller than Pr")
                print("##################################################\n")
                return_loss_calc_dBm()

        else:
            print("\n##################################################")
            print("Error: dBm input ranges are between [0,1000]")
            print("##################################################\n")
            return_loss_calc_dBm()


def gama_to_rl(gama):
    """Calculate RL from gama/Reflection Coefficient(Γ) RL"""
    rl = -20 * log10(gama)
    return rl


def gama_to_vswr(gama):
    """Calculate VSWR from gama/Reflection Coefficient(Γ) RL"""
    vswr = abs((1 + abs(gama))/(1-abs(gama)))
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


# start-up
program()
