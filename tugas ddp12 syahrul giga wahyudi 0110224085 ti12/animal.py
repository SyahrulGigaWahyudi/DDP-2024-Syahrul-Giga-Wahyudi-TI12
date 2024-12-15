class animal:
    def __init__(self,name,makanan,hidup,berkembang_biak):
        self.name=name
        self.makanan=makanan
        self.hidup=hidup
        self.berkembang_biak=berkembang_biak
     
        #method informasi
    
    def info_animal(self):
        print("Nama hewan\t\t: ",self.name,"\nMakanan\t\t\t: ",self.makanan,"\nHidup\t\t\t: ",self.hidup, "\nBerkembang biak \t: ",self.berkembang_biak)
        

kucing= animal("kucing","daging","darat","melahirkan")
kucing.info_animal()

        