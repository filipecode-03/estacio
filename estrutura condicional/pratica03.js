img = new SimpleImage("img/calcada.jpg");
for( pixel: img ){
if( pixel.getRed() > 150 && pixel.getGreen() > 150 ){
pixel.setRed( 0 );
pixel.setGreen( 0 );
pixel.setBlue( 0 );
}
}
print( img );