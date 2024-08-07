img = new SimpleImage("img/flores.jpg");
for(pixel: img){
    pixel.setGreen(pixel.getGreen()*0.7)
}
print(img);