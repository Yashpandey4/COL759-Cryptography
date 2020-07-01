import numpy as np


def read_input(file_name: str) -> str:
    f = open(file_name, "r")
    data = f.read()
    f.close()
    return data


def get_next_letter_pos(arr: list, idx: int) -> int:
    res = 0
    for i in range(idx, len(arr)):
        if arr[i].islower():
            res = i
            break
    return res


def write_output(data: str, encoded_letters: str, name: str) -> None:
    res = list(data)
    idx = 0
    for encoded_letter in encoded_letters:
        if res[idx].islower():
            res[idx] = encoded_letter
            idx += 1
        else:
            next_letter_pos = get_next_letter_pos(list(data), idx)
            res[next_letter_pos] = encoded_letter
            idx = next_letter_pos + 1
    f = open(name, "w")
    f.write(''.join(res))
    f.close()


def encrypt_data(data: str, key: list) -> str:
    arr = []
    res = list(data)
    idx = 0
    count = 0
    for letter in data:
        if letter.islower():
            count = count + 1
            arr.append(ord(letter) - 97)
            if len(arr) == len(key):
                arr = np.array([arr]).T.tolist()
                encoded_letters = np.matmul(np.array(key), arr).T.ravel().tolist()
                for encoded_letter in encoded_letters:
                    res[idx] = chr((encoded_letter % 26) + 97)
                    idx += 1
                arr = []
    return ''.join(res)


def get_key(encrypted_word: str, popular_word: str, n: int):
    decrypted_guess = [[(ord(popular_word[0]) - 97), (ord(popular_word[2]) - 97)],
                       [(ord(popular_word[1]) - 97), (ord(popular_word[3]) - 97)]] if n == 2 else [
        [(ord(popular_word[0]) - 97), (ord(popular_word[3]) - 97), (ord(popular_word[6]) - 97)],
        [(ord(popular_word[1]) - 97), (ord(popular_word[4]) - 97), (ord(popular_word[7]) - 97)],
        [(ord(popular_word[2]) - 97), (ord(popular_word[5]) - 97), (ord(popular_word[8]) - 97)]]

    encrypted_matrix = [[(ord(encrypted_word[0]) - 97), (ord(encrypted_word[2]) - 97)],
                        [(ord(encrypted_word[1]) - 97), (ord(encrypted_word[3]) - 97)]] if n == 2 else [
        [(ord(encrypted_word[0]) - 97), (ord(encrypted_word[3]) - 97), (ord(encrypted_word[6]) - 97)],
        [(ord(encrypted_word[1]) - 97), (ord(encrypted_word[4]) - 97), (ord(encrypted_word[7]) - 97)],
        [(ord(encrypted_word[2]) - 97), (ord(encrypted_word[5]) - 97), (ord(encrypted_word[8]) - 97)]]

    det = int(round(np.linalg.det(np.array(encrypted_matrix))))
    inv_det = 0
    for i in range(1, 26):
        if i * det % 26 == 1:
            inv_det = i
            break
    if inv_det == 0:
        return None
    inv_encrypted_matrix = inv_det * (np.linalg.inv(encrypted_matrix) * det)
    key = np.rint(np.matmul(np.array(decrypted_guess), inv_encrypted_matrix)) % 26
    key = key.astype(int)
    return key


def decrypt_data(original_data: str, key_len: int) -> None:
    data = ''.join(original_data.split())
    popular_words = ["tion", "nthe", "ther", "that", "ofth", "thes", "with", "inth", "othe"] if key_len == 2 else [
        "fireboard", "identical", "chocolate", "Christmas", "beautiful", "happiness", "Wednesday", "challenge",
        "celebrate", "adventure", "important", "consonant", "Christian", "dangerous", "masculine", "Australia",
        "irregular", "something", "Elizabeth", "knowledge", "macaronic", "pollution", "President", "wrestling",
        "pineapple", "adjective", "secretary", "undefined", "Halloween", "Amerindic", "ambulance", "alligator",
        "seventeen", "affection", "congruent", "marijuana", "community", "different", "vegetable", "influence",
        "structure", "invisible", "wonderful", "packaging", "provoking", "nutrition", "crocodile", "education",
        "abounding", "beginning"]
    n = 4 if key_len == 2 else 9

    if key_len < 2 or key_len > 3:
        return

    possible_decrypted_data_list = []
    print('Select the entry below which was decrypted successfully')

    for popular_word in popular_words:
        for i in range(0, len(data), n):
            encrypted_ngram = data[i: i + n]
            if len(encrypted_ngram) == n:
                key = get_key(encrypted_ngram, popular_word, key_len)
                if key is not None:
                    possible_decrypted_data = encrypt_data(data, key)
                    if popular_word in possible_decrypted_data:
                        possible_decrypted_data_list.append(possible_decrypted_data)

        for i in range(len(possible_decrypted_data_list)):
            print(f"\nOption {i}:\n")
            print(possible_decrypted_data_list[i])

        choice = int(input("Enter your choice, or input -1 if none of the options match:"))

        if choice <= -1 or choice >= len(possible_decrypted_data_list):
            if choice != -1:
                print("Invalid input")
            possible_decrypted_data_list = []
            continue

        else:
            write_output(original_data, possible_decrypted_data_list[choice], f"possible_output.txt")
            break


if __name__ == '__main__':
    encrypted_data = read_input("encrypted_output.txt")
    key_length = 3
    decrypt_data(encrypted_data, key_length)
    print("Done")
