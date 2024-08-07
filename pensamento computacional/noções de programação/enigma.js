img = new SimpleImage("img/frutas-5-2-10.jpg");
for(pixel: img){
    pixel.setRed(pixel.getRed()*10);
    pixel.setGreen(pixel.getGreen()*5);
    pixel.setBlue(pixel.getBlue()*2);
}
print(img);