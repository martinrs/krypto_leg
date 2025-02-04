import string

cipher_disc = string.ascii_lowercase
cipher_disc += string.digits
cipher_disc += 'ÆØÅ'
cipher_disc += ' '
cipher_disc += string.punctuation
cipher_disc += string.ascii_uppercase
cipher_disc += 'æøå'

def rotate(message, key):
    # Select mode between standard RotX and Cyclic key
    rot_list = []

    if not key.isdigit():
        rot_list = key.split('_')
        rot_i = 0
        rot = int(rot_list[rot_i])
    else:
        rot = int(key)

    # RotX
    out = ''
    for i in range(len(message)):
        if message[i] in cipher_disc:
            encrypted_i = cipher_disc.index(message[i]) + rot
            if encrypted_i > len(cipher_disc)-1:
                encrypted_i -= len(cipher_disc)-1
            out += cipher_disc[encrypted_i]
        else:
            out += '?'

        # Cyclic key
        if len(rot_list) > 0:
            if rot_i < len(rot_list)-1:
                rot_i += 1
            else:
                rot_i = 0
            rot = int(rot_list[rot_i])
    return out


if __name__ == '__main__':
    msg = 'Lorem ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development to fill empty spaces in a layout that do not yet have content. Lorem ipsum is typically a corrupted version of De finibus bonorum et malorum, a 1st-century BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin.'
    print(rotate(msg, '100_39_52_2_4'))
    print(rotate(msg, '39'))