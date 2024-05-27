from SortColors import  milieux#, aretes, coins
aretes = ["WR", "WB", "WG", "WO", "BR", "BO", "BY", "OG", "OY", "GR", "GY","RY"]
coins = ["WBR", "WRG", "WOB","WGO" , "BYR", "GRY", "BYO", "GYO"]

class Cube():
    def __init__(self) -> None:        
        self.coins = coins # coins_list = C1, C2, C3, C4, C5, C6, C7, C8
        self.aretes = aretes # aretes_list = A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12
        self.milieux = milieux # milieu_list = M1, M2, M3, M4, M5
        self.right_aretes = [2, 7, 9, 10]
        self.left_aretes = [1, 4, 5, 6]
        self.right_coins = [1, 3, 5, 7]
        self.left_coins = [0, 2, 4, 6]

    def get_coins(self):
        return self.coins
    
    def get_right_coins(self):
        return self.right_coins

    def get_left_coins(self):
        return self.left_coins
    
    def get_right_aretes(self):
        return self.right_aretes
    
    def get_left_aretes(self):
        return self.left_aretes
    
    def get_color_coin(self, num_coin):
        # print(self.coins[num_coin])
        return self.coins[num_coin]
    
    def set_color_coin(self, num_coin, color):
        self.coins[num_coin] = color

    def get_aretes(self):
        return self.aretes
    
    def get_color_arete(self, num_arete):
        # print(self.aretes[num_arete])
        return self.aretes[num_arete]
    
    def set_color_arete(self, num_arete, color):
        self.aretes[num_arete] = color
    

    def print_cube(self):
        print(f"""

        {self.coins[4][2]} {self.aretes[11][0]} {self.coins[5][1]} 
        {self.aretes[4][1]} {self.milieux[4]} {self.aretes[9][1]}  
        {self.coins[0][2]} {self.aretes[0][1]} {self.coins[1][1]}

{self.coins[4][0]} {self.aretes[4][0]} {self.coins[0][1]}   {self.coins[0][0]} {self.aretes[0][0]} {self.coins[1][0]}   {self.coins[1][2]} {self.aretes[9][0]} {self.coins[5][0]}   {self.coins[5][2]} {self.aretes[11][1]} {self.coins[4][1]}
{self.aretes[6][0]} {self.milieux[1]} {self.aretes[1][1]}   {self.aretes[1][0]} {self.milieux[0]} {self.aretes[2][0]}   {self.aretes[2][1]} {self.milieux[3]} {self.aretes[10][0]}   {self.aretes[10][1]} {self.milieux[5]} {self.aretes[6][1]} 
{self.coins[6][0]} {self.aretes[5][0]} {self.coins[2][2]}   {self.coins[2][0]} {self.aretes[3][0]} {self.coins[3][0]}   {self.coins[3][1]} {self.aretes[7][1]} {self.coins[7][0]}   {self.coins[7][1]} {self.aretes[8][1]} {self.coins[6][1]} 

        {self.coins[2][1]} {self.aretes[3][1]} {self.coins[3][2]}
        {self.aretes[5][1]} {self.milieux[2]} {self.aretes[7][0]} 
        {self.coins[6][2]} {self.aretes[8][0]} {self.coins[7][2]}

""")
