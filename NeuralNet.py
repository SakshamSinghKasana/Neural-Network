class Neuron:
    def __init__(self, inputX, W_list):
        self.inputX = inputX
        self.W_list = W_list

    def z(W_list,inputX):
        sum = 0
        for i in range(len(W_list)):
            sum += W_list*inputX
        return sum

    def a(z):
        return 1/(1+(2.718**(-z)))

def main():
    inputX = [1,2,3,4]
    W1 = [[1,2,3,4],[1,2,3,4]]
    W2 = [1,2]

    l01 = inputX[0]
    l02 = inputX[1]
    l03 = inputX[2]
    l04 = inputX[3]

    l11 = Neuron(inputX, W_list)
    l12 = Neuron(inputX, W_list)

    l0 = [l01,l02,l03,l04]
    l1 = [l11,l12]
    l = [l0,l1]

    for i in 
