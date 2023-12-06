import emoji

texto = input("Input: ")
if texto == ":thumbsup:":
    texto = ":thumbs_up:"
if ":earth_asia:" in texto:
    texto = texto.replace(":earth_asia:", ":globe_showing_Asia-Australia:")

print(f"{emoji.emojize(texto)}")
