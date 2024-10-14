img = new SimpleImage("img/calcada.jpg");
for( pixel: img ){
    media=( pixel.getRed()+pixel.getGreen()+pixel.getBlue() ) / 3;
if( pixel.getRed() > media &&pixel.getGreen() > media ){
pixel.setRed( media );
pixel.setGreen( media );
pixel.setBlue( media );
    }
}
print( img );