
def collatz_eval(int eval_num):
    cdef int step_number = 0
    while eval_num != 1:
        if eval_num % 2 == 0:
            eval_num /= 2
        else:
            eval_num *= 3
            eval_num +=1
        print("The Number is now " + str(eval_num))
        step_number += 1
    return step_number;
