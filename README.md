# Autonomous RC Car Project

![Screenshot from 2024-07-02 17-20-15](https://github.com/IyadElwy/AutonomousCarSoftware/assets/83036619/fb231813-403d-420f-a791-c1c675ecbfe7)


This repository contains the software for training and gathering data for an autonomous RC car project. The project is built using a toy RC car equipped with a Raspberry Pi and a single front-facing camera.

## Repository Contents

- **Training Software**: Scripts and modules to train the car's navigation system.
- **Data Gathering Software**: Tools to collect data from the car's sensors and camera.

**Note**: This repository does not include software for inference. Users need to write their own inference software by extending the existing code modules or rewriting the entire system from scratch.

## Project Overview

The aim of this project is to create an autonomous RC car that can navigate through its environment using machine learning techniques. The system relies on a front-facing camera to gather visual data, which is processed on a Raspberry Pi.

## How to Use This Repository

1. **Data Collection**:
    - Use the provided scripts to collect data from the RC car's camera.
    - Store the collected data for training purposes.

2. **Training**:
    - Utilize the training modules to build models based on the collected data.
    - Experiment with different models and parameters to improve performance.

3. **Inference**:
    - The repository does not include inference code. You will need to:
        - Extend the provided modules to implement inference.
        - Alternatively, rewrite the inference software from scratch.

## Additional Resources

- **Drive Folder**: [Project Drive](https://drive.google.com/drive/folders/1R2jCih48Qa1VRuxLK3PNdFmi35KgT1ai?usp=sharing)
    - Contains experiments and data from previous trials.
    - Includes pretrained models and a PowerPoint presentation with a high-level overview of the project.


Happy experimenting and happy driving!
