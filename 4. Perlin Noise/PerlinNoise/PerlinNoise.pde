// Typically we would start at time = 0, though this is arbitrary.
float t = 0;

void setup()
{
  size (600,400);
  frameRate(100);
}

void draw() {
  background(0);
  fill (255);
  
  t=t+0.01;
  
  float z = random(width);
  float x = noise (t);
  float y = noise (t+50);
  y = map(y,0,1,0, height);
  x = map (x,0,1,0,width);
  ellipse(x,y,40,40);
}
