import math
def equation_from_2_points(x1,y1,x2,y2):
    #determine the slope
    rise = y2-y1
    run = x2-x1
    slope_m = rise/run
    #determining the y-intercept
    y_intercept = y1-(x1*slope_m)
    intercept_form = f"y=({rise}/{run})x+{int(y_intercept)}"
    print(f"""rise: {rise}
run: {run}
slope_decimal: {slope_m}
y_intercept: {y_intercept}
equation = {intercept_form}
""")
equation_from_2_points(
    int(input("X1: ")),
    int(input("Y1: ")),
    int(input("X2: ")),
    int(input("Y2: "))
)