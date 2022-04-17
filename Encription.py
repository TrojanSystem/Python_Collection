alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


run = 'yes';

while run == 'yes':
    choose = input('Type encode to Encrypt or decode to Decrypt: ')
    message = input('Type a word: ').lower()
    shifter = input('Insert the shifter: ')
    def encryptsText(message, shift):
        cipherText = ''
        for i in message:
            positions = alpabet.index(i)
            newPositions = positions + shift

            newLetter = alpabet[newPositions]
            cipherText = cipherText + newLetter
        print(cipherText)
        

    def decrptText(message, shift):
        cipherText = ''
        for i in message:
            positions = alpabet.index(i)
            newPositions = positions - shift
            newLetter = alpabet[newPositions]
            cipherText = cipherText + newLetter
        print(cipherText)
        

    if choose == 'encode':
        encryptsText(message, int(shifter))
        run = input('runAgain: ').lower()
        if run == 'no':
           run = 'no';
    else:
        decrptText(message, int(shifter))
        run = input('runAgain: ').lower()
        if run == 'no':
            run = 'no';
       