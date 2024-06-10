meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL":"Tanggapan terhadap lelucon",
            "OTW":"Menuju ketujuan",
            "MAGER":"Males gerak/beraktivitas",
            "MANTUL":"Mantap betul",
            "GWS":"Cepat sembuh"
            }
word=input("Masukkan kata gaul:")
if word.upper() in meme_dict.keys():
    print("Artinya adalah:", meme_dict[word.upper()])
else:
    print("error!!!")
