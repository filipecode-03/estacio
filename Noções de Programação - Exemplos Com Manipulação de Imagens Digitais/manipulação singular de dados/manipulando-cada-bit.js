img = new SimpleImage("img/circulo.bmp");
img.setZoom(20);
pixel = img.getPixel(4, 4);
pixel.setRed(255);
print(img);