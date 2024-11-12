from functions import (b10_b2, 
                       range_correction, 
                       add_b2, 
                       b2_b10, 
                       sub_b2, 
                       filter_input, 
                       allowed_range)


def main() -> None:
    n1_input: str = input("n1 (ex: 8 or -8): ")
    n2_input: str = input("n2 (ex: 8 or -8): ")
    n_bits = int(input("Number of bits: "))
    n1: str
    n2: str
    n1_sign: str
    n2_sign: str
    n1, n2, n1_sign, n2_sign = filter_input(n1_input, n2_input)

    n1_positive: bool = n1_sign == '+'
    n2_positive: bool = n2_sign == '+'

    signed = n1_positive and n2_positive
    n_min: int
    n_max: int
    n_min, n_max = allowed_range(bits=n_bits, signed=signed)
    print(f"The allowed range is ({n_min} -- +{n_max})")


    if n1_positive and n2_positive:
        n1_b2: str = b10_b2(int(n1))
        print(f"{n1} in binary is {n1_b2}")

        n2_b2: str = b10_b2(int(n2))
        print(f"{n2} in binary is {n2_b2}")

        n1_b2_c: str
        n2_b2_c: str
        n1_b2_c, n2_b2_c = range_correction([n1_b2, n2_b2], req_bits=n_bits)
        print(f"{n1_b2} in range {n_bits} is {n1_b2_c}")
        print(f"{n2_b2} in range {n_bits} is {n2_b2_c}")

        addition: str = add_b2(n1_b2_c, n2_b2_c)
        print(f"{n1_b2_c} + {n2_b2_c} = {addition}")

        n_b10: int = b2_b10(b2=addition)
        print(f"{addition} in decimal is {n_b10}")
    
    elif not n1_positive and not n2_positive:
        n1_b2: str = b10_b2(int(n1))
        print(f"{'-' + n1} in binary is {'-' + n1_b2}")

        n2_b2: str = b10_b2(int(n2))
        print(f"{'-' + n2} in binary is {'-' + n2_b2}")

        n1_b2_c: str
        n2_b2_c: str
        n1_b2_c, n2_b2_c = range_correction([n1_b2, n2_b2], req_bits=n_bits)
        print(f"{'-' + n1_b2} in range {n_bits} is {'-' + n1_b2_c}")
        print(f"{'-' + n2_b2} in range {n_bits} is {'-' + n2_b2_c}")

        addition: str = add_b2(n1_b2_c, n2_b2_c)
        print(f"- {n1_b2_c} - {n2_b2_c} = {'-' + addition}")

        n_b10: int = b2_b10(b2=addition)
        print(f"{'-' + addition} in decimal is {-1 * n_b10}")

    elif n1_positive and not n2_positive:
        n1_b2: str = b10_b2(int(n1))
        print(f"{n1} in binary is {n1_b2}")

        n2_b2: str = b10_b2(int(n2))
        print(f"{'-' + n2} in binary is {'-' + n2_b2}")

        n1_b2_c: str
        n2_b2_c: str
        n1_b2_c, n2_b2_c = range_correction([n1_b2, n2_b2], req_bits=n_bits)
        print(f"{n1_b2} in range {n_bits} is {n1_b2_c}")
        print(f"{'-' + n2_b2} in range {n_bits} is {'-' + n2_b2_c}")

        n: str = sub_b2(n1_b2_c, n2_b2_c)
        print(f"{n1_b2_c} - {n2_b2_c} = {n}")

        b10: int = b2_b10(n)
        print(f"{n} in decimal is {b10}")

    else:
        n1_b2: str = b10_b2(int(n1))
        print(f"{'-' + n1} in binary is {'-' + n1_b2}")

        n2_b2: str = b10_b2(int(n2))
        print(f"{n2} in binary is {n2_b2}")

        n1_b2_c: str
        n2_b2_c: str
        n1_b2_c, n2_b2_c = range_correction([n1_b2, n2_b2], req_bits=n_bits)
        print(f"{'-' + n1_b2} in range {n_bits} is {'-' + n1_b2_c}")
        print(f"{n2_b2} in range {n_bits} is {n2_b2_c}")

        n: str = sub_b2(n1_b2_c, n2_b2_c)
        print(f"- {n1_b2_c} + {n2_b2_c} = {n}")

        b10: int = b2_b10(n)
        print(f"{n} in decimal is {b10}")

    return None

if __name__ == '__main__':
    main()