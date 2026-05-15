class TwoSum(object):

    def __init__(self):
        self.count = {}

    def add(self, number):
        self.count[number] = self.count.get(number, 0) + 1

    def find(self, value):
        for num in self.count:
            complement = value - num

            if complement in self.count:
                if complement != num or self.count[num] > 1:
                    return True

        return False
