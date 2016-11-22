/*
 * Button Board Hello World
 * By: Travis Bumgarner
 * Revision: 1.0
 * Date: 8-14-2016
 * 
 * This sketch is for the Button Board V1.1. It will display a message
 * via serial for each button press. 
 */
 
/*
 * s1 through s12 refers to the button name on the board. 
 * Plug in 12 wires from either JP1 or JP2 on the board to Digital pins 2 
 * through 12.
 */
int s1 = 2;
int s2 = 3;
int s3 = 4;
int s4 = 5;
int s5 = 6;
int s6 = 7;
int s7 = 8;
int s8 = 9;
int s9 = 10;
int s10 = 11;
int s11 = 12;
int s12 = 13;
int delayIncrement = 150;
 
void setup() {
    //Each button is declared as an input to the Arduino board.
    pinMode(s1, INPUT);
    pinMode(s2, INPUT);
    pinMode(s3, INPUT);
    pinMode(s4, INPUT);
    pinMode(s5, INPUT);
    pinMode(s6, INPUT);
    pinMode(s7, INPUT);
    pinMode(s8, INPUT);
    pinMode(s9, INPUT);
    pinMode(s10, INPUT);
    pinMode(s11, INPUT);
    pinMode(s12, INPUT);
    Serial.begin(9600);
}
 
void loop() {
    /*
     * If a button is pressed, print a message to the serial monitor 
     * saying that the button is working. Delay for delayIncrement
     * and then wait for another button press.
    */
    if (digitalRead(s1) == HIGH){
            Serial.println("Button S1 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s2) == HIGH){
            Serial.println("Button S2 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s3) == HIGH){
            Serial.println("Button S3 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s4) == HIGH){
            Serial.println("Button S4 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s5) == HIGH){
            Serial.println("Button S5 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s6) == HIGH){
            Serial.println("Button S6 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s7) == HIGH){
            Serial.println("Button S7 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s8) == HIGH){
            Serial.println("Button S8 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s9) == HIGH){
            Serial.println("Button S9 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s10) == HIGH){
            Serial.println("Button S10 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s11) == HIGH){
            Serial.println("Button S11 is working.");
            delay(delayIncrement);
    }
    else if(digitalRead(s12) == HIGH){
            Serial.println("Button S12 is working.");
            delay(delayIncrement);
    }
}
