import enchant


class CaesarsCipher:
    def __init__(self):
        self.code_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
        self.En_dict = enchant.Dict('en_US')

    def decrypt(self, info):
        for key in range(len(self.code_chars)):
            result = ''

            for curr_chr in info:
                index = self.code_chars.find(curr_chr)
                if index + key >= len(self.code_chars):
                    index -= len(self.code_chars)
                result += self.code_chars[index + key]

            flag_check_info = False
            for i in result.split():
                if self.En_dict.check(i) == False:
                    flag_check_info = False
                    break
                else:
                    flag_check_info = True
            if flag_check_info == True:
                return key, result

    def encrypt(self, info, key):
        result = ''
        for curr_char in info:
            index = self.code_chars.find(curr_char)
            if index + key >= len(self.code_chars):
                index -= len(self.code_chars)
            result += self.code_chars[index + key]
        return result


if __name__ == '__main__':
    string_to_be_checked = 'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D'
    test_str = 'Wkh.ydfdwlrq.zdv.d.vxffhvv'
    cipher = CaesarsCipher()
    print(f'key: {cipher.decrypt(test_str)[0]}, '
          f'result: {cipher.decrypt(test_str)[1]}')
    print(cipher.encrypt(cipher.decrypt(test_str)[1], -cipher.decrypt(test_str)[0]))