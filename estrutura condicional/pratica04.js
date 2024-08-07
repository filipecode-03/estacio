img = new SimpleImage("img/calcada.jpg");
for( pixel: img ){
    media=( pixel.getRed()+pixel.getGreen()+pixel.getBlue() ) / 3;
if( pixel.getRed() >media&&pixel.getGreen() > media ){
pixel.setRed( 0 );
pixel.setGreen( 0 );
pixel.setBlue( 0 );
}
}
print( img );
