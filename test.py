class LZW:
    def encode(self, text: str) -> tuple[str, list]:
        i = 0
        len_ = len(text)
        code = ""

        start_dict = sorted(set(text))
        dict_ = start_dict[:]
        print(dict_)

        new_entry = ""
        while i < len_:
            new_entry += text[i]
            i += 1
            if new_entry not in dict_:
                dict_.append(new_entry)
                code += str(dict_.index(new_entry[:-1]))
                new_entry = ""
                i -= 1

        if new_entry not in dict_:
            dict_.append(new_entry)
        code += str(dict_.index(new_entry))

        return code, start_dict

    def decode(self, code: str, coding_dict: list) -> str:
        decoded_text = ""
        i = 0
        print(code, coding_dict)

        for symb in code:
            symb = int(symb)
            if int(symb) >= len(coding_dict):
                while len(coding_dict) <= symb:
                    new_entry = decoded_text[i]
                    i += 1
                    while i < len(decoded_text) and new_entry in coding_dict:
                        new_entry += decoded_text[i]
                        i += 1
                    if new_entry in coding_dict:
                        for new_char in new_entry:
                            new_entry += new_char
                            if new_entry not in coding_dict:
                                break

                    coding_dict.append(new_entry)
                    i -= 1
            decoded_text += coding_dict[symb]

        return decoded_text


code, dict_ = LZW().encode("ababababa")
print(LZW().decode(code, dict_))
