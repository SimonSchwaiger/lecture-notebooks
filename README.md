# Lecture Notebooks

This repository contains interactive Jupyter notebooks that complement my robotics programming courses. These notebooks include text, figures, executable code, and code output that can be viewed statically or run interactively.

## Repository Structure

```
lecture-notebooks/
├── Notebooks/
│   ├── 0_Basics.ipynb                    # Python fundamentals
│   ├── 1_ROS_Interfacing.ipynb           # ROS integration basics
│   ├── 2_2D_Transformations_ROS.ipynb    # 2D transformations in ROS
│   ├── 3_Data_Visualisation.ipynb        # Data visualization techniques
│   ├── Code-Debugging-With-LLMs/         # LLM-assisted debugging exercise
│   ├── Mobile-Robotics-Notebooks/        # Mobile robotics projects
│   ├── Optimisation-Based-Robotics/      # Robot behaviour from optimisation
│   └── util/                             # Utility scripts
├── ROS Resources/                        # ROS 2 installation and setup guides (Coming Soon)
└── requirements.txt                      # Python dependencies
```

## Getting Started

1. You can open all notebooks here on GitHub, but you will not be able to interact with them. For an interactive version, install the following on your machine

    - Python 3.7+
    - pip package manager

2. Then clone the repository or download each notebook of interest
    ```bash
    git clone https://github.com/SimonSchwaiger/lecture-notebooks.git
    ```

3. To execute all examples, install dependencies first.
   ```bash
   pip install -r requirements.txt
   ```

## Viewing Notebooks

We recommend [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) for its ease of use and notebook-centric UI, however, any Notebook viewer works.

### Interactive Viewing
- **JupyterLab**: Launch with `jupyter lab` for full interactive experience
- **Jupyter Notebook**: Use `jupyter notebook` for classic interface
- **VS Code**: Open notebooks directly in VS Code with the Jupyter extension

### Static Viewing
- **GitHub**: View notebooks directly on GitHub (non-interactive)
- **nbviewer**: Use [nbviewer.org](https://nbviewer.org/) to view notebooks from GitHub URLs
- **VS Code**: Preview notebooks without running cells

## Contributing

Feel free to explore, modify, and run the notebooks. Each notebook is designed to be self-contained with clear explanations and practical examples. The main Notebooks (`./Notebooks`) are numbered and designed to be worked through in order.

## Support

For questions or issues, please refer to the individual notebook documentation or create an issue in this repository.
