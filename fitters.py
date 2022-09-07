import matplotlib.pyplot as plt
import ipywidgets as widgets
import numpy as np

def add_line(x, slope, intercept, ax=None, label=None):
    # This function adds a line to plot ax.
    # Create a figure if one isn't supplied.
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    y = slope * (x - x.min()) + intercept
    ax.plot(x, y, label=label)

def line_data_fit(x_data, y_data, xerr=None, yerr=None, slope=None, intercept=None):
    # This function plots data points and a line.
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    # Increase n_fit_points for smoother plot. 
    # Decrease n_fit_points for faster performance.
    n_fit_points = 20 
    # Create range of x-values for line plot.
    x_in_range = np.linspace(np.min(x_data),np.max(x_data),n_fit_points)
    # Plot data points.
    ax.errorbar(x_data,y_data,xerr=xerr,yerr=yerr,fmt="o")
    # Expand the figure vertically by a smidge.
    smidge = 0.1*(np.max(y_data)-np.min(y_data))
    ax.set_ylim(np.min(y_data)-smidge,np.max(y_data)+smidge)
    # Add line plot.
    add_line(x_in_range, slope, intercept, ax=ax)

def line_fitter(x_data,y_data,xerr=None,yerr=None,
                min_slope=-10,max_slope=10,slope_step=0.1,
                min_intercept=-10,max_intercept=10,intercept_step=0.1):
  if (min_slope<1<max_slope):
    slope_value = 1
  else:
    slope_value = (min_slope+max_slope)/2
  if (min_intercept<1<max_intercept):
    intercept_value = 1
  else:
    intercept_value = (min_intercept+max_intercept)/2
  fitter = widgets.interactive(
      line_data_fit, x_data = widgets.fixed(x_data), y_data = widgets.fixed(y_data),     
      xerr = widgets.fixed(xerr), yerr = widgets.fixed(yerr),
      slope=widgets.FloatSlider(min=min_slope, max=max_slope, step=slope_step, value=slope_value),
      intercept=widgets.FloatSlider(min=min_intercept, max=max_intercept, step=intercept_step, value=intercept_value)
  )
  print('y = slope * x + intercept')
  display(fitter)

def add_quad(x, a, b, c, ax=None, label=None):
    # This function adds a qudratic fit to plot ax.
    # Create a figure if one isn't supplied.
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    y = a * x**2 + b * x + c
    ax.plot(x, y, label=label)

def quad_data_fit(x_data, y_data, a, b, c):
    # This function plots data points and a quadratic fit.
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    # Increase n_fit_points for smoother plot. 
    # Decrease n_fit_points for faster performance.
    n_fit_points = 20 
    # Create range of x-values for fit plot.
    x_in_range = np.linspace(np.min(x_data),np.max(x_data),n_fit_points)
    # Plot data points.
    ax.scatter(x_data,y_data)
    # Expand the figure vertically by a smidge.
    smidge = 0.1*(np.max(y_data)-np.min(y_data))
    ax.set_ylim(np.min(y_data)-smidge,np.max(y_data)+smidge)
    # Add fit plot.
    add_quad(x_in_range, a, b, c, ax=ax)

def quad_fitter(x_data,y_data,
                min_a=-10,max_a=10,a_step=0.1,
                min_b=-10,max_b=10,b_step=0.1,
                min_c=-10,max_c=10,c_step=0.1):

  if (min_a<1<max_a):
    a_value = 1
  else:
    a_value = (min_a+max_a)/2
  if (min_b<1<max_b):
    b_value = 1
  else:
    b_value = (min_b+max_b)/2
  if (min_c<1<max_c):
    c_value = 1
  else:
    c_value = (min_c+max_c)/2
  fitter = widgets.interactive(
      quad_data_fit, x_data = widgets.fixed(x_data), y_data = widgets.fixed(y_data),     
      a=widgets.FloatSlider(min=min_a, max=max_a, step=a_step, value=a_value),
      b=widgets.FloatSlider(min=min_b, max=max_b, step=b_step, value=b_value),
      c=widgets.FloatSlider(min=min_c, max=max_c, step=c_step, value=c_value)
  )
  print('y = a * x**2 + b * x + c')
  display(fitter)

def add_exp(x, vertical, horizontal, power, ax=None, label=None):
    # This function adds an exponential fit to plot ax.
    # Create a figure if one isn't supplied.
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    y = vertical * np.exp(horizontal * x**power)
    ax.plot(x, y, label=label)

def exp_data_fit(x_data, y_data, vertical, horizontal, power):
    # This function plots data points and an exponential fit.
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    # Increase n_fit_points for smoother plot. 
    # Decrease n_fit_points for faster performance.
    n_fit_points = 20 
    # Create range of x-values for fit plot.
    x_in_range = np.linspace(np.min(x_data),np.max(x_data),n_fit_points)
    # Plot data points.
    ax.scatter(x_data,y_data)
    # Expand the figure vertically by a smidge.
    smidge = 0.1*(np.max(y_data)-np.min(y_data))
    ax.set_ylim(np.min(y_data)-smidge,np.max(y_data)+smidge)
    # Add fit plot.
    add_exp(x_in_range, vertical, horizontal, power, ax=ax)

def exp_fitter(x_data,y_data,
                min_vertical=-10,max_vertical=10,vertical_step=0.1,
                min_horizontal=-10,max_horizontal=10,horizontal_step=0.1,
                min_power=-3,max_power=3,power_step=0.1):

  if (min_vertical<1<max_vertical):
    vertical_value = 1
  else:
    vertical_value = (min_vertical+max_vertical)/2
  if (min_horizontal<1<max_horizontal):
    horizontal_value = 1
  else:
    horizontal_value = (min_horizontal+max_horizontal)/2
  if (min_power<1<max_power):
    power_value = 1
  else:
    power_value = (min_power+max_power)/2
  fitter = widgets.interactive(
      exp_data_fit, x_data = widgets.fixed(x_data), y_data = widgets.fixed(y_data),     
      vertical=widgets.FloatSlider(min=min_vertical, max=max_vertical, step=vertical_step, value=vertical_value),
      horizontal=widgets.FloatSlider(min=min_horizontal, max=max_horizontal, step=horizontal_step, value=horizontal_value),
      power=widgets.FloatSlider(min=min_power, max=max_power, step=power_step, value=power_value)
      )
  print('y = vertical * e**(horizontal * x**power)')
  display(fitter)

def add_power(x, power, scale, horizontal, vertical, ax=None, label=None):
    # This function adds a qudratic fit to plot ax.
    # Create a figure if one isn't supplied.
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    y = scale * (x - horizontal)**power + vertical
    ax.plot(x, y, label=label)

def power_data_fit(x_data, y_data, power, scale, horizontal, vertical):
    # This function plots data points and a power-law fit.
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    # Increase n_fit_points for smoother plot. 
    # Decrease n_fit_points for faster performance.
    n_fit_points = 20 
    # Create range of x-values for fit plot.
    x_in_range = np.linspace(np.min(x_data),np.max(x_data),n_fit_points)
    # Plot data points.
    ax.scatter(x_data,y_data)
    # Expand the figure vertically by a smidge.
    smidge = 0.1*(np.max(y_data)-np.min(y_data))
    ax.set_ylim(np.min(y_data)-smidge,np.max(y_data)+smidge)
    # Add fit plot.
    add_power(x_in_range, power, scale, horizontal, vertical, ax=ax)

def power_fitter(x_data,y_data,
                min_power=-10,max_power=10,power_step=0.1,
                min_scale=-10,max_scale=10,scale_step=0.1,
                min_horizontal=-10,max_horizontal=10,horizontal_step=0.1,
                min_vertical=-10,max_vertical=10,vertical_step=0.1):

  if (min_power<1<max_power):
    power_value = 1
  else:
    power_value = (min_power+max_power)/2
  if (min_scale<1<max_scale):
    scale_value = 1
  else:
    scale_value = (min_scale+max_scale)/2
  if (min_horizontal<1<max_horizontal):
    horizontal_value = 0
  else:
    horizontal_value = (min_horizontal+max_horizontal)/2
  if (min_vertical<1<max_vertical):
    vertical_value = 0
  else:
    vertical_value = (min_vertical+max_vertical)/2
  fitter = widgets.interactive(
      power_data_fit, x_data = widgets.fixed(x_data), y_data = widgets.fixed(y_data),     
      power=widgets.FloatSlider(min=min_power, max=max_power, step=power_step, value=power_value),
      scale=widgets.FloatSlider(min=min_scale, max=max_scale, step=scale_step, value=scale_value),
      horizontal=widgets.FloatSlider(min=min_horizontal, max=max_horizontal, step=horizontal_step, value=horizontal_value),
      vertical=widgets.FloatSlider(min=min_vertical, max=max_vertical, step=vertical_step, value=vertical_value)
  )
  print('scale * (x - horizontal)**power + vertical')
  display(fitter)

if __name__ == "__main__":
    main()
