from PIL import Image

def bin_to_sprava(bin_message):
    message = ""
    for i in range(0, len(bin_message), 7):
        char_bin = bin_message[i:i+7]
        char = chr(int(char_bin, 2))
        if char == "#":
            break
        message += char
    return message

def extract_message(pic):
    pixels = pic.load()
    bin_message = ""
    for y in range(pic.size[1]):
        for x in range(pic.size[0]):
            blue_bin = bin(pixels[x, y][2])[2:]
            if len(blue_bin) > 1:
                bin_message += blue_bin[-1]
    return bin_to_sprava(bin_message)

if __name__ == "__main__":
    # Načítanie zakódovaného obrázka
    skryty_obr = Image.open("skryta_sprava.png")
    vytiahnuta_sprava = extract_message(skryty_obr)
    print("Vytiahnutá správa:", vytiahnuta_sprava)