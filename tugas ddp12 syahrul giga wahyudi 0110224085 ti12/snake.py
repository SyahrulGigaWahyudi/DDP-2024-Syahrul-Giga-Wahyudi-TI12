from animal import *

class Snake(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,berbisa,habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.berbisa=berbisa
        self.habitat=habitat
    def info_snake(self):
        super().info_animal()
        print("beracun\t\t\t: ",self.berbisa,"\nHabitat\t\t\t: ",self.habitat)

print("====================================================================")
snake=Snake("ular piton","daging","darat","bertelur","ya sangat bahaya bisa bikin hilang nyawa","hutan")
snake.info_snake()
    
