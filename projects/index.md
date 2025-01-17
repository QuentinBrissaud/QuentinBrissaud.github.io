---
layout: splash
title: Portfolio
tags: [portfolio]
comments: false
intro: 
  - excerpt: 'My work includes Machine Learning applications for geophysics, seismic and acoustic event monitoring, and planetary exploration'
feature_row_ML:
  - image_path: images/ML_Ukraine.jpg
    image_caption: "Example of wave detection and classification on a seismometer in Ukraine"
    alt: "Example of wave detection and classification on a seismometer in Ukraine"
    title: "2023: Conflict monitoring using seismic timeseries segmentation"
    excerpt: "We developed model to detect and pick seismic and sound signals from explosions during the Ukraine-Russia war by training a CNN autoencoder with self-attention."
    url: "https://quentinbrissaud.github.io/infrasound/Ukraine_Sandia/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: images/map_TL_freq_vs_range.png
    image_caption: "Sound amplitude prediction vs range and frequency"
    alt: "Sound amplitude prediction vs range and frequency"
    title: "2022: Predicting sound amplitude with deep learning"
    excerpt: "We trained a deep CNN to compute the sound amplitudes from explosions by mapping atmospheric winds sound attenuation at ground level."
    url: "https://quentinbrissaud.github.io/infrasound/ML_acoustic/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: images/iono_map_event_Iquique_30s.png
    image_caption: "Detected earthquake wave arrival times in a satellite network"
    alt: "Detected earthquake wave arrival times in a satellite network"
    title: "2021: Detection of earthquakes from satellite data using machine learning"
    excerpt: "We built an automatic detector and arrival time picker of large earthquake signals in GNSS satellite data using Ranfom Forests."
    url: "https://quentinbrissaud.github.io/ionosphere/ML_TEC/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row_event:
  - image_path: images/kiruna_schematic_3d.png
    image_caption: "3D mine diagram and the acoustic array location (label A), our seismic solution (label B), and locations of main source types from (Dineva et al., 2022)"
    alt: "3D mine diagram"
    title: "2023: Seismic and acoustic analysis of the largest minequake in the Nordics"
    excerpt: "We were able to retrieve seismic source parameters from the sound signature of a large minequake."
    url: "https://quentinbrissaud.github.io/infrasound/Kiruna_preprint/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: images/Ukraine_detection.png
    image_caption: "An unreported explosion northeast of Malyn detected by our model."
    alt: "An unreported explosion northeast of Malyn detected by our model."
    title: "2023: Seismic monitoring of the Ukraine-Russia war"
    excerpt: "We developed a model to perform seismic and infrasound monitoring of the 2022 Russia-Ukraine war in real time."
    url: "https://quentinbrissaud.github.io/infrasound/Ukraine_Nature/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: images/Hunga_map_cropped.jpg
    image_caption: "Map of the seismo-acoustic and satellite detectections of the 2022 Hunga eruption."
    alt: "Map of the seismo-acoustic and satellite detectections of the 2022 Hunga eruption."
    title: "2023: Atmospheric waves and global seismoacoustic observations of the January 2022 Hunga eruption, Tonga"
    excerpt: "We analyzed the seismic, acoustic, and satellite data after the 2022 Hunga eruption, the largest volcanic eruption in recorded history."
    url: "https://quentinbrissaud.github.io/volcano/Hunga_Science/"
    btn_label: "Read More"
    btn_class: "btn--primary"
---

{% assign feature_row = page.intro %}
{% assign type = "center" %}
<div class="feature__wrapper">

  {% for f in feature_row %}
    <div class="feature__item{% if type %}--{{ type }}{% endif %}">
      <div class="archive__item">
          {% if f.excerpt %}
            <div class="archive__item-excerpt">
              {{ f.excerpt | markdownify }}
            </div>
          {% endif %}
        </div>
      </div>
    </div>
  {% endfor %}

## Machine learning
{% assign feature_row = page.feature_row_ML %}
{% assign type = "" %}
<div class="feature__wrapper">
{% for f in feature_row %}
  <div class="feature__item">
    <div class="feature__item{% if type %}--{{ type }}{% endif %}">
      {% if f.image_path %}
        <div class="archive__item-teaser">
          <img src="{{ f.image_path | relative_url }}" alt="{% if f.alt %}{{ f.alt }}{% endif %}" width="100." />
          {% if f.image_caption %}
            <span class="archive__item-caption">{{ f.image_caption | remove: "<p>" | remove: "</p>" }}</span>
          {% endif %}
        </div>
      {% endif %}

      <div class="archive__item-body">
        {% if f.title %}
          <h4 class="archive__item-title">{{ f.title }}</h4>
        {% endif %}

        {% if f.excerpt %}
          <div class="archive__item-excerpt">
            {{ f.excerpt | markdownify }}
          </div>
        {% endif %}

        {% if f.url %}
          <p><a href="{{ f.url | relative_url }}" class="btn {{ f.btn_class }}">{{ f.btn_label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a></p>
        {% endif %}
      </div>
    </div>
  </div>
{% endfor %}

</div>

## Event monitoring
{% assign feature_row = page.feature_row_event %}
{% assign type = "" %}
<div class="feature__wrapper">
{% for f in feature_row %}
  <div class="feature__item">
    <div class="feature__item{% if type %}--{{ type }}{% endif %}">
      {% if f.image_path %}
        <div class="archive__item-teaser">
          <img src="{{ f.image_path | relative_url }}" alt="{% if f.alt %}{{ f.alt }}{% endif %}" width="100." />
          {% if f.image_caption %}
            <span class="archive__item-caption">{{ f.image_caption | remove: "<p>" | remove: "</p>" }}</span>
          {% endif %}
        </div>
      {% endif %}

      <div class="archive__item-body">
        {% if f.title %}
          <h4 class="archive__item-title">{{ f.title }}</h4>
        {% endif %}

        {% if f.excerpt %}
          <div class="archive__item-excerpt">
            {{ f.excerpt | markdownify }}
          </div>
        {% endif %}

        {% if f.url %}
          <p><a href="{{ f.url | relative_url }}" class="btn {{ f.btn_class }}">{{ f.btn_label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a></p>
        {% endif %}
      </div>
    </div>
  </div>
{% endfor %}

</div>

<!--
## Machine learning

### 2023: Conflict monitoring using seismic timeseries segmentation
[![Learn more](https://img.shields.io/badge/Learn%20more-F9A431)](https://quentinbrissaud.github.io/infrasound/Ukraine_Sandia/)

The real-time seismo-acoustic monitoring of military conflicts can provide a unique alternative to conventional ground reports and sparse satellite coverage. The pressure waves generated by an explosion travel through the atmosphere and subsurface as sound and seismic waves, and their signature can be recorded by arrays of seismometers for ground motion or microbarometers for sound propagation. However, standard monitoring techniques can be both computationally expensive when localizing signals over large regions and/or prone to false detections when signals have low amplitudes. In this contribution we propose a Machine-Learning (ML) based solution to detect seismic and infrasound arrivals and locate sources close to real time. To validate our model we leverage the seismic data collected during the Russia-Ukraine conflict started in February 2022 using the Ukrainian primary station of the International Monitoring System (IMS), the Malin array (AKSAG). We test both the accuracy and computational efficiency of our approach against a threshold-based migration stacking model developed for near-real time monitoring in Ukraine. We hope that this first-ever ML detector of both seismic and acoustic phases could be employed for real-time monitoring of conflicts around the world across different network geometries and noise conditions.

### 2022: Regional scale sound amplitude predictions with deep learning
[![Learn more](https://img.shields.io/badge/Learn%20more-F9A431)](https://quentinbrissaud.github.io/presentation/Talk-AGU-deep-learning/) 
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/QuentinBrissaud/ML_attenuation_infrasound)

Modelling the spatial distribution of infrasound attenuation (or transmission loss, TL) is key to understanding and interpreting microbarometer data and observations. Such predictions enable the reliable assessment of infrasound source characteristics such as ground pressure levels associated with earthquakes, man-made or volcanic explosion properties, and ocean-generated microbarom wavefields. However, the computational cost inherent in full-waveform modelling tools, such as parabolic equation (PE) codes, often prevents the exploration of a large parameter space, that is variations in wind models, source frequency and source location, when deriving reliable estimates of source or atmospheric properties—in particular for real-time and near-real-time applications. Therefore, many studies rely on analytical regression-based heuristic TL equations that neglect complex vertical wind variations and the range-dependent variation in the atmospheric properties. This introduces significant uncertainties in the predicted TL. In the current contribution, we propose a deep learning approach trained on a large set of simulated wavefields generated using PE simulations and realistic atmospheric winds to predict infrasound ground-level amplitudes up to 1000 km from a ground-based source. Realistic range dependent atmospheric winds are constructed by combining ERA5, NRLMSISE-00 and HWM-14 atmospheric models, and small-scale gravity-wave perturbations computed using the Gardner model. Given a set of wind profiles as input, our new modelling framework provides a fast (0.05 s runtime) and reliable (∼5 dB error on average, compared to PE simulations) estimate of the infrasound TL.

### 2021: Automatic earthquake detection in the high atmosphere
[![Learn more](https://img.shields.io/badge/Learn%20more-F9A431)](https://quentinbrissaud.github.io/ionosphere/ML_TEC/)
[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/QuentinBrissaud/AIDE)

Tsunamis generated by large earthquake-induced displacements of the ocean floor can lead to tragic consequences for coastal communities. Measurements of co-seismic ionospheric disturbances (CIDs) offer a unique solution to characterize an earthquake’s tsunami potential in near-real-time (NRT) since CIDs can be detected within 15 min of a seismic event. However, the detection of CIDs relies on human experts, which currently prevents the deployment of ionospheric methods in NRT. To address this critical lack of automatic procedure, we designed a machine-learning-based framework to (1) classify ionospheric waveforms into CIDs and noise, (2) pick CID arrival times and (3) associate arrivals across a satellite network in NRT. Machine-learning models (random forests) trained over an extensive ionospheric waveform data set show excellent classification and arrival-time picking performances compared to existing detection procedures, which paves the way for the NRT imaging of surface displacements from the ionosphere.

### 2020: ML-aided prediction of seismic hazard in sedimentary basins
[![Learn more](https://img.shields.io/badge/Learn%20more-F9A431)](https://quentinbrissaud.github.io/seismology/Basin_ML/)

The amplification of surface waves propagating through sedimentary basins is a well-known source of seismic hazard for infrastructure. To characterize basin effects, seismologists have routinely employed physic-based regression models to connect observations to the known driving factors of amplification (velocity contrasts, sediment-to-rock depth). However, the surface-wave contribution is commonly neglected and the basin parameters driving amplification are sometimes poorly constrained (lack of high-resolution velocity and density models) or not understood because of the insufficient number of high-quality observations. Because purely numerical investigations can be computationally expensive and analytic formulas rely on simplifying assumptions (neglecting complex basin geometries, near-field effects and conversions between body and surface waves), the generalization of simple regression models is a difficult task. In order to bridge the gap between simplistic analytic models and computationally-expensive numerical tools in geophysics, we use a random forest machine-learning approach to learn the nonlinear correlations between subsurface parameters and amplification spectra in axisymmetric basins. Trained over a large dataset of high-order numerical solutions, the approach provides a fast and highly accurate amplification prediction tool. It greatly facilitates sensitivity measurements of wave amplification for a wide range of basin structures and provides estimates of the relative importance of various basin parameters. Finally, we assess various commonly-used proxies in ground-motion prediction equation to predict the surface-wave contribution in amplification spectra.

## Event monitoring

### Seismo-acoustic couplings
[![Learn more](https://img.shields.io/badge/Learn%20more-F9A431)](https://quentinbrissaud.github.io/seismology/Basin_ML/)
The amplification of surface waves propagating through sedimentary basins is a well-known source of seismic hazard for infrastructure. To characterize basin effects, seismologists have routinely employed physic-based regression models to connect observations to the known driving factors of amplification (velocity contrasts, sediment-to-rock depth). However, the surface-wave contribution is commonly neglected and the basin parameters driving amplification are sometimes poorly constrained (lack of high-resolution velocity and density models) or not understood because of the insufficient number of high-quality observations. Because purely numerical investigations can be computationally expensive and analytic formulas rely on simplifying assumptions (neglecting complex basin geometries, near-field effects and conversions between body and surface waves), the generalization of simple regression models is a difficult task. In order to bridge the gap between simplistic analytic models and computationally-expensive numerical tools in geophysics, we use a random forest machine-learning approach to learn the nonlinear correlations between subsurface parameters and amplification spectra in axisymmetric basins. Trained over a large dataset of high-order numerical solutions, the approach provides a fast and highly accurate amplification prediction tool. It greatly facilitates sensitivity measurements of wave amplification for a wide range of basin structures and provides estimates of the relative importance of various basin parameters. Finally, we assess various commonly-used proxies in ground-motion prediction equation to predict the surface-wave contribution in amplification spectra.
-->