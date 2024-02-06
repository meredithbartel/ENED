# Python Lists Additional Example
# File: Example_Additional.py 
# Date:    02 January 2024
# By:      Gregory Bucks
# Section: XXX
# Team:    XXX
# 
# ELECTRONIC SIGNATURE
# Gregory Bucks
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script computes the RMS average value for a set of
# voltage values defined in the 2-D List V.  Each row in
# V corresponds to a set of 100 voltage measurements.

# import libraries
import math

# create voltage data
V = [[88.287,29.871,59.71,89.398,57.41,88.797,47.671,94.144,40.749,49.12,65.425,13.865,97.395,98.904,34.528,42.71,8.636,2.737,73.064,64.652,9.602,0.445,38.267,34.113,88.976,48.812,57.929,80.87,21.404,98.596,66.823,88.895,67.998,55.612,76.151,27.807,87.158,74.561,58.944,78.444,41.738,75.752,64.252,2.476,99.582,5.431,51.453,4.969,0.318,59.119,13.575,1.748,94.385,32.499,48.959,15.012,34.672,53.506,55.484,88.307,84.463,88.087,82.699,81.955,3.379,32.67,87.065,94.015,78.628,67.637,17.505,96.777,29.653,23.631,14.721,74.782,38.93,0.929,68.029,11.008,65.885,65.655,20.492,59.008,32.664,85.948,95.518,20.105,2.447,4.882,94.106,56.079,19.241,37.198,7.271,21.031,52.621,72.675,71.583,50.918],[51.189,0.59,54.338,95.072,46.637,63.877,87.782,26.819,23.345,61.647,19.347,32.824,23.79,56.256,9.161,58.886,4.081,4.97,98.096,17.67,19.939,19.861,97.72,84.94,49.069,86.113,62.898,6.667,16.695,21.275,72.822,86.412,65.488,61.129,66.704,40.963,14.272,9.798,61.157,44.635,27.317,79.191,95.692,2.227,55.445,26.821,88.84,67.021,51.008,68.792,51.152,78.852,79.933,74.835,60.628,64.659,55.204,91.452,98.128,12.192,22.876,23.748,39.168,68.102,85.945,91.44,97.23,93.312,60.141,72.507,76.417,63.414,31.22,99.434,30.486,97.001,88.168,19.833,85.852,34.378,11.918,27.744,61.879,0.229,32.515,71.318,62.775,4.286,3.978,81.204,66.156,0.109,56.748,70.761,44.028,68.364,79.692,88.633,48.865,80.413],[37.62,22.865,12.977,46.236,37.404,1.095,38.988,74.54,53.531,12.278,9.46,34.644,10.858,49.589,63.16,9.17,75.156,23.855,58.821,87.648,60.705,43.872,93.608,18.623,31.351,71.646,48.193,19.586,64.613,91.899,28.564,69.759,41.181,73.883,97.811,62.681,20.06,89.027,84.317,91.191,31.471,38.588,18.634,79.852,65.609,54.601,17.43,97.662,14.446,16.644,4.143,54.079,43.773,47.647,71.769,58.378,55.844,64.566,16.286,29.026,42.837,93.969,62.135,33.006,52.856,49.456,11.698,98.376,94.701,68.579,45.933,77.726,54.97,90.93,77.987,69.514,89.327,2.068,87.179,26.407,12.922,70.913,69.915,94.453,40.017,57.501,81.913,63.916,52.982,3.259,21.49,12.686,65.767,34.566,60.653,15.439,27.368,5.193,7.807,50.983],[88.376,67.012,55.222,28.76,75.462,97.726,4.916,90.907,31.161,13.303,91.836,92.876,80.003,25.304,37.819,25.058,32.376,12.73,50.316,25.169,70.971,55.829,89.274,20.874,76.214,62.033,16.053,97.478,18.034,66.516,59.369,88.499,47.637,25.692,11.707,91.91,62.093,8.209,45.699,8.659,58.17,31.805,90.952,10.781,94.535,77.519,82.007,22.027,50.465,65.223,31.241,4.548,9.031,51.559,14.002,31.233,6.681,15.347,15.66,6.234,36.829,2.715,96.515,3.469,97.546,71.024,50.831,69.304,63.122,79.672,60.606,89.85,55.258,79.079,48.723,27.327,38.6,79.227,89.706,58.018,7.797,13.03,31.483,79.248,76.351,74.114,18.897,25.176,93.337,41.504,91.359,21.464,68.558,87.716,30.478,97.432,29.268,7.856,53.007,30.27],[24.576,98.167,14.906,92.637,45.56,38.553,30.743,58.455,70.863,31.418,55.824,88.832,4.481,19.596,88.736,59.377,6.649,63.033,53.159,35.648,89.053,38.513,44.353,53.043,95.453,8.977,75.438,57.509,11.655,74.348,37.053,46.564,38.827,72.626,86.932,41.515,77.503,78.152,88.279,99.894,68.936,48.093,56.874,68.881,22.464,60.376,18.119,8.406,56.821,76.864,32.177,51.385,93.357,48.009,58.305,67.214,58.194,5.218,16.367,14.353,69.605,56.151,82.847,12.019,87.722,66.464,75.557,70.248,87.884,52.963,36.404,22.657,64.04,13.515,54.917,95.114,72.755,19.083,84.359,43.539,73.524,52.4,80.479,39.933,16.407,75.367,75.148,41.988,60.221,59.467,38.02,82.682,35.374,75.053,40.664,50.266,34.815,1.449,66.605,86.193],[16.4,25.615,25.855,49.633,70.603,39.966,32.021,90.65,58.706,8.786,41.764,79.004,95.996,49.273,42.653,52.058,92.326,47.641,60.629,30.335,60.264,64.686,75.153,8.429,64.588,11.176,79.35,58.321,36.533,37.846,79.564,37.156,45.206,71.325,56.786,71.15,24.681,84.868,49.357,72.758,86.387,27.851,19.352,77.503,98.152,31.61,9.726,35.886,64.217,39.577,94.832,44.562,37.838,42.402,19.5,39.706,47.586,1.505,7.849,6.797,94.438,89.045,81.34,28.371,16.134,83.178,10.999,37.131,12.269,75.464,40.195,10.127,59.665,55.034,87.822,90.767,91.265,95.208,48.515,41.51,55.615,4.589,17.802,87.345,68.829,55.509,22.158,17.184,60.118,19.68,3.498,38.761,95.679,43.443,10.101,89.141,87.597,19.334,60.771,5.739],[65.86,61.917,52.871,87.733,92.951,51.029,46.13,5.668,23.919,40.879,11.045,7.447,80.164,71.088,89.077,91.405,5.436,11,76.432,96.776,86.245,58.567,90.94,24.077,48.532,57.559,29.137,95.002,40.238,47.477,7.353,8.302,2.676,50.376,12.015,97.087,36.945,45.088,62.285,55.841,21.086,15.804,70.424,79.149,17.062,43.335,3.131,73.318,20.693,39.626,20.734,49.136,75.892,17.602,6.334,21.952,66.194,19.636,71.84,18.509,21.789,16.699,95.509,83.824,35.338,25.804,3.386,6.411,81.355,50.355,73.007,82.826,16.117,5.384,98.829,45.742,90.413,77.023,48.854,5.421,83.437,10.131,24.131,67.44,64.332,80.091,41.645,88.446,64.387,79.609,22.735,31.808,24.374,40.066,47.688,72.649,9.332,2.629,41.955,73.076],[25.562,97.183,81.338,21.324,82.047,55.163,48.813,55.674,6.406,28.232,55.274,41.98,96.06,98.762,22.423,66.329,6.794,43.543,60.062,19.229,67.596,76.633,37.332,63.455,43.818,46.166,50.761,10.004,8.981,10.626,99.274,99.722,42.529,89.277,97.033,43.547,34.11,60.533,56.217,14.282,50.675,39.541,65.158,70.947,94.106,84.278,1.018,60.214,34.019,69.212,48.934,65.989,80.379,28.056,6.39,24.082,78.61,52.771,44.627,76.868,75.3,42.524,18.312,90.135,5.801,76.924,44.11,44.345,97.76,90.704,95.513,42.447,41.791,67.655,1.915,73.317,8.145,81.657,6.533,25.97,10.612,46.894,59.473,24.237,82.135,67.035,79.087,34.101,92.193,21.099,90.689,26.178,74.827,37.294,29.241,49.718,20.668,46.877,11.08,90.088],[15.76,49.217,71.853,11.44,3.985,95.889,70.674,0.296,0.337,63.059,11.128,39.672,76.575,33.462,79.693,49.965,57.353,90.188,72.259,9.786,78.5,17.463,11.629,11.108,18.638,54.545,23.799,87.873,68.377,88.378,77.603,86.983,10.581,77.939,83.997,63.538,45.639,35.447,72.166,83.764,42.505,28.546,33.19,94.654,95.696,62.613,96.745,45.137,32.747,23.767,44.468,50.537,80.424,87.767,93.987,38.638,19.003,14.767,51.012,89.768,51.984,32.69,67.043,44.995,44.412,41.057,12.978,54.299,23.124,12.361,87.88,72.71,36.906,82.228,35.132,55.824,3.334,42.605,45.698,24.418,25.656,71.065,86.823,16.844,37.855,53.511,39.996,20.512,21.926,17.441,86.899,29.652,39.023,44.325,1.628,60.721,30.276,24.338,81.661,46.404],[27.661,30.103,50.082,12.432,96.619,85.54,36.73,15.316,18.907,21.976,23.602,41.293,60.823,22.017,85.828,63.48,43.92,56.583,43.521,69.379,53.665,50.311,52.512,60.734,44.313,3.801,19.268,89.145,54.689,44.51,0.737,0.007,4.311,49.486,6.232,90.156,17.082,75.91,54.677,72.525,23.97,24.305,52.157,29.802,17.501,27.255,88.804,91.28,61.496,94.888,82.085,74.186,59.579,87.386,52.018,3.35,96.151,7.313,60.514,51.827,76.007,56.759,73.56,98.854,44.109,5.566,97.16,54.016,91.274,85.223,60.973,93.675,8.026,91.14,53.465,99.389,57.241,30.022,59.556,70.91,5.412,60.135,81.867,86.112,11.19,68.593,4.511,79.539,88.49,61.384,58.247,42.818,84.476,38.031,88.442,34.929,35.152,91.992,24.93,46.936]]

# create RMS List to store values for each set of voltages
V_RMS = [0,0,0,0,0,0,0,0,0,0]

# calculate RMS values for each dataset
for R in range(10):
    Sum = 0
    for C in range(100):
        Sum = Sum + V[R][C]**2
    V_RMS[R] = math.sqrt(Sum/100)

# calculate average of RMS values
Sum = 0
for k in range(10):
    Sum = Sum + V_RMS[k]

# display average RMS value
print('Average V_RMS value = {0:0.2f}V'.format(Sum/10))