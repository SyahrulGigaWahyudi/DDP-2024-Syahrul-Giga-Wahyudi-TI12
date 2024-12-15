from animal import*

class Bird(animal):
        #kosntruktor properti
    def __init__(self, name, makanan, hidup, berkembang_biak,warna,paruh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        #method info
    def info_bird (self):
        super().info_animal()
        print("warna\t\t\t: ",self.warna,"\nparuh\t\t\t:",self.paruh)
    
print("====================================================================")
bird=Bird("elang","daging","di tebing","bertelur","coklat","bengkok dan lancip")

bird.info_bird()