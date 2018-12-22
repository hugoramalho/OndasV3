
String freq_input = "";
float freq;

void setup() {
  Serial.begin(9600);  // Inicia o Serial Monitor
  pinMode(8, INPUT);//Botão que liga
  

}
void loop() {
 
      //freq_input = Serial.read();
      //freq = freq_input.toFloat();
      
      tone(8,);

      Serial.println(freq);   // Imprime na tela a frequência gerada

}
    
     
  


