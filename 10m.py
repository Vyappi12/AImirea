
class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def chat(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'G'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'G':
            self.state = 'G'
            return 10
        raise MealyError('chat')

    def dash(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 5
        raise MealyError('dash')

    def chip(self):
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'H':
            self.state = 'B'
            return 11
        raise MealyError('chip')

    def patch(self):
        if self.state == 'G':
            self.state = 'H'
            return 9
        if self.state == 'B':
            self.state = 'D'
            return 4
        raise MealyError('patch')

def test():
    o = main()
    raises(lambda: o.patch(), MealyError)
    assert o.chat() == 0
    assert o.patch() == 4
    raises(lambda: o.dash(), MealyError)
    raises(lambda: o.patch(), MealyError)
    assert o.chip() == 6
    assert o.chat() == 7
    assert o.chip() == 8
    assert o.patch() == 9
    assert o.chip() == 11
    assert o.chat() == 3
    assert o.chat() == 10
    raises(lambda: o.chip(), MealyError)
    assert o.patch() == 9
    raises(lambda: o.chat(), MealyError)
    assert o.chip() == 11
    assert o.dash() == 2
    assert o.dash() == 5
    o = main()
    assert o.dash() == 1
    assert o.chip() == 6
    assert o.chat() == 7
    assert o.chip() == 8
    assert o.patch() == 9
    o = main()
    o = main()
    o = main()
    o = main()


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None

