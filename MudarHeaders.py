# Import the astropy fits tools
from astropy.io import fits

# Open the file header for viewing and load the header
for i in range(1,10):
	# ~ hdulist = fits.open('/home/luis/Desktop/ImagensFits/Flats/FLATR_00' + str(i) + '.fits')
	# ~ header = hdulist[0].header
	# ~ header.set('EPOCH',2000.0,'Valor Mudado')
	# ~ hdulist.writeto('/home/luis/Desktop/ImagensFits/FlatsNovos/Flat' + str(i) + '.fits')
	# ~ hdulist.close()
	
	hdulist = fits.open('/home/luis/Desktop/ImagensFits/Darks/DARK100_00' + str(i) + '.fits')
	header = hdulist[0].header
	header.set('EPOCH',2000.0,'Valor Mudado')
	hdulist.writeto('/home/luis/Desktop/ImagensFits/DarksNovos/Dark' + str(i) + '.fits')
	hdulist.close()
	







# ~ # Print the header keys from the file to the terminal
# ~ print(header.keys)

# ~ # Modify the key called 'NAXIS1' to have a value of 100
# ~ header['NAXIS1'] = '100'

# ~ # Modify the key called 'NAXIS1' and give it a comment
# ~ header['NAXIS1'] = ('100','This value has been modified!')
