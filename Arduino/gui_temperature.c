// project 7 temperature alarm
// https://www.dfrobot.com/blog-600.html
void setup() {
  Serial.begin(9600);
}

void loop() {
  int val;
  double data;
  val = analogRead(0);  // connect LM35 to analog pin and read value from it
  data = (double)val * (5.0 / 10.24); // Convert the voltage value to temperature value

  Serial.print(data);
  delay(2000);
}
