let black, white;

function setup() {
  createCanvas(1080, 720);
  noLoop();
  
  black = {
    x: width/2 - width/4, 
    y: height/2 - 64,
    text: "black"
  }
  
  white = {
    x: width/2 + width/4,
    y: height/2 - 64,
    text: "white"
  }

  mousePressed();
}

function setRandomBgColor() {
    let r = random(255);
    let g = random(255);
    let b = random(255);
    background(r, g, b);
    
    return {r: r, g: g, b: b};
}

function showInstructions() {
  textSize(64);
  noStroke();
  textAlign(CENTER, CENTER);
  fill(0);
  text(black.text, black.x, black.y);
  fill(255);
  text(white.text, white.x, white.y);
  
  fill(255); 
  strokeWeight(3);
  stroke(0);
  textSize(16);
  textAlign(LEFT, BOTTOM);
  text("press 's' to swap font color; 'enter' to keep", 0, height); 
}

function showPick(foregroundColor) {
  noStroke();
  if (foregroundColor == 0) {
    fill(0);
    ellipse(black.x, black.y + 100, 50);  
  } else {
    fill(255);
    ellipse(white.x, white.y + 100, 50);
  }
}

function predictForegroundColor(r, g, b) {
  //if (r + g + b < 500) {return 255}
  //else {return 0}
}

function mousePressed() {
  let {r, g, b} = setRandomBgColor();
  
  foregroundColor = predictForegroundColor(r, g, b);
  showInstructions();
  showPick(foregroundColor);  

  if (mouseX > width/2) {
    
  }
}



function keyPressed() {
  if (key == "s") {
    
  }
}

function draw() {
  
}
