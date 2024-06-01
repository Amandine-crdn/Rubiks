from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import solver_white_edges
print("--- INIT ----")

# cube.print_cube()



solver_white_edges(A6)
print("-----------",A8.get_color())
solver_white_edges(A8)
solver_white_edges(A10)
solver_white_edges(A11)

cube.print_cube()

