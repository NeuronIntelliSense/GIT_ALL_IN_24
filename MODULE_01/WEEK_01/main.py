from ex01_cal_f1_score import exercise1
from ex02_activate_functions import exercise2
from ex03_loss_functions import exercise3
from ex04_functions_approx import approx_sin, approx_cos, approx_cosh, approx_sinh
from ex05_md_nre_single_sample import md_nre_single_sample


if __name__ == "__main__":
    choose = input("Choose the exercise that will be executed (1|2|3|4|5) or 6 for exit: ")
    choose = int(choose)
    exe = False
    if 1 <= choose <= 5:
        exe = True
    
    cont_prompt = "Make another choice: "

    while exe:
        if choose == 1:
            print("---------- Exercise 1 ----------")
            exercise1(tp=2, fp=3, fn=4)

            choose = int(input(cont_prompt))
        elif choose == 2:
            print("---------- Exercise 2 ----------")
            exercise2()

            choose = int(input(cont_prompt))
        elif choose == 3:
            print("---------- Exercise 3 ----------")
            exercise3()

            choose = int(input(cont_prompt))
        elif choose == 4:
            print("---------- Exercise 4 ----------")
            approx_sin(x=3.14, n=10)
            approx_cos(x=3.14, n=10)
            approx_sinh(x=3.14, n=10)
            approx_cosh(x=3.14, n=10)

            choose = int(input(cont_prompt))
        elif choose == 5:
            print("---------- Exercise 5 ----------")
            md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)

            choose = int(input(cont_prompt))
        elif choose == 6:
            exe = False
        else:
            print("The exercise is not existed.")
            choose = int(input("Input again: "))
    
    print("---------- The program is terminated ----------")