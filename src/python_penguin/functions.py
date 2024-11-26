def p_value_to_words (p_value):
    p_value_rounded = str(round(p_value,3))

    if p_value >= 0.05:
        print("We cannot reject the null hypothesis. " + p_value_rounded)
    elif p_value < 0.001:
        print("*** The p-value is smaller than the critical threshold, p-value is: " + p_value_rounded)
    elif p_value < 0.05:
        print("* The p-value is smaller than the critical threshold, p-value is: "+p_value_rounded)
    else:
        print("Your p-value defies maths. ")

p_value_to_words(0.5)
