meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
word = input("masukan kata : ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kata tidak ada")
