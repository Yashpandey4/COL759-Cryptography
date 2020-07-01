import numpy as np


def read_input(file_name: str) -> str:
    f = open(file_name, "r")
    data = f.read()
    f.close()
    return data


def write_output(data: str, name: str) -> None:
    f = open(name, "w")
    f.write(data)
    f.close()


def get_next_letter_pos(arr: list, idx: int) -> int:
    res = 0
    for i in range(idx, len(arr)):
        if arr[i].islower():
            res = i
            break
    return res


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
                    if res[idx].islower():
                        res[idx] = chr((encoded_letter % 26) + 97)
                        idx += 1
                    else:
                        next_letter_pos = get_next_letter_pos(list(data), idx)
                        res[next_letter_pos] = chr((encoded_letter % 26) + 97)
                        idx = next_letter_pos + 1
                arr = []
    return ''.join(res)


def decrypt_data(data: str, key: list) -> str:
    det = int(np.linalg.det(np.array(key)))
    inv_det = 0
    for i in range(1, 26):
        if i * det % 26 == 1:
            inv_det = i
            break
    if inv_det == 0:
        return "ERROR"
    inv_key = inv_det * (np.linalg.inv(key) * det).tolist()
    inv_key = [list(map(int, i)) for i in inv_key]
    return encrypt_data(data, inv_key)


if __name__ == '__main__':
    input_data = read_input("text_input.txt")
    key_matrix = [[22, 3], [9, 6]]
    encrypted_data = encrypt_data(input_data, key_matrix)
    write_output(encrypted_data, "encrypted_output.txt")
    decrypted_data = decrypt_data(encrypted_data, key_matrix)
    write_output(decrypted_data, "decrypted_output.txt")
