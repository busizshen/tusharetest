#coding=utf-8
from functools import partial
import numpy
from matplotlib import pyplot

# Define a PDF
x_samples = numpy.arange(-3, 3.01, 0.01)
PDF = numpy.empty(x_samples.shape)
PDF[x_samples < 0] = numpy.round(x_samples[x_samples < 0] + 3.5) / 3
PDF[x_samples >= 0] = 0.5 * numpy.cos(numpy.pi * x_samples[x_samples >= 0]) + 0.5
PDF /= numpy.sum(PDF)

# Calculate approximated CDF
CDF = numpy.empty(PDF.shape)
cumulated = 0
for i in range(CDF.shape[0]):
    cumulated += PDF[i]
    CDF[i] = cumulated

# Generate samples
generate = partial(numpy.interp, xp=CDF, fp=x_samples)
u_rv = numpy.random.random(10000)
x = generate(u_rv)

# Visualization
fig, (ax0, ax1) = pyplot.subplots(ncols=2, figsize=(9, 4))
ax0.plot(x_samples, PDF)
ax0.axis([-3.5, 3.5, 0, numpy.max(PDF)*1.1])
ax1.hist(x, 100)
pyplot.show()