/* ProcessingTestDriver
 * gratefulfrog
 * 2018 05 11
 *
 */

///////////////////// USER PARAMETERS /////////////////////////////

final int baudRate = 115200;
final String portName = "/dev/ttyACM0";

///////////////////// END of USER PARAMETERS /////////////////////////////

import processing.serial.*;
import java.util.*;

Serial commsPort;

final boolean autoExec = true;
final int autoExecPause = 1500; // milliseconds
int lastExecTime = 0;

final int maxRecDelay = 15000; // 15 seconds
int lastRecTime = 0;

final color bg = 0,
            fg = 255;
final char contactChar = '|',  // confirms arduin handshake
           pollChar    = 'p',
           execChar    = 'x';

final String startupMsg = "starting...",
             nbFormat   = "%4d : ",
             recMsg     = "Received : ",
             sendMsg    = "Sent : ";
 
final int XYValuesLength = 16,
          spiBitsLength  = 256,
          outMsgLength   = XYValuesLength + spiBitsLength,
          inMsgLength    = 2*XYValuesLength + spiBitsLength;

String outXBits   = "",
       outSPIBits = "";
int outXBitsIndex = 0,
    outSPIBitsIndex = 0;

int inCount=0,
    outCount=0;
boolean messageArrived = false; 
String incoming = "";

Gui gui;

void initOutBits(){
  outXBits = "";
  outSPIBits="";
  for(int i=0;i<XYValuesLength;i++){
    outXBits+="0";
  }
  for(int i=0;i<spiBitsLength;i++){
    outSPIBits+="0";
  }
  outXBitsIndex = 0;
  outSPIBitsIndex=0;
}

void setup() {
  //fullScreen();
  size(1000, 800); 
  initOutBits();
  commsPort = new Serial(this, portName, baudRate);
  fill(fg);
  background(bg);
  gui = new Gui();  
}

void processIncoming () {
  gui.matrixDisplay(incoming);  // do stuff here!
}
void showBitsAsString(String bits, int size){
  for(int i=0;i<bits.length(); i+=size){
    println(String.format(nbFormat,i) + bits.substring(i,i+XYValuesLength));
  }
}

void receiveFromComms(String s, boolean countIt, int size){
   String displayMsg = (countIt 
                       ? String.format(nbFormat, inCount++) 
                       : "") 
                       + recMsg;
   println(displayMsg);
   showBitsAsString(s, size);
 }

// When we want to print to the window
void ShowIncoming() {
  receiveFromComms(incoming,true,XYValuesLength);
}

void send2Comms(char c, boolean countIt){
  String displayMsg = (countIt 
                       ? String.format(nbFormat, outCount++) 
                       : "") 
                       + sendMsg + String.valueOf(c);
  println(displayMsg);
  commsPort.write(c);
}
 
void send2Comms(String s, boolean countIt, int size){
  String displayMsg = (countIt ? String.format(nbFormat, outCount++) : "") + sendMsg + s.substring(0,1);
  println(displayMsg);
  //showBitsAsString(s.substring(1,s.length()),size);
  commsPort.write(s);
}

char notChar(char c){
  return c== '0' ? '1' : '0';
}


boolean timeToPoll(){
  if (((millis() - lastRecTime) > maxRecDelay) ||
      (millis() < lastRecTime)){
      return true;
      }
  return false;
}

void poll(){
  send2Comms(pollChar,true);
}

boolean timeToExec(){
  if (((millis() - lastExecTime) > autoExecPause) ||
      (millis() < lastExecTime)){
      return true;
      }
  return false;
}

void exec(){  
  send2Comms(execChar+outXBits+outSPIBits,true,XYValuesLength);
  // now inc outbits
  String newBits = "";
  for(int i=0;i<XYValuesLength;i++){
    newBits+= (i==outXBitsIndex ? notChar(outXBits.charAt(i)) : outXBits.charAt(i)); 
  }
  outXBitsIndex = (outXBitsIndex+1) % XYValuesLength;
  outXBits = newBits;
  newBits = "";
  for(int i=0;i<spiBitsLength;i++){
    newBits+= (i==outSPIBitsIndex ? notChar(outSPIBits.charAt(i)) : outSPIBits.charAt(i)); 
  }
  outSPIBitsIndex = (outSPIBitsIndex+1) % spiBitsLength;
  outSPIBits = newBits;
  lastExecTime = millis();
}

void draw() {
  if (messageArrived) {
    background(bg);
    processIncoming();
    //ShowIncoming();
    messageArrived= false;
    incoming = "";
  }
  if (timeToPoll()){
    poll();
  }
  if (autoExec && timeToExec()){
    exec();
  }
  //gui.display();
 }
 
void serialEvent(Serial commsPort) {
  char inChar = commsPort.readChar();
  if (inChar == contactChar) {
    send2Comms(contactChar, false);
    println(startupMsg);
  }
  else if (!messageArrived){
    incoming += inChar;
    if (incoming.length() == inMsgLength)
      messageArrived = true;
      lastRecTime = millis();
  }
}

void connectionsAllOff(){
  outSPIBits="";
  for(int i=0;i<spiBitsLength;i++){
    outSPIBits+="0";
  }
  outSPIBitsIndex=0;
}
void connectionsAllOn(){
  outSPIBits="";
  for(int i=0;i<spiBitsLength;i++){
    outSPIBits+="1";
  }
  outSPIBitsIndex=0;
}
void mouseClicked(){
  if (mouseButton == LEFT) {
    connectionsAllOn();
  }
  else{
     connectionsAllOff();
  } 
}