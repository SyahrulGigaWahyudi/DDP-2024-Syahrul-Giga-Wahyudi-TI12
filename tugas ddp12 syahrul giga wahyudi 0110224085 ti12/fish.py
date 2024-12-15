from animal import *

class Fish(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,bernapas,habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernapas=bernapas
        self.habitat=habitat
    def info_fish(self):
        super().info_animal()
        print("Bernapas\t\t: ",self.bernapas,"\nhabitat\t\t\t: ",self.habitat)

print("====================================================================")
fish=Fish("hiuu","daging","laut","melahirkan","ingsan","air asin")
fish.info_fish()
    
