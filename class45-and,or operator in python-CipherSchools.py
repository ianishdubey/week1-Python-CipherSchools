# check two conditions at same time
# and,or operators
name = 'abc'
age = 18
#'and' operator
# in 'and' operator both the conditions need to be true
if name=='abc' and age==18:
    print("condition True")
else:
    print("condition Flase")

if name=='abcd' and age==18:
    print("condition True")
else:
    print("condition Flase")

#'or operator 
# in 'or' operator only one condition need to be true
if name=='abcd' or age==18:
    print("condition True")
else:
    print("condition Flase")

if name=='abc' or age==45:
    print("condition True")
else:
    print("condition Flase")
