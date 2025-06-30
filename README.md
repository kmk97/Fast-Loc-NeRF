# Fast Global Localization on Neural Radiance Field

[![arXiv](https://img.shields.io/badge/arXiv-2406.12202-B31B1B.svg)](https://arxiv.org/abs/2406.12202)

###  *Accepted to ICRA 2025*  
### Code will be released soon


---

## 🔥 Overview  
Fast-Loc-NeRF is a novel approach for **fast and accurate global localization** in NeRF maps. While Loc-NeRF introduced the idea of Monte Carlo Localization (MCL) using NeRF, it suffers from **slow rendering speed**, making it impractical for real-time applications.  

**Fast-Loc-NeRF** improves upon this by introducing:  
✔ **Particle Rejection Weighting**: Uses NeRF's inherent uncertainty estimation to filter out unreliable particles.  
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

## Using LLFF Data for Global Localization

Download LLFF images and pretrained NeRF-Pytorch weights from [NeRF-Pytorch](https://github.com/yenchenlin/nerf-pytorch). If you download our fork of [iNeRF](https://github.com/salykovaa/inerf), the configs and ckpts folder will already be setup correctly with the pre-trained weights, and you just need to add the data folder from NeRF-Pytorch.

Place data using the following structure:

```
├── configs   
│   ├── ...
├── ckpts                                                                                                       
│   │   ├── fern
|   |   |   └── fern.tar                                                                                                                     
│   │   ├── fortress
|   |   |   └── fortress.tar                                                                                   
│   │   ├── horns
|   |   |   └── horns.tar   
│   │   ├── room
|   |   |   └── room.tar   
│   │   └── ...                                                                                 
                                                                                            
├── data                                                                                                                                                                                                       
│   ├── nerf_llff_data                                                                                                  
│   │   └── fern  # downloaded llff dataset                                                                                                                         
│   │   └── fortress  # downloaded llff dataset                                                                                  
│   │   └── horns   # downloaded llff dataset
|   |   └── room   # downloaded llff dataset
|   |   └── ...
```

After updating your yaml file `fast.yaml` with the directory where you placed the data and any other params you want to change, you are ready to run Fast-Loc-NeRF! By default, Fast-Loc-NeRF will estimate the camera pose of 5 random images from each of fern, fortress, horns, room (20 images in total). You can use rviz to provide real-time visualization of the ground truth pose and the particles.

---

# 1. Installation

## A. Prerequisites

* Install ROS by following [ROS website](http://wiki.ros.org/ROS/Installation).
* If you want to use VIO for the predict step for a real robot demo, install a VIO such as [VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) or [Kimera](https://github.com/MIT-SPARK/Kimera).

## B. Fast-Loc-NeRF Installation

```bash
# Setup catkin workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin init

# Clone repo
cd ~/catkin_ws/src
git clone https://github.com/kmk97/Fast-Loc-NeRF.git

# Compile code
catkin build

# Source workspace
source ~/catkin_ws/devel/setup.bash

# Install Python dependencies (if requirements.txt exists)
cd ~/catkin_ws/src/Fast-Loc-NeRF
pip install torch torchvision torchaudio
pip install opencv-python numpy scipy matplotlib pyyaml tqdm imageio configargparse
```

---

# 2. Starting Fast-Loc-NeRF

We will use ROS and rviz as a structure for running Fast-Loc-NeRF and for visualizing performance. As a general good practice, remember to source your workspace for each terminal you use.

1. Open a new terminal and run: `roscore`

2. In another terminal, launch Fast-Loc-NeRF:
```bash
roslaunch locnerf navigate.launch parameter_file:=<param_file.yaml>
```

3. In another terminal, launch rviz for visualization:
```bash
rviz -d $(rospack find locnerf)/rviz/rviz.rviz
```

4. If you are not running with a rosbag, i.e. you are using LLFF data, then Fast-Loc-NeRF should start and you should be set. If you are using a rosbag, continue to the next steps.

5. In another terminal launch VIO

6. Finally, in another terminal, play your rosbag:
```bash
rosbag play /PATH/TO/ROSBAG
```

---

# 3. Provided Config Files

We provide two yaml files in `/cfg` for global localization experiments:

- **`fast.yaml`**: Setup to run Fast-Loc-NeRF with our novel particle rejection weighting and coarse-to-fine matching techniques. This configuration demonstrates the improvements over standard Loc-NeRF with faster convergence and better accuracy in global localization scenarios.

- **`llff_global.yaml`**: Runs standard global localization on the LLFF dataset with a wider spread of particles to test the ability to perform global localization without our enhancements, for comparison purposes.

---

# 4. Usage

We provide example code to run Fast-Loc-NeRF on LLFF data to compare with iNeRF and Loc-NeRF for global localization experiments. We use [NeRF-Pytorch](https://github.com/yenchenlin/nerf-pytorch) as our NeRF map.

The fastest way to start running Fast-Loc-NeRF is to download LLFF data with pre-trained NeRF weights. The data structure and configuration details are explained in the "Using LLFF Data for Global Localization" section above.

---

## Publications

If you find this code relevant for your work, please consider citing our paper:

```bibtex
@article{kim2024fast,
  title={Fast Global Localization on Neural Radiance Field},
  author={Kim, Mangyu and Bang, Jaeho and Lim, Hwangpil and others},
  journal={arXiv preprint arXiv:2406.12202},
  year={2024}
}
```

---

# Third-party Code

This code were based on [Loc-NeRF](https://github.com/MIT-SPARK/Loc-NeRF), and [NeRF-Pytorch](https://github.com/yenchenlin/nerf-pytorch).

```bibtex
@misc{lin2020nerfpytorch,
 title={NeRF-pytorch},
 author={Yen-Chen, Lin},
 publisher = {GitHub},
 journal = {GitHub repository},
 howpublished={\url{https://github.com/yenchenlin/nerf-pytorch/}},
 year={2020}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

