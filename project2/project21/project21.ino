int red_led=12;
int green_led=11;
int buzz=13;
int gas_value;
int gas_avalue;
int sensorThres=400;


void setup()
{
pinMode(red_led,OUTPUT);
pinMode(buzz,OUTPUT);
pinMode(green_led,OUTPUT);
pinMode(A1,INPUT);
Serial.begin(9600);
}




void loop()
{
gas_avalue=analogRead(A0);
if (A0 > sensorThres)
{
digitalWrite(red_led, HIGH);
digitalWrite(green_led, LOW);
digitalWrite( buzz, HIGH);
Serial.println("danger");
//Serial.println(“DANGER!!!!”);
Serial.println(gas_avalue);
}
else
{
digitalWrite(red_led, LOW);
digitalWrite(green_led, HIGH);
digitalWrite( buzz, LOW);
Serial.println("no danger");
//Serial.println(“NO LEAKAGE”);
Serial.println(gas_avalue);
}
delay(1000);
}
