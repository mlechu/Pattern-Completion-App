import numpy as np
from predictionAlgorithms import *
from patternProcessing import *

def check_1d(inp):
    for x in range(len(inp) - 1):
        if len(inp[x]) >= 2 and len(inp[x + 1]) >= 2:
            return False
    return True
            



# Python program to take in a pattern
# and return a prediction of the next n elements
if __name__ == '__main__':
    # lr_mat = lin_reg_mat_builder(np.array([["1Aa", "2Aa"], ["3Bb", "4Bb"]]))
    # inp = get_user_input()
    inp = np.array([["a2-A", "b3-B"], ["d5-D", "e6-E"]], dtype=object)
    
    if (check_1d(inp)):
        print(generate_predictions_1d(generate_1d_str(np.hstack(inp)), 5))
    else:
        lr_mat = lin_reg_mat_builder(np.array(inp))
        print(predict_at_pos(lr_mat, 2, 0))

