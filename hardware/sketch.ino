#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

// Definição de pinos
#define PINO_DHT    2
#define TIPO_DHT    DHT22

// Pinos para os 3 sensores LDR (fotoresistores).
// No futuro, estes pinos poderiam ser usados para um acelerômetro.
#define PINO_SENSOR_X   34 // LDR 1, representando o eixo X
#define PINO_SENSOR_Y   32 // LDR 2, representando o eixo Y
#define PINO_SENSOR_Z   35 // LDR 3, representando o eixo Z

// Intervalo de leitura em milissegundos (10 segundos)
const unsigned long intervaloLeitura = 10000;
unsigned long ultimoTempo = 0;

// Objeto para o DHT22
DHT dht(PINO_DHT, TIPO_DHT);

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // Espera o Serial "encaixar" antes de prosseguir
  }
  dht.begin();   // Inicializa o DHT22

  Serial.println("Monitor de Sensores Iniciado.");
  Serial.println("Aguardando a primeira leitura...");
}

void loop() {
  unsigned long agora = millis();
  if (agora - ultimoTempo >= intervaloLeitura) {
    ultimoTempo = agora;

    // 1) Leitura DHT22: temperatura (°C) e umidade (%)
    float tempC = dht.readTemperature();
    float hum   = dht.readHumidity();

    // Se der erro na leitura (NaN), usa um valor de erro
    if (isnan(tempC)) {
      tempC = -999.0;
    }
    if (isnan(hum)) {
      hum = -999.0;
    }

    // 2) Leitura dos 3 sensores analógicos (LDRs neste caso)
    // Os valores serão o ADC bruto (0 a 4095)
    int valorX = analogRead(PINO_SENSOR_X);
    int valorY = analogRead(PINO_SENSOR_Y);
    int valorZ = analogRead(PINO_SENSOR_Z);
    
    // 3) Imprime os dados de forma organizada no Monitor Serial
    Serial.println("--- Nova Leitura ---");

    // Imprime umidade
    Serial.print("Umidade:     ");
    if (hum == -999.0) {
      Serial.println("Erro de leitura");
    } else {
      Serial.print(hum, 1); // Imprime com 1 casa decimal
      Serial.println(" %");
    }

    // Imprime temperatura
    Serial.print("Temperatura: ");
    if (tempC == -999.0) {
      Serial.println("Erro de leitura");
    } else {
      Serial.print(tempC, 1); // Imprime com 1 casa decimal
      Serial.println(" *C");
    }
    
    // Imprime os valores dos LDRs rotulados como "Vibração"
    Serial.print("Vibracao X:  ");
    Serial.println(valorX);

    Serial.print("Vibracao Y:  ");
    Serial.println(valorY);

    Serial.print("Vibracao Z:  ");
    Serial.println(valorZ);
    
    Serial.println("----------------------\n"); // Adiciona uma linha em branco para separar
  }
}