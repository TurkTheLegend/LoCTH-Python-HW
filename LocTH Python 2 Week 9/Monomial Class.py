class Monomial:
    def __init__(self, a: int, k: list, is_positive: bool) -> None:
        self.a = abs(a)
        self.k = k
        self.is_positive = is_positive

    def isMonomial(self) -> bool:
        for i in self.k:
            if not (isinstance(i, int)):
                return False
            elif i < 0 :
                return False
        return True

    def maxDegree(self) -> int:
        return max(self.k)

    def isConstant(self) -> int:
        return self.countVariable() != 0

    def countVariable(self) -> int:
        return len(self.k)

    def MathematicalTerm(self) -> str:
        if self.is_positive:
            result = str(self.a)
        else :
            result = str(-self.a)
        for i in range(self.countVariable()):
            if self.k[i] == 1 :
                result = result + "x_" + str(i)
            else :
                result = result + "x_" + str(i) + "^" + str(self.k[i])
        return result

def isSimilarMonomial(x: Monomial, y: Monomial) -> bool:
    x.k.sort()
    y.k.sort()
    return x.k == y.k

def bruh(x: Monomial, y: Monomial) -> Monomial:
    if isSimilarMonomial:
        result = Monomial(a = 0 , k = x.k, is_positive = None)
        if not(x.is_positive) :
            x.a = -(x.a)
        if not(y.is_positive) :
            y.a = -(y.a)
        result.a = x.a + y.a
        if result.a > 0 :
            result.is_positive = True
        else :
            result.is_positive = False
        result.a = abs(result.a)
        return result

def bruh2(x: Monomial, y: Monomial) -> Monomial:
    result = Monomial(a = x.a * y.a, k = sum(x.k) + sum(y.k), is_positive = True)
    if (x.is_positive == False and y.is_positive == True) or (x.is_positive == True and y.is_positive == False):
        result.is_positive = False
    return result