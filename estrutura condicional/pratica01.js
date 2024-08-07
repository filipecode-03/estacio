img = new SimpleImage("img/RGB.png");
for(pixel: img){
    if(pixel.getRed() == 255){
        pixel.setRed(120);
        pixel.setGreen(120);
        pixel.setBlue(120);
    }
}
print(img);