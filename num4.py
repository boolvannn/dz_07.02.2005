MorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/ '
}

def encode_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MorseCode:
            morse_code.append(MorseCode[char])
        else:
            morse_code.append('')
    return ' '.join(morse_code)

def decode_from_morse(code):
    code = code.split(' ')
    reversed_morse_code = {v: k for k, v in MorseCode.items()}
    decoded_text = []
    for morse in code:
        if morse in reversed_morse_code:
            decoded_text.append(reversed_morse_code[morse])
        else:
            decoded_text.append('')
    return ''.join(decoded_text)

def main():
    while True:
        action = input("Вы хотите закодировать или раскодировать текст? (encode/decode/exit): ").strip().lower()
        if action == 'encode':
            text = input("Введите текст для кодирования: ").strip()
            encoded_message = encode_to_morse(text)
            print(f"Закодированное сообщение: {encoded_message}")
        elif action == 'decode':
            code = input("Введите код Морзе для декодирования: ").strip()
            decoded_message = decode_from_morse(code)
            print(f"Раскодированное сообщение: {decoded_message}")
        elif action == 'exit':
            print("До свидания!")
            break
        else:
            print("Неверная команда. Пожалуйста, выберите 'encode', 'decode' или 'exit'.")

main()