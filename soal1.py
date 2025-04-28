def deteksi_hama(gejala):
    if "daun menguning" in gejala and "bercak hitam" in gejala:
        return "Hama E (daun menguning + bercak hitam)"
    elif "daun menguning" in gejala:
        return "Hama A (daun menguning)"
    elif "daun berlubang" in gejala:
        return "Hama B (daun berlubang)"
    elif "bercak hitam" in gejala:
        return "Hama C (bercak hitam)"
    elif "tanaman layu" in gejala:
        return "Hama D (tanaman layu)"
    else:
        return "Gejala tidak dikenali. Perlu pemeriksaan lebih lanjut."

def main():
    print("Deteksi Hama Tanaman")
    print("Masukkan gejala yang dialami tanaman (pisahkan dengan koma)")
    input_gejala = input("Contoh: daun menguning, bercak hitam\n> ")
    gejala_list = [g.strip().lower() for g in input_gejala.split(",")]
    hasil = deteksi_hama(gejala_list)
    print("\nHasil Deteksi:")
    print(hasil)

if __name__ == "__main__":
    main()
