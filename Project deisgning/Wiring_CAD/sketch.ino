#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1 // Reset pin # (-1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Serial1.begin(115200);
  
  // Initialize I2C on Pico GP4 (SDA) and GP5 (SCL)
  Wire.setSDA(4);
  Wire.setSCL(5);
  Wire.begin();

  // Initialize the OLED display (address 0x3C is standard for 128x64)
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial1.println(F("SSD1306 allocation failed"));
    for(;;);
  }

  // Clear the buffer
  display.clearDisplay();

  // Configure text properties
  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white pixels
  display.setCursor(0, 0);            // Start at top-left corner
  
  // What you want the screen to say!
  display.println(F("Fallen Air-Mouse"));
  display.println(F("Status: Ready!"));
  display.println(F("Gesture: Active"));
  
  // Push the buffer to the physical screen
  display.display();
}

void loop() {
  // Nothing needed here for a static display message
}