# fitters
This library creates fitting functions using ipywidgets.

Here's a simple use example for a Google Colab notebook:

```
!git clone https://github.com/LetsCodePhysics/fitters.git

import sys

sys.path.insert(0, 'fitters/') 

import fitters

x_data = [0,1,2,3]

y_data = [1,2,3,4]

fitters.line_fitter(x_data,y_data)
```

Functions include...

```
 line_fitter(x_data,y_data,

          min_slope=-10,max_slope=10,slope_step=0.1,
          
          min_intercept=-10,max_intercept=10,intercept_step=0.1)
          
quad_fitter(x_data,y_data,

          min_a=-10,max_a=10,a_step=0.1,
          
          min_b=-10,max_b=10,b_step=0.1,
          
          min_c=-10,max_c=10,c_step=0.1)
          
exp_fitter(x_data,y_data,

          min_vertical=-10,max_vertical=10,vertical_step=0.1,
          
          min_horizontal=-10,max_horizontal=10,horizontal_step=0.1,
          
          min_power=-3,max_power=3,power_step=0.1)

power_fitter(x_data,y_data,

          min_power=-10,max_power=10,power_step=0.1,
          
          min_scale=-10,max_scale=10,scale_step=0.1,
          
          min_horizontal=-10,max_horizontal=10,horizontal_step=0.1,
          
          min_vertical=-10,max_vertical=10,vertical_step=0.1)
```

`x_data` and `y_data` are your independent and dependent variable values as a list or array.

Each `min_` argument is the minimum value for that parameter in the slider that is produced.

Each `max_` argument is the maximum value for that parameter in the slider that is produced.

Each `_step` argument is the step size for that parameter in the slider that is produced.

Running each fitter function with your data and no `min_`, `max_`, or `_step` arguments uses the default values and prints the function being fit to your data.
