const int IR_SENSOR_PIN = 8;

void setup() {
  Serial.begin(9600);
  pinMode(IR_SENSOR_PIN, INPUT);
}

void loop() {
  int sensorValue = digitalRead(IR_SENSOR_PIN);
  Serial.println(sensorValue);
  delay(1000); // Send data every second
}
