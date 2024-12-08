class gempa:
    # konstruktor inisialisasi artribut lokasi dan sekala
    def __init__(self,lokasi,skala):

        #atribut
        self.lokasi=lokasi
        self.skala=skala

    #method menentukan dampak skala gempa
    def dampak (self):
        #statment/logika
        if self.skala < 2:
            print("Dampak Gempa tidak Berasa")
        elif self.skala >=2 and self.skala <=4 :
            print("Dampak Gempa Bangunan retak retak")
        elif self.skala >4 and self.skala <=6:
            print("Dampak Gempa Berpontesi Bangunan Roboh")
        elif self.skala >6:
            print("Damapak Gempa Berpontesi Tsunami")

            #menamilkan lokasi dan skala

        print(f"lokasi gempa: {self.lokasi}")
        print(f"skala gempa: {self.skala}")
        
        
