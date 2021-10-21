import struct
from itertools import islice
 
 
def float_to_bin_parts(number, bits=64):
    if bits == 32:          # single precision
        int_pack      = 'I'
        float_pack    = 'f'
        exponent_bits = 8
        mantissa_bits = 23
        exponent_bias = 127
    elif bits == 64:        # double precision. all python floats are this
        int_pack      = 'Q'
        float_pack    = 'd'
        exponent_bits = 11
        mantissa_bits = 52
        exponent_bias = 1023
    else:
        raise ValueError('bits argument must be 32 or 64')
    bin_iter = iter(bin(struct.unpack(int_pack, struct.pack(float_pack, number))[0])[2:].rjust(bits, '0'))
    return [''.join(islice(bin_iter, x)) for x in (1, exponent_bits, mantissa_bits)]
 
 
number = 0.1111111

def from_mantissa_to_number(m:str) -> float:
    result = 0
    for index, item in enumerate(m):
        result += int(item) * 2**(-1 * (index + 1))
    return result

def get_mantissa(number):
    number %= 1
    
    result = ''
    for i in range(23):
        result += str(int(number * 2))
        number *= 2
        number %= 1
    return result

for j in range(9):
    initial_number = number * (j + 1)
    print(initial_number)
    for i in range(20):
        num = initial_number + 2**i
        sign, exponent, mantissa = float_to_bin_parts(num, 32)
        exp = int(exponent, 2)
        print("Знак: {}, Экспонента: {} ({}), Мантиса: 1.{}, Число: {}, Остаток: {}, {}".format(sign, exponent, exp, mantissa, num, round(from_mantissa_to_number(mantissa[exp - 127:]), 10), exp - 127))
    print()
