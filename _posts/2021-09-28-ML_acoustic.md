---
layout: post
title: "Prediction of long-range infrasound amplitudes using machine learning"
description: "Convolutional neural network trained over synthetic data to predict transmission-loss up to 1000 km from a source."
output: html_document
date: 2021-09-28 11:00:00 -0400
category: infrasound
tags: [infrasound, machine-learning, modeling]
comments: false
---

{% highlight r %}
Reference:
[1] Q. Brissaud, S. P. Naesholm, A. Turquet, and A. Le Pichin. Predicting infrasound transmission loss using deep learning. Geophysical Journal International (in review, 2021)
{% endhighlight %}

Modeling the spatial distribution of infrasound attenuation (or transmission loss,TL) from surface sources is key to understanding and interpreting observations atground-based stations. Such predictions enable the reliable assessment of infrasoundsource characteristics such as ground pressure levels associated with earthquakes,volcanic explosion properties, yield of nuclear and non-nuclear explosions, and ocean-generated microbaroms wavefields. However, the computational cost associated withcurrent full-waveform modeling tools, such as Parabolic Equation (PE) codes, oftenprevents the exploration of a large parameter space, i.e., variations in wind models,source frequency, and source location, when deriving reliable estimates of source oratmospheric properties — in particular for real-time and near-real-time applications.Therefore, many studies rely on analytical regression heuristic TL equations thatneglect complex vertical wind variations and the range-dependent variation in theatmospheric properties. This introduces significant uncertainties in the predictedTL.  In this contribution, we propose a deep-learning model trained on a largeset of simulated wavefields generated using PE simulations and ERA5 re-analysisatmospheric models to predict infrasound amplitudes up to 1000 km from the source,also accounting for arbitrarily large vertical and horizontal wind variations. Given an atmospheric model wind and temperature input, our new modeling framework provides a fast (0.05 s runtime) and reliable estimate of the infrasound TL.

![Frequency vs range infrasound tranmission-loss map](/images/map_TL_freq_vs_range.png)

 The map above shows the predicted amplitude at the ground (in db) vs range and frequency. The wind model used for prediction in shown on top. We observe the development of an acoustic shadow zone within 200 km from the source for high frequencies.