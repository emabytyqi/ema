objekt = {
    "emri":"Ema",
    "mbiemri":"Bytyqi",
    "mosha":15 
    }
key = input("shkruaje property:")
if key in objekt:
    print("po ekziston")
else:
    print("jo nuk ekziston")

piket = {
    "Dea":77,
    "Ereni":81,
    "Ela":75,
    "Trimi":90,
    "Ema":100
}
shuma_e_pikeve = sum(piket.values())
piket_mesatare = shuma_e_pikeve / len(piket)
print(f"piket mesatare jane {piket_mesatare}")