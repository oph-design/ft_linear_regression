<a name="readme-top"></a>




<h1 align="center">FT Linear Regression</h1>
<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/oph-design/ft_linear_regression?color=lightblue" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/oph-design/ft_linear_regression?color=yellow" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/oph-design/ft_linear_regression?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/created-at/oph-design/ft_linear_regression?color=green" />
</p>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
<img width="400" alt="Screen Shot 2024-04-04 at 7 09 39 PM" src="https://github.com/oph-design/ft_linear_regression/assets/115570424/0c62f155-91fa-403d-a475-da216cfd2dcf">
</p>

The project is about training a linear model able to predict the price of a car based on the driven mileage.
</br> So the formular to achieve is:
$`price = mileage * m + c`$ </br>
with `m` and `c` having to be found by the training alogrithm. </br> For finding the coeficciants the project is using the Gradient Descent algorithm,
which uses the mean squared error as loss function: </br> $$E = \sum_{i=1}^n (y_i * (m * x_i + c))^2$$
During each the program calculates the loss for each coefficient using the partial derivatives of the loss function.
The coefficiants than get adjusted by their multiplied by the Learningrate L (0.1): $`Coef_x = Coef_x - L * D_x `$ </br>


<!-- GETTING STARTED -->
## Getting Started

The following contains a description of how to use the program.

### Prerequisites

To run the programs you have to have python3 and pip3 installed. See an installation guide <a href="https://kinsta.com/knowledgebase/install-python/">here</a>
After, you have to clone the repository and install the libraries used in this project.
  ```sh
   git clone https://github.com/oph-design/ft_linear_regression
   pip3 install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
### Usage

The project consists of three seperate programs `predict.py`, `train.py` and `evaluate.py`
Each of the programs can be started by typing:
   ```sh
   python3 <programname>.py
   ```
* `predict.py` asks for any mileage and ourt puts the pice prediction
* `train.py` train the model on the current data and shows the training process
* `evaluate.py` calculates the R squared value of the current model


## Contact

Ole-Paul Heinzelmann</br>
ole.paul.heinzelmann@protonmail.com </br>
<p></p>
<a href="https://www.linkedin.com/in/ole-paul-heinzelmann-a08304258/">
<img alt="linkedin shield" src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" />
</a></br> 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
