import enchant


class CaesarsCipher:
    Code_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    En_dict = enchant.Dict('en_US')
    @staticmethod
    def decrypt(info):
        for key in range(len(CaesarsCipher.Code_chars)):
            result = ''

            for curr_chr in info:
                index = CaesarsCipher.Code_chars.find(curr_chr)
                if index + key >= len(CaesarsCipher.Code_chars):
                    index -= len(CaesarsCipher.Code_chars)
                result += CaesarsCipher.Code_chars[index + key]

            flag_check_info = False
            for i in result.split():
                if CaesarsCipher.En_dict.check(i) == False:
                    flag_check_info = False
                    break
                else:
                    flag_check_info = True
            if flag_check_info == True:
                return key, result

            # if (CaesarsCipher.En_dict.check(result.split()[0]) and
            #         CaesarsCipher.En_dict.check(result.split()[1])):
            #     return key, result

    @staticmethod
    def encrypt(info):
        pass


if __name__ == '__main__':
    string_to_be_checked = 'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D'
    test_str = 'Wkh.ydfdwlrq.zdv.d.vxffhvv'

    print(f'key: {CaesarsCipher.decrypt(test_str)[0]}, '
          f'result: {CaesarsCipher.decrypt(test_str)[1]}')