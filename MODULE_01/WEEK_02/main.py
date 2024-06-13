from ex01_sliding_window import sliding_window
from ex02_counting_dict import count_chars
from ex03_file_word_count import word_count
from ex04_levenshtein_distance import levenshtein_distance

if __name__ == "__main__":
    choose = input("Choose the exercise that will be executed (1|2|3|4) or 5 for exit: ")
    choose = int(choose)
    exe = True
    begin = True
    
    cont_prompt = "Make another choice: "
    test_prompt = "Testing..."
    while exe or begin:
        if choose == 1:
            print("---------- Exercise 1 ----------")
            num_list = [3, 4, 5, 1,-44 , 5 ,10, 12 ,33, 1]
            k = 3

            print(test_prompt)
            print(f"num_list = {num_list}; k = {k}")
            print(f"Output: {sliding_window(num_list=num_list, k=k)}")

            begin = False
            choose = int(input(cont_prompt))
        elif choose == 2:
            print("---------- Exercise 2 ----------")
            testcase = ["Happiness", "smiles"]

            print(test_prompt)
            for word in testcase:
                print(f"Word: {word}")
                print(f"Output: {count_chars(word)}")
            
            begin = False
            choose = int(input(cont_prompt))
        elif choose == 3:
            print("---------- Exercise 3 ----------")
            file_path = "P1_data.txt"

            print(test_prompt)
            print(f"File path: {file_path}")
            print(f"Output: {word_count(file_path=file_path)}")

            begin = False
            choose = int(input(cont_prompt))
        elif choose == 4:
            print("---------- Exercise 4 ----------")
            test_cases = [['kitten', 'sitting'],
                          ['yu', 'you']]
            
            print(test_prompt)
            for pair in test_cases:
                print(f"Source word: {pair[0]} - Target word: {pair[1]}")
                print(f"Output: {levenshtein_distance(src_word=pair[0],
                                                      tar_word=pair[1])}")

            begin = False
            choose = int(input(cont_prompt))
        elif choose == 5:
            begin = False
            exe = False
        else:
            begin = False
            print("The exercise is not existed.")
            choose = int(input("Input again: "))
    
    print("---------- The program is terminated ----------")










