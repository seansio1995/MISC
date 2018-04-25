import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights=np.random.random((3,1))*2-1

    def __sigmoid(self,z):
        return 1/(1+np.exp(-z))


    def __sigmoid_derivative(self,z):
        return z*(1-z)


    def train(self,training_set_inputs,training_set_outputs,number_of_iterations):
        for i in range(number_of_iterations):
            outputs=self.think(training_set_inputs)

            error=training_set_outputs-outputs
            ##gradient descent
            adjustment=np.dot(training_set_inputs.T,error*self.__sigmoid_derivative(outputs))

            self.synaptic_weights+=adjustment

    def think(self,inputs):
        return self.__sigmoid(np.dot(inputs,self.synaptic_weights))




if __name__=="__main__":
    neural_network=NeuralNetwork()
    print("Random starting synaptic weigts: {}".format(neural_network.synaptic_weights))

    ###data
    training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = np.array([[0, 1, 1, 0]]).T


    ####train
    neural_network.train(training_set_inputs,training_set_outputs,10000)



    ###test
    print("New synaptic weights after training {}".format(neural_network.synaptic_weights))
    print("When the input is [1,0,0] the result is {}".format(neural_network.think(np.array([1,0,0]))))
