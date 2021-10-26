class Transformer(object):
    decimal_digits = '0123456789'
    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        if fromdigits == todigits: # don't have to convert
            return number
        else:
            fromdigits_len, todigits_len = len(fromdigits), len(todigits)
            number = str(number)
            number_len = len(number)

            # get temp_decimal_val
            tmp_dec = 0
            for idx, n in enumerate(number):
                tmp = fromdigits_len**(number_len-idx-1) * fromdigits.index(n)
                tmp_dec += tmp

            # get todigits_val from decimal_val
            result = ''
            while tmp_dec > 0:
                tmp_dec, mod = divmod(tmp_dec, todigits_len)
                result += str(todigits[mod])
            return result[::-1]

# For test
print("hex")
hex_transformer = Transformer('0123456789ABCDEF')
print(hex_transformer.to_decimal('42C'))
print(hex_transformer.from_decimal(1234))
print("dec")
dec_transformer = Transformer('0123456789')
print(dec_transformer.to_decimal('425'))
print(dec_transformer.from_decimal(1234))
print("base62")
base62_transformer = \
    Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
print(base62_transformer.to_decimal('Bs'))
print(base62_transformer.from_decimal(1234))

