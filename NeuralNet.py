import math

class Neuron:
    def __init__(self, inputX, W_list):
        self.inputX = inputX
        self.W_list = W_list

    def z(self):
        total = 0
        for i in range(len(self.W_list)):
            total += self.W_list[i] * self.inputX[i]
        return total

    def a(self):
        return 1 / (1 + (math.e**(-self.z())))

def main():
    inputX = [1, 2, 3, 4]
    W1 = [
            [1, 2, 3, 4],
            [1, 2, 3, 4]
    ]
    W2 = [1,2]
    l11 = Neuron(inputX, W1[0]).a()
    l12 = Neuron(inputX, W1[1]).a()

    l1 = [l11, l12]
    l21 = Neuron(l1,W2).a()
    output = [l21]

    print(output)

if __name__ == "__main__":
    main()
