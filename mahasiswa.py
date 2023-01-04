class Mahasiswa:
    # atribut
    # konstruktor
    def __init__(self, nim, nama, rombel) :
        # variable objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
    # method
    def lulus(self,nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")

    def cetak(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Rombel :", self.rombel)


# objek
mahasiswa1 = Mahasiswa("011022", "azis","Ti05")

mahasiswa1.cetak()
mahasiswa1.lulus(95)

# objek ke -2
mahasiswa2 = Mahasiswa("01103", "dadin", "Ti05")
mahasiswa2.nama = "dadin"
mahasiswa2.nim = "01103"
mahasiswa2.rombel = "Ti05"
mahasiswa2.cetak()
mahasiswa2.lulus(85)

