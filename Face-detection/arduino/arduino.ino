#define LED_PIN 13  // Or whichever pin you use

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char data = Serial.read();
    if (data == '1') {
      digitalWrite(LED_PIN, HIGH);  // LED ON
    } else if (data == '0') {
      digitalWrite(LED_PIN, LOW);   // LED OFF
    }
  }
}