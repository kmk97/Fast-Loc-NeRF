# Fast Global Localization on Neural Radiance Field

[![arXiv](https://img.shields.io/badge/arXiv-2406.12202-B31B1B.svg)](https://arxiv.org/abs/2406.12202)

###  *Accepted to ICRA 2025*  
### Code will be released soon


---

## 🔥 Overview  
Fast-Loc-NeRF is a novel approach for **fast and accurate global localization** in NeRF maps. While Loc-NeRF introduced the idea of Monte Carlo Localization (MCL) using NeRF, it suffers from **slow rendering speed**, making it impractical for real-time applications.  

**Fast-Loc-NeRF** improves upon this by introducing:  
✔ **Particle Rejection Weighting**: Uses NeRF’s inherent uncertainty estimation to filter out unreliable particles.  
✔ **Coarse-to-Fine Matching**: Matches rendered pixels with observed images progressively from low to high resolution, reducing computational overhead.  

---

## 🏞️ Overview Diagram  

<p align="left">
  
  <img src="./asset/test2.png" width="60%">
</p>
*Figure: Overview of Fast-Loc-NeRF.*

---

## 📊 Experimental Results  

Fast-Loc-NeRF outperforms existing methods in both **accuracy and efficiency**.  

![Results](./asset/result1.png)  
*Figure: Localization accuracy and speed comparison.*

---

## 📽️ Video Demonstration  

[![Watch the video](https://img.youtube.com/vi/hkKbtk9wHGk/maxresdefault.jpg)](https://youtu.be/hkKbtk9wHGk)  
*(Click the image to watch the video on YouTube)*
---

<!-- ## 📦 Installation  
Clone the repository and install dependencies:  
```bash
git clone https://github.com/kmk97/Fast-Loc-NeRF.git
cd Fast-Loc-NeRF
pip install -r requirements.txt -->

