class Process:
    def __init__(self, data):
        self.data = data

    def validasi(self):
        if self.data.jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if self.data.harga <= 0:
            raise ValueError("Harga harus lebih dari 0")

    def hitung_total(self):
        return self.data.jumlah * self.data.harga
