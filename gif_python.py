
import imageio.v3 as iio
file_names = ['C:\\Users\\agamd\\OneDrive\\Documents\\python codedex proj\\gif\\team-pic1.png',
              'C:\\Users\\agamd\\OneDrive\\Documents\\python codedex proj\\gif\\team-pic2.png']
images = []
for filename in file_names:
    images.append(iio.imread(filename))


iio.imwrite('C:\\Users\\agamd\\OneDrive\\Documents\\python codedex proj\\gif\\team.gif',
            images, duration=500, loop=0)
