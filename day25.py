def get_encryption_key(card_public_key, door_public_key):
    v, subject_num = 1, 7
    loop_size = 0
    while v != card_public_key:
        v *= subject_num
        v = v % 20201227
        loop_size += 1

    v = 1
    for i in range(loop_size):
        v *= door_public_key
        v = v % 20201227
    return v


if __name__ == '__main__':
    pk_card = 14082811
    pk_door = 5249543
    print(get_encryption_key(pk_card, pk_door))
