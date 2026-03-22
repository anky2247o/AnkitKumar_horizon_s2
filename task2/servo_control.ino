include <Servo.h>

Servo myServo;
const int potPin = A0;
const int ledPin = 13;

void setup() {
  myServo.attach(9);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int potValue = analogRead(potPin);
  
  int requestedAngle = map(potValue, 0, 1023, 0, 180);

  if (requestedAngle > 68) {
    myServo.write(68);    //  Limit to 68
    digitalWrite(ledPin, HIGH); // ON
  } else {
    myServo.write(requestedAngle);
    digitalWrite(ledPin, LOW);  
  }
  
}
