preferrredlanguage.py
Customization
import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.4,4.5,6.5,7.2]
plt.plot(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('world population')
plt.yticks([2,4,6,8,10])
plt.show()

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/usr/lib/python3/dist-packages/IPython/core/formatters.py in __call__(self, obj)
    332                 pass
    333             else:
--> 334                 return printer(obj)
    335             # Finally look for special method names
    336             method = get_real_method(obj, self.print_method)

/usr/lib/python3/dist-packages/IPython/core/pylabtools.py in <lambda>(fig)
    245 
    246     if 'png' in formats:
--> 247         png_formatter.for_type(Figure, lambda fig: print_figure(fig, 'png', **kwargs))
    248     if 'retina' in formats or 'png2x' in formats:
    249         png_formatter.for_type(Figure, lambda fig: retina_figure(fig, **kwargs))

/usr/lib/python3/dist-packages/IPython/core/pylabtools.py in print_figure(fig, fmt, bbox_inches, **kwargs)
    129 
    130     bytes_io = BytesIO()
--> 131     fig.canvas.print_figure(bytes_io, **kw)
    132     data = bytes_io.getvalue()
    133     if fmt == 'svg':

/usr/lib/python3/dist-packages/matplotlib/backend_bases.py in print_figure(self, filename, dpi, facecolor, edgecolor, orientation, format, bbox_inches, **kwargs)
   2073                     orientation=orientation,
   2074                     bbox_inches_restore=_bbox_inches_restore,
-> 2075                     **kwargs)
   2076             finally:
   2077                 if bbox_inches and restore_bbox:

/usr/lib/python3/dist-packages/matplotlib/backends/backend_agg.py in print_png(self, filename_or_obj, *args, **kwargs)
    508 
    509         """
--> 510         FigureCanvasAgg.draw(self)
    511         renderer = self.get_renderer()
    512 

/usr/lib/python3/dist-packages/matplotlib/backends/backend_agg.py in draw(self)
    394         Draw the figure using the renderer.
    395         """
--> 396         self.renderer = self.get_renderer(cleared=True)
    397         # acquire a lock on the shared font cache
    398         RendererAgg.lock.acquire()

/usr/lib/python3/dist-packages/matplotlib/backends/backend_agg.py in get_renderer(self, cleared)
    415 
    416         if need_new_renderer:
--> 417             self.renderer = RendererAgg(w, h, self.figure.dpi)
    418             self._lastKey = key
    419         elif cleared:

/usr/lib/python3/dist-packages/matplotlib/backends/backend_agg.py in __init__(self, width, height, dpi)
     85         self.width = width
     86         self.height = height
---> 87         self._renderer = _RendererAgg(int(width), int(height), dpi)
     88         self._filter_renderers = []
     89 

ValueError: Image size of 1908425x17434 pixels is too large. It must be less than 2^16 in each direction.
<Figure size 432x288 with 1 Axes>
Pandas
dict1={
    "country":['brazil','india','russia','china','south africa'],
    "capital":['brazilia','new delhi','moscow','beijing','pretoria'],
    "area":[7.5,4.6,3.5,5.6,8.4],
    "population":[200,300,130,500,399]
}
import pandas as pd
brics=pd.DataFrame(dict1)
print(brics)
print()
brics.index=['br','in','ru','ch','sa']
print(brics)
        country    capital  area  population
0        brazil   brazilia   7.5         200
1         india  new delhi   4.6         300
2        russia     moscow   3.5         130
3         china    beijing   5.6         500
4  south africa   pretoria   8.4         399

         country    capital  area  population
br        brazil   brazilia   7.5         200
in         india  new delhi   4.6         300
ru        russia     moscow   3.5         130
ch         china    beijing   5.6         500
sa  south africa   pretoria   8.4         399
#read csv file
#brics=pd.read_csv("path/to/file.csv",index_col=0)
print(brics['country'])
#panda series
br          brazil
in           india
ru          russia
ch           china
sa    south africa
Name: country, dtype: object
print(brics[['country']])
#panda dataframe
         country
br        brazil
in         india
ru        russia
ch         china
sa  south africa
print(brics[1:4])

