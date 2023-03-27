let nn;

function setup() {
  createCanvas(400, 300);
  noLoop();
  
  nn = new NeuralNetwork(4);
  
  for (let i=0; i<100000; i++) {
    train();
  }
  
  mousePressed( );
}

function train() {
  let r = random(255);
  let g = random(255);
  let b = random(255);

  let target = predictColor(r, g, b);
  nn.train([r, g, b, 255], target);
}

function mousePressed() {
  let r = random(255);
  let g = random(255);
  let b = random(255);
  
  background(r, 0, 0);
  drawText();
  
  let guessedColor = nn.guess([r, g, b, 255]);
  
  let correctColor = predictColor(r, g, b);
  
  drawPick(correctColor, 50);
  drawPick(guessedColor, 30); 
}

function drawPick(color, size) {
  if (color == 1) {
    fill(255);
  } else if (color == -1) {
    fill(0);
  }
  
  ellipse(width/2, height/2, size);
}

function predictColor(r, g, b) {
  let threshold = 300;

  if (r < 100 && g < 200 && b < 300) {
    return 1; //white
  } else {
    return -1; //black
  }
}

function predictColorTraining(r) {
  let threshold = 200;

  if (r < threshold) {
    return 1; //white
  } else {
    return -1; //black
  }
}

function drawText() {
  textSize(64);
  noStroke();
  fill(0);
  textAlign(CENTER, CENTER);
  text("black", width/2 - width/4, height/2);
  
  fill(255);
  text("white", width/2 + width/4, height/2);
}
