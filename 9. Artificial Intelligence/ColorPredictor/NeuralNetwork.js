class NeuralNetwork {
       constructor(n) {
         this.weights = [];
         for (let i=0; i<n; i++) {
           this.weights[i] = Math.random() * 2 - 1;
         }
         
       }
       
       guess(inputs) {
         let sum = 0;
         
         for (let i=0; i<this.weights.length; i++) {
           sum += inputs[i] * this.weights[i];
         }
         
         let output = activation(sum);
         return output;
       }
       
       train(inputs, target) {
         let guess = this.guess(inputs);
         let error = target - guess;
         
         for (let i=0; i<this.weights.length; i++) {
           this.weights[i] += error * inputs[i] * 0.01; //how does this work?
         }
       }
}

function activation(n) {
  return n >= 0 ? 1 : -1;
}

/*
- what is OOP: class and instance
- neural networks perceptron
  - basic math and converting theory into practice
  - why it's not enough 
    - 1d universal function approximator
    - 3d space
- using library with hidden layers
*/
