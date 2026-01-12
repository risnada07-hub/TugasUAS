from data import Data
from process import Process

class View:
    def tampilkan(self):
        try:
            nama = input("Masukkan Nama Barang : ")

            jumlah = int(input("Masukkan Jumlah      : "))
            harga = float(input("Masukkan Harga       : "))

            data = Data(nama, jumlah, harga)
            proses = Process(data)

            proses.validasi()
            total = proses.hitung_total()

            # Table View
            print("\n=== DATA PEMBELIAN ===")
            print("+----------------+--------+------------+------------+")
            print("| Nama Barang    | Jumlah | Harga      | Total      |")
            print("+----------------+--------+------------+------------+")
            print(f"| {nama:<14} | {jumlah:<6} | {harga:<10.2f} | {total:<10.2f} |")
            print("+----------------+--------+------------+------------+")

        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception:
            print("Terjadi kesalahan yang tidak terduga")
