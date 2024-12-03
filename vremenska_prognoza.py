temperatura = int(input("unesite temperaturu: "))
test_temperatura = -1
temperatura = test_temperatura
poruka = ""
if temperatura < 0:
    poruka = "Oprez klizavo"

if temperatura > 0:
    print("Temperatura iznad 0")
    if temperatura > 30:
        poruka = "Ukljucite klima uredjaje"


ocekivana_poruka = "Oprez klizavo"
if poruka == ocekivana_poruka:
    print("Case - ispod nule - Test prosao")