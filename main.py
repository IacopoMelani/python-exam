def create_dict(numbers=[]):
    dict = {}

    for i, n in enumerate(numbers):
        if n > 0:
            dict[i] = n

    return dict


def exercise_1():
    dict = create_dict([1, -2, 3, -4, 5])
    print(dict)


def swap_rows(matrix, r1, r2):
    matrix_len = len(matrix)
    if max(r1, r2) > matrix_len:
        raise Exception("Colonne non valide")
    pro_mode = not False
    if pro_mode:
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
    else:
        temp = matrix[r1]
        matrix[r1] = matrix[r2]
        matrix[r2] = temp
    return matrix


def swap_column(matrix, c1, c2):
    pro_mode = not False
    for row in matrix:
        if pro_mode:
            row[c1], row[c2] = row[c2], row[c1]
        else:
            temp = matrix[c1]
            matrix[c1] = matrix[c2]
            matrix[c2] = temp

    return matrix


def exercise_2():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # swap_rows(matrix, 0, 1)
    swap_column(matrix, 2, 1)
    print(matrix)


def exercise_3():
    print(conta_caratteri_parole("Test conta parole molto super"))


def conta_caratteri_parole(str=""):
    str = str.strip()
    if str == "":
        return 0, 0
    pro_mode = False
    if pro_mode:
        return len(str), len(str.split(" "))
    else:
        char_counter = 0
        word_counter = 0
        for index, s in enumerate(str):
            char_counter += 1
            if s == " " and len(str) - 1 != index:
                word_counter += 1
        return char_counter, word_counter + 1


def gcd(a, b):
    # print(a, b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


class Frazione:
    def __init__(self, numeratore, denominatore) -> None:
        if denominatore == 0:
            raise Exception("Denominatore == 0!")
        self.numeratore = numeratore
        self.denominatore = denominatore

        self.semplifica()

    def semplifica(self):
        common_factor = gcd(self.numeratore, self.denominatore)

        self.numeratore = int(self.numeratore / common_factor)
        self.denominatore = int(self.denominatore / common_factor)

    def frazione_decimale(self):
        return self.numeratore / self.denominatore


def somma_frazioni(f1: Frazione, f2: Frazione):
    new_denominatore = lcm(f1.denominatore, f2.denominatore)
    new_numeratore = (new_denominatore / f1.denominatore * f1.numeratore) + (
        new_denominatore / f2.denominatore * f2.numeratore
    )
    return Frazione(new_numeratore, new_denominatore)


def exercise_4():
    f1 = Frazione(22, 10)
    f2 = Frazione(10, 10)
    print(somma_frazioni(f1, f2).frazione_decimale())


def prodotto_matrice_vettore(matrix=[], vec=[]):
    for row in matrix:
        for index, v in enumerate(vec):
            if len(row) >= len(vec):
                row[index] = row[index] * v
    return matrix


def exercise_5():
    matrix = [[1, 2, 3, 5], [3, 4, 10]]
    vec = [1, 2, 100, 3]
    matrix = prodotto_matrice_vettore(matrix, vec)
    print(matrix)


class Offer:
    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount


class Auction:
    def __init__(self) -> None:
        self.offers = []
        self.open = True

    def add_offer(self, offer):
        if not self.open:
            raise Exception("Asta chiusa")
        if len(self.offers) == 0 or self.offers[0].amount < offer.amount:
            self.offers.insert(0, offer)
        else:
            self.offers.append(offer)

    def get_highest_offer(self):
        return self.offers[0] if len(self.offers) > 0 else None

    def end_auction(self):
        self.open = False
        return self.get_highest_offer()


def exercise_6():
    auction = Auction()

    offer1 = Offer("Alice", 100)
    offer2 = Offer("Bob", 200)
    offer3 = Offer("Charlie", 300)

    auction.add_offer(offer1)
    auction.add_offer(offer2)

    highest_offer = auction.get_highest_offer()
    if highest_offer:
        print(highest_offer.name)
        print(highest_offer.amount)

    auction.add_offer(offer3)

    winning_offer = auction.end_auction()

    if winning_offer:
        print(winning_offer.name)
        print(winning_offer.amount)


# exercise_1()
# exercise_2()
# exercise_3()
# exercise_4()
# exercise_5()
exercise_6()

