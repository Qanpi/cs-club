function activation(sum) {
  if (sum >= 0) return 1;
  else return -1;

  //return sum >= 0 ? 1 : -1;
}

class NeuralNetwork {
  constructor(n) {
    this.weights = [];
    for (let i = 0; i < n; i++) {
      this.weights[i] = Math.random() * 2 - 1;
    }
  }

  //inputs -> [200, 150, 10]
  guess(inputs) {
    let sum = 0;

    for (let i = 0; i < inputs.length; i++) {
      sum += this.weights[i] * inputs[i];
    }

    let output = activation(sum);
    return output;
  }

  train(inputs, target) {
    let guess = this.guess(inputs);
    let error = target - guess;

    for (let i = 0; i < this.weights.length; i++) {
      let step = error * inputs[i] * 0.01;

      this.weights[i] += step;
    }
    
    let weightsString = ""
    for (let w of this.weights) {
      weightsString += w + " ";
    }
    console.log(weightsString);
  }
}
