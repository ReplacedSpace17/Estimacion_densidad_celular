#include <OneWire.h>
#include <DallasTemperature.h>

// Pin al que está conectado el pin de datos del DS18B20
#define ONE_WIRE_BUS 2

// Configuración de OneWire y del sensor de temperatura
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  // Inicializa la comunicación serie
  Serial.begin(9600);
  
  // Inicializa el sensor de temperatura
  sensors.begin();
}

void loop() {
  // Solicita a los sensores que tomen una lectura
  sensors.requestTemperatures();
  
  // Obtiene la temperatura del primer sensor DS18B20 encontrado
  float temperatureC = sensors.getTempCByIndex(0);
  
  // Imprime la temperatura en la consola serie
  Serial.print("Temperatura: ");
  Serial.print(temperatureC);
  Serial.println(" °C");
  
  // Espera 1 segundo antes de la próxima lectura
  delay(1000);
}
