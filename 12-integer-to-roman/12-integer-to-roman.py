class Solution:
    def intToRoman(self, num: int):
        num_str = str(num)  #Breaks down number in string form
        expand_num = []     #Stores the digits when broken down into 1s and 5s
        place_val = 10 ** (len(num_str) - 1)
        pos = 0
        hash_t = {}
        res = ""
        
        roman_hash = {"0": "", "1": "I", "4": "IV", "5": "V", "9": "IX",
                      "10": "X", "40": "XL", "50": "L", "90": "XC",
                      "100": "C", "400": "CD", "500": "D", "900": "CM", "1000": "M"
                      }
        expand_hash = {
            "2": "11", "3": "111", "6": "51", "7": "511", "8": "5111"
        }

        for val in num_str:
            if val in expand_hash.keys():
                expand_num.append(expand_hash[val])
                #breaks the digit down if it's a 2, 3, 6, 7, or 8
            else:
                expand_num.append(val)

        while pos < len(expand_num):
            hash_t[int(place_val)] = expand_num[pos]
            # the place values are used as keys instead of using the digits as there might be duplicate digits
            # which would not be stored in the dictionary as keys twice.
            pos += 1
            place_val /= 10

        for key in hash_t:
            val = hash_t[key]

            # Uses the key place value as a multiplier to generate the key for roman_hash
            if val in roman_hash.keys():
                res += roman_hash[str(int(val) * key)]
            else:
                for d in val:
                    res += roman_hash[str(int(d) * key)]
        return res
    