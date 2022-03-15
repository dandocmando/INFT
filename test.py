def main():
    in1 = 6
    varOb = ""

    if type(in1) is str:
        varOb = "str"

    elif type(in1) is int:
        varOb = "int"

    elif type(in1) is bool:
        varOb = "bool"

    elif type(in1) is float:
        varOb = "float"

    print("This variable is a "+varOb+" with a value of: "+str(in1))

main()