import math
import numpy as np
import pandas as pd
# Import sklearn modules.
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Import matplotlib modules.
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import matplotlib as mpl
mpl.rcParams.update({
    'font.size': 20.0,
    'axes.titlesize': 'small',
    'axes.labelsize': 'small',
    'xtick.labelsize': 'small',
    'ytick.labelsize': 'small'
})


transactions = pd.read_csv('./item_sales.csv')

# print(transactions['state_bottle_retail']*transactions['sale_bottles'])
# print(pd.DatetimeIndex(transactions['date']).strftime(date_format='%Y-%m'))

transactions['month']=pd.DatetimeIndex(transactions['date']).strftime(date_format='%Y-%m')

transactions.drop(columns=['invoice_line_no','date','itemno','pack','vendor_no'], inplace=True)


gb = transactions.groupby('month')


agg = pd.DataFrame()
agg['Price'] = gb['state_bottle_retail'].mean()
agg['Demand'] = gb['sale_bottles'].sum()
agg.to_csv('agg_data.csv')

print(agg)


def split_and_std(X, y, test_size=0.2):
    '''
    Note: standardizes ALL features.  
    '''
    # Train/test split, 80/20 or 70/30.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    # Standardize X_train, X_test.
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train=scaler.transform(X_train)
    X_test=scaler.transform(X_test)
    return (X_train, X_test, y_train, y_test)
    
def lin_reg_errors(y_true, y_pred):
    # Mean square error.
    MSE=mean_squared_error(y_true, y_pred)
    # Root mean square error.
    RMSE = math.sqrt(MSE)
    # Coefficient of determination. 
    R2 = r2_score(y_true,y_pred)
    return (MSE, RMSE, R2)
    
def acc_res_plots(y_true, y_pred):
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(4, 5))
    # Accuracy plot.
    ax[0].scatter(y_pred, y_true);
    ax[0].set_title('Accuracy')  
    ax[0].set_ylabel('Actual')
    # Residual plot.
    residuals = y_true - y_pred
    ax[1].scatter(y_pred, residuals);
    ax[1].set_title('Residuals')  
    ax[1].set_ylabel('Residual')
    ax[1].set_xlabel('Predicted')
    # Plot model.
    pred_min = np.amin(y_pred)
    pred_max = np.amax(y_pred)
    ax[0].plot([pred_min, pred_max], [pred_min, pred_max], 'k--')
    ax[1].plot([pred_min, pred_max], [0, 0], 'k--')
    fig.tight_layout()
    return (fig, ax)

X = np.matrix(agg['Price']).transpose()
y = agg['Demand'].as_matrix()

# X, y = make_regression( n_samples=100, n_features=2, noise=2.0)


# print(X)
# print(y)

# # Split and standardize.
# X_train, X_test, y_train, y_test = split_and_std(X, y)
# # Make and fit linear model, i.e. y = X*beta_coefs + epsilon, using ordinary least squares.
# linear = LinearRegression()
# linear.fit(X_train, y_train)
# # beta_coefs = (XTX)-1XTy
# beta_coefs = linear.coef_
# # Generate predictions.
# y_pred = linear.predict(X_test)
# # Compute error measures.
# MSE, RMSE, R2 = lin_reg_errors(y_test, y_pred)
# print(MSE, RMSE, R2)
# # Accuracy and residual plots.
# fig, ax = acc_res_plots(y_test, y_pred)

# plt.savefig('acc_res.png')



