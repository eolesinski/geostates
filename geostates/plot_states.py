import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import pandas as pd
import math


def usa_plot(linestyle='solid', cmap=None, extra_regions=False, **kwargs):
    """Plot a choropleth map of the United States.

    Parameters
    ----------

    df : dataframe
       The geodataframe including the column of the value to plot.

    column : str
       Name of the column for the value to plot

    extra_regions : bool, default=False
       Adds Guam and Puerto Rico to the plot.

    labels : string, default 'postal'
       Labels each of the regions on the plot. Options are 'postal',
       'values', and 'both'.
       Postal displays the two letter abbreviations for each of the
       regions on the plot.
       Values displays the numerical values for the target that are
       being plotted (these values are rounded to four decimal
       places).
       Both plots both the two letter abbreviations for each of the
       regions and the target values that are being plotted (these
       values are rounded to four decimal places).

    linestyle : string, default 'dashed'
       Linestyle to place around the inset plots. Options are
       'solid', 'dashed', and 'none'.

    cmap : str, default=None
       Specifies the matplotlib colormap to use.

    legend : bool, default=False
       Adds a legend object to the map.

    Returns
    -------
    A choropleth plot of the United States.

    """

    # import the shape file for the United States
    # df = gpd.read_file('Desktop/cb_2018_us_state_500k/cb_2018_us_state_500k.shp')

    # set the index to the continental states and exclude the ones that we do not want to include
    # df = df.set_index('STUSPS').drop(index=['AS', 'VI', 'MP'])

    # -------------------------------------GENERATE THE PLOT AND INSET PLOTS--------------------------------

    # create the plot figure

    # ax.inset_axes([right/left, up/down, width, hieght])
    fig, continental_states_ax = plt.subplots(figsize=(20, 10))

    # create an axis with four insets
    alaska_ax = continental_states_ax.inset_axes([.08, .012, .20, .28])
    hawaii_ax = continental_states_ax.inset_axes([.28, .014, .15, .19])
    puerto_rico_ax = continental_states_ax.inset_axes([.51, .03, .10, .1])
    guam_ax = continental_states_ax.inset_axes([.612, .03, .10, .15])

    # set the x and y limits for the puerto rico plot
    puerto_rico_ax.set_xlim(-67.5, -65)
    puerto_rico_ax.set_ylim(17.55, 18.95)

    # set the x and y limits for the guam plot
    guam_ax.set_xlim(144.55, 145)
    guam_ax.set_ylim(13.2, 13.7)

    # set the x and y limits for the continental United States plot
    continental_states_ax.set_xlim(-130, -64)
    continental_states_ax.set_ylim(22, 53)

    # set the x and y limits for the alaska plot
    alaska_ax.set_xlim(-180, -127)
    alaska_ax.set_ylim(51, 72)

    # set the x and y limits for the hawaii plot
    hawaii_ax.set_xlim(-160, -154.6)
    hawaii_ax.set_ylim(18.8, 22.5)

    # for loop to remove axis tick marks from graphs
    for ax in [alaska_ax, hawaii_ax, puerto_rico_ax, guam_ax, continental_states_ax]:
        ax.set_yticks([])
        ax.set_xticks([])

    # ----------------------------------------BEGIN SET PARAMETER VALUES--------------------------------

    # parameter for displaying extra regions or not
    if extra_regions == True:
        states_merged_2.loc[['PR']].plot(ax=puerto_rico_ax, cmap='copper_r')
        states_merged_2.loc[['GU']].plot(ax=guam_ax, cmap='copper_r')

    # --------------------------------------CHANGE LINESTYLE--------------------------------------------

    # parameters for changing the linestyle of inset plots

    if linestyle == 'dashed':

        # for loop to change axis lines to dotted lines
        for ax in [alaska_ax, hawaii_ax, puerto_rico_ax, guam_ax]:

            for spine in ['right', 'left', 'top', 'bottom']:
                ax.spines[spine].set_linestyle('--')


    elif linestyle == 'solid':

        # for loop to change axis lines to solid lines
        for ax in [alaska_ax, hawaii_ax, puerto_rico_ax, guam_ax]:

            for spine in ['right', 'left', 'top', 'bottom']:
                ax.spines[spine].set_linestyle('-')


    elif linestyle == 'none':

        # for loop to change axis lines to remove lines
        for ax in [alaska_ax, hawaii_ax, puerto_rico_ax, guam_ax]:
            ax.set_axis_off()

    else:

        raise ValueError('Linestyle must be \'dashed\', \'solid\', or \'none\'')

    # ---------------------------------------ADD LABELS------------------------------------------------

    # -------PRIVATE METHODS-----

    # create a function to compute the x coordinate of the x centroid of a state
    def centroid_x(state_name):

        '''Computes the x value of the centroid of a State's polygon
        Parameters
        ----------
        state_name : the name of the state we would like to get the x centroid value of

        '''

        state = df.loc[state_name]
        centroid_x = round(state['geometry'].centroid.x, 4)
        return centroid_x

    # create a function to compute the y coordinate of the y centroid of a state
    def centroid_y(state_name):

        '''Computes the y value of the centroid of a State's polygon
        Parameters
        ----------
        state_name : the name of the state we would like to get the y centroid value of

        '''
  
        state = df.loc[state_name]
        centroid_y = round(state['geometry'].centroid.y, 4)
        return centroid_y

    # ---------------------------

    # for loop to add state lable annotaitons to the continental plot
    rows = df.index.drop(['AK', 'HI', 'PR', 'GU', 'RI', 'DC', 'DE', 'FL', 'MI', 'LA'])

    for row in rows:
        test = df.loc[row]
        test_centroid_x = round(test['geometry'].centroid.x, 4)
        test_centroid_y = round(test['geometry'].centroid.y, 4)

        continental_states_ax.annotate(test.name, xy=(test['geometry'].centroid.x, test['geometry'].centroid.y),
                                       color='white', ha='center', va='center')

    # create the lable for Rhode Island
    continental_states_ax.annotate('RI', xy=(centroid_x('RI'), centroid_y('RI')), xycoords='data',
                                   xytext=(-69, 39), textcoords='data', arrowprops=dict(arrowstyle='-'))

    # create the label for Deleware
    continental_states_ax.annotate('DE', xy=(centroid_x('DE'), centroid_y('DE')), xycoords='data',
                                   xytext=(-72, 37), textcoords='data', arrowprops=dict(arrowstyle='-', ))

    # create the label for DC
    continental_states_ax.annotate('DC', xy=(centroid_x('DC'), centroid_y('DC')), xycoords='data',
                                   xytext=(-74, 35), textcoords='data', arrowprops=dict(arrowstyle='-'))

    # state label annotation for Alaska inset plots
    ak = df.loc['AK']
    alaska_ax.annotate(ak.name, xy=(centroid_x('AK'), centroid_y('AK')), color='white', ha='center', va='center')

    # state label annotation for Hawaii inset plot
    hi = df.loc['HI']
    hawaii_ax.annotate(hi.name, xy=(centroid_x('HI'), centroid_y('HI')), color='black', ha='center', va='center')

    # state label annotation for Puerto Rick inset plot
    pr = df.loc['PR']
    puerto_rico_ax.annotate(pr.name, xy=(centroid_x('PR'), centroid_y('PR')), color='white', ha='center', va='center')

    # state label annotation for Guam inset plot
    gu = df.loc['GU']
    guam_ax.annotate(gu.name, xy=(centroid_x('GU'), centroid_y('GU')), color='white', ha='center', va='center')

    # ----------------------PLOT THE FIGURE ONCE ALL THE PARAMETER VALUES ARE SPECIFIED----------------

    # plot the continental United States
    vmin, vmax = states_merged_2['ALAND'].agg(['min', 'max'])
    states_merged_2.drop(index=['AK', 'HI', 'PR']).plot(column='admits', cmap='copper_r', ax=continental_states_ax,
                                                        edgecolor='white')

    # plot the inset plots
    states_merged_2.loc[['AK']].plot(column='admits', cmap='copper_r', ax=alaska_ax)
    states_merged_2.loc[['HI']].plot(column='admits', cmap='copper_r', ax=hawaii_ax)

    # return the plot figure
    return continental_states_ax
