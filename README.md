# TugasUAS
# --- data.py ---
class Data:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

# --- process.py ---
class Process:
    def __init__(self, data):
        self.data = data

    def validasi(self):
        """Memastikan jumlah dan harga tidak nol atau negatif."""
        if self.data.jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if self.data.harga <= 0:
            raise ValueError("Harga harus lebih dari 0")

    def hitung_total(self):
        """Menghitung total harga."""
        return self.data.jumlah * self.data.harga

# --- view.py ---
class View:
    def tampilkan(self):
        try:
            print("--- Input Data Barang ---")
            nama = input("Masukkan Nama Barang : ")
            jumlah = int(input("Masukkan Jumlah      : "))
            harga = float(input("Masukkan Harga       : "))

            # Inisialisasi Data dan Proses
            data_obj = Data(nama, jumlah, harga)
            mesin_proses = Process(data_obj)

            # Validasi dan Hitung
            mesin_proses.validasi()
            total = mesin_proses.hitung_total()

            # Tampilan Output (Tabel)
            print("\n=== DATA PEMBELIAN ===")
            print("+----------------+--------+------------+------------+")
            print("| Nama Barang    | Jumlah | Harga      | Total      |")
            print("+----------------+--------+------------+------------+")
            print(f"| {nama:<14} | {jumlah:<6} | {harga:<10.2f} | {total:<10.2f} |")
            print("+----------------+--------+------------+------------+")

        except ValueError as e:
            print(f"\n[!] Kesalahan Input: {e}")
        except Exception:
            print("\n[!] Terjadi kesalahan sistem.")

# --- main.py ---
if __name__ == "__main__":
    app = View()
    app.tampilkan()
