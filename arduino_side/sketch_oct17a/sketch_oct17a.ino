int reqCod;
int pin13 = 13;
unsigned char buffer[4];

void setup() {
  Serial.begin(9600);
  pinMode(pin13, OUTPUT);
}

void loop() {

  while (Serial.available() == 0) {

    reqCod = Serial.read();

    if (Serial.readBytes(buffer, sizeof(int)) == sizeof(int)) {
      memcpy(&reqCod, buffer, sizeof(int));
      switch (reqCod)
      {
        case 1:
          //instructions;
        break;
        
    }
  }
}
