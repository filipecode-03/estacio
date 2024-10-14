img = new SimpleImage("img/circulo.bmp");
img.setZoom(20);
pixel = img.getPixel(4, 0);
pixel.setRed(0);
pixel.setGreen(255);
pixel.setBlue(0);
print(img);