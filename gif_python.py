
import imageio.v3 as iio
file_names = ['team-pic1.png',
              'team-pic2.png']
images = []
for filename in file_names:
    images.append(iio.imread(filename))


iio.imwrite('team.gif', images, duration=500, loop=0)

