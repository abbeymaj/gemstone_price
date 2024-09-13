## Gemstone Price Prediction

The objective of this project is to predict the price of gemstones, given certain attributes of the gemstone. A company would use this prediction to distinguish between higher profitable stones from lower profitable stones. Thus, this is a typical regression machine learning problem.

There are 10 independent variables (including id):

1. id : unique identifier of each diamond
2. carat : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones.
3. cut : Quality of the gemstone's Cut
4. color : Color of the gemstone.
5. clarity : The gemstone's clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
6. depth : The depth of the gemstone is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
table : A gemston's table is the facet which can be seen when the stone is viewed face up.
7. x : The gemstone's X dimension
8. y : The gemstone's Y dimension
9. x : The gemstone's Z dimension
10. Price : Price of the gemstone.

"Price" is the target variable for this project.

## Installation

Install the project using pip. It is always recommended to use a virtual environment (for example, using anaconda) to do the installation.

This project was built using Python 3.9.

To install the project, use the following: 

```bash
  pip install -r requirements.txt
```
    
## Tech Stack

**Client:** Flask, HTML, CSS

**Language:** Python


## Screenshot of the Prediction Page

There are two webpages, which the user can interact with, for the project. 

Landing Page:

This is the landing page for the project. The page provides a brief overview of the project and then allows the user to navigate to the prediction page. 

The screenshot of the Landing Page is given below:

![Landing Page Screenshot Link](https://github.com/abbeymaj80/my-ml-datasets/blob/master/screenshots/gemstone_landing.jpg)

Prediction Page:

The prediction page enables the user to select or enter information pertaining to the gemstone whose price needs to be predicted. Once the user enters the necessary information, the user must click on the "Submit" button to generate the price prediction.

The screenshot of the Prediction page is given below:

![Prediction page Screenshot Link](https://github.com/abbeymaj80/my-ml-datasets/blob/master/screenshots/gemstone_predict.jpg)


## Link to the High Level Design Document

The High Level design document for the project can be found using the link below:

 ![High Level Design Document Link](https://github.com/abbeymaj80/my-ml-datasets/blob/master/Design_Docs/gemstone_price_prediction_hdd.docx)


## Link to Dataset on Kaggle

 ![Kaggle Credit Card Fraud Detection Dataset Link](https://www.kaggle.com/competitions/playground-series-s3e8/overview)


## Additional Reference Materials Used in the Project

Additional reference used in the project are listed below:

 ![Link to the American Gem Society](https://www.americangemsociety.org/ags-diamond-grading-system/)