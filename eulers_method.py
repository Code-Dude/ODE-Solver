# Performs Eulers Method for approximating Ordinary Differential Equations

# This is the definition of Eulers equation
eulers_equation = lambda x, y, h, equa: y + h*equa(x,y)

# Parameters:
#   h         - the step amount (delta x)
#   num_iters - the number of iterations you wish to run (integer value)
#   init      - an indexable list containing the initial condition of the ODE
#   ode       - a function representing the ODE
def eulers_method(h, num_iters, init, ode):
    y_subn = 0

    for n in range(num_iters):
        if(n == 0):
            y_subn = eulers_equation(init[0], init[1], h, ode)
            print("y1 = " + str(y_subn))
        else:
            y_subn = eulers_equation(init[0] + n*h, y_subn, h, ode)
            print("y" + str(n + 1) + " = " + str(y_subn))

# Step amount
dx = 0.0001
# Num iterations
i = 10000
# Initial Condition [x,y]
i_state = [0,1]
# Change this ODE to whatever you like...
ode = lambda x, y: y

eulers_method(dx, i, i_state, ode)
