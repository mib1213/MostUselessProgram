def b10_b2(b10: int) -> str:
    base_10: int = abs(b10)
    remainders: list[int] = []
    while base_10 != 0:
        remainder: int = base_10 % 2
        remainders.append(remainder)
        base_10 = (base_10 - remainder) // 2

    base_2: str = ''
    for num in remainders[::-1]:
        base_2 = base_2 + str(num)
    if b10 > 0:
        return base_2
    elif b10 == 0:
        return '0'
    else: 
        return '-' + base_2

def b2_b10(b2: str) -> int:
    if b2[0] == '-':
        base_2_without_sign: str = b2.replace('-', '')
    else:
        base_2_without_sign: str = b2
    terms: list[int] = []
    for i, n in enumerate(base_2_without_sign, 1):
        terms.append(int(n) * (2**(len(base_2_without_sign)-i)))
    
    base_10: int = 0
    for term in terms:
        base_10 += term
    
    if b2[0] == '-':
        base_10 = base_10 * -1
    return base_10

def allowed_range(bits: int, signed: bool = True) -> tuple[int]:
    if signed:
        n_min: int = -1 * (2**bits) // 2
        n_max: int = ((2**bits) // 2) - 1
    else:
        n_min: int = 0
        n_max: int = (2**bits) - 1
        
    return n_min, n_max

def range_correction(numbers: list[str], req_bits: int) -> list[str]:
    numbers_without_sign: list[str] = [n.replace('-', '') if n[0] == '-' else n for n in numbers]

    new_numbers_without_sign: list[str] = []
    for n in numbers_without_sign:
        if len(n) < req_bits:
            additional_zeros: int = req_bits - len(n)
            new_numbers_without_sign.append((additional_zeros * '0') + n)
        else:
            new_numbers_without_sign.append(n)

    new_numbers_with_sign: list[str] = []
    for i, n in enumerate(new_numbers_without_sign):
        if numbers[i][0] == '-':
            new_numbers_with_sign.append('-' + n)
        else:
            new_numbers_with_sign.append(n)
    return new_numbers_with_sign

def add_b2(n1: str, n2: str) -> str:  
    n1_list: list[str] = [n for n in n1]
    n2_list: list[str] = [n for n in n2]
    n3_list: list[str] = ['0' for _ in n2]
    result_list: list[str] = []

    for i in range(len(n1_list)-1, -1, -1):
        if n1_list[i] == '1' and n2_list[i] == '1' and n3_list[i] == '1':
            result_list.append('1')
            if i != 0:
                n3_list[i-1] = '1'
        elif (n1_list[i] == '1' and n2_list[i] == '1') or (n1_list[i] == '1' and n3_list[i] == '1') or (n2_list[i] == '1' and n3_list[i] == '1'):
            result_list.append('0')
            if i != 0:
                n3_list[i-1] = '1'

        elif n1_list[i] == '1' or n2_list[i] == '1' or n3_list[i] == '1':
            result_list.append('1')
        else:
            result_list.append('0')
        
    result_list = result_list[::-1]
    return ''.join(result_list)

def opposite(b2: str) -> str:
    return ''.join(['0' if n == '1' else '1' for n in b2])

def sub_b2(n1: str, n2: str) -> str:
    n2: str = opposite(n2)
    one: str = '1'
    for _ in range(len(n2)-1):
        one = '0' + one

    n2: str = add_b2(n2, one)

    n: str = add_b2(n1, n2)

    if n[0] == '1':
        opposite_one: str = opposite(one)
        opposite_one_with_one: str = add_b2(opposite_one, one)
        n: str = '-' + opposite(add_b2(n, opposite_one_with_one))

    return n


def filter_input(n1: str, n2: str) -> tuple[str]:
    if n1[0] == '-':
        n1 = n1.replace('-', '')
        n1_sign: str = '-'
    else:
        n1_sign: str = '+'
    
    if n2[0] == '-':
        n2 = n2.replace('-', '')
        n2_sign: str = '-'
    else:
        n2_sign: str = '+'
    
    return n1, n2, n1_sign, n2_sign