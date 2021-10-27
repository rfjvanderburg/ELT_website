#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Tue Oct 26 21:35:05 2021@author: rvanderbPurpose:    Make image with multiple clickable areas in HTML.    Used for the overview in https://eso.org/wiki/bin/view/ELTScienceInput:    Set two parameters in the script below:        -url which links to image to be used        -pathname of file with link urls to be embedded in imageUse:    For each link, click on the upper left and lower right of rectangular box.    When done clicking, just close the figure and paste the HTML snippet into     the webpage."""# User Input #url = 'http://www.eso.org/~rvanderb/Overview_ELT_working_groups.png'strlinkname = 'links.txt'# Loading packages #import numpy as npimport matplotlib.pyplot as pltimport matplotlib.image as mpimgimport osfrom PIL import Imageimport requestsfrom io import BytesIOfig = plt.figure()ax = fig.add_subplot(111)response = requests.get(url)img = Image.open(BytesIO(response.content))ax.imshow(img)width, height = img.sizeprint(width,height)coords = []def onclick(event):    global ix, iy    ix, iy = event.xdata, event.ydata    print(f'x = {ix}, y = {iy}')    global coords    coords.append((np.int(np.round(ix)), np.int(np.round(iy))))    return coordscid = fig.canvas.mpl_connect('button_press_event', onclick)print("Define the boxes in this order:")os.system('cat '+strlinkname)plt.show()print("")print("HTML snippet:")print(f'<img src="{url}" alt="ELT WG Overview" width="{width}" height="{height}" class="aligncenter size-full wp-image-3344" usemap="#my-image-map"/>') print('<map name="my-image-map">')with open(strlinkname, "r") as a_file:    for i, line in enumerate(a_file):        link = line.split(' ', 1)[0]        description = line.split(' ', 1)[1][0:-1]        print(f'<area target="_blank" alt="{description}" title="{description}" href="{link}" coords="{coords[i*2][0]},{coords[i*2][1]},{coords[i*2+1][0]},{coords[i*2+1][1]}" shape="rect">')print('</map>')