1. What is an RGBA value?

	It is a tuple of 4 integers from range 0 to 255 which corresponds to ammount red, green, blue and alpha	in the color

2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?

	ImageColor.getcolor('CornflowerBlue','RGBA') 

3. What is a box tuple?

	A box tuple is a tuble containing the left edge x co-ordinate, top edge y co-ordinate, the width and height.

4. What function returns an Image object for, say, an image file named zophie.png?

	Image.open('zophie.png')

5. How can you find out the width and height of an Image object’s image?

	imageObj.size

6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?

	imageObj.crop((0,50,50,50))

7. After making changes to an Image object, how could you save it as an image file?

	imgObj.save('filename.png')

8. What module contains Pillow’s shape-drawing code?

	ImageDraw module

9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

	Image objects has shape drawing methods like point(), line(), rectangle(). They are returned by passing the image object to ImageDraw.Draw() function.
	