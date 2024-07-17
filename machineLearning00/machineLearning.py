#Code from Kaggle
import pandas as pd 

#Load data 
melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

#Filter rows with missing values
melbourne_data = melbourne_data.dropna(axis=0)

#Chose target and features
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]


from sklearn.model_selection import train_test_split

# Split data into training and validation data, for both features and target
# The split is based on a random number generator
# Supplying a numeric value to the random_state argument guarantees we get the same split every time we run the script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)


# Decision Tree Regressor 
from sklearn.tree import DecisionTreeRegressor

# specify model
melbourne_model = DecisionTreeRegressor(random_state=1)
# fit model 
melbourne_model.fit(train_X, train_y)


# Mean Absolute Error: Underfitting and Overfitting
from sklearn.metrics import mean_absolute_error

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 20, 50, 100, 250, 500]
# loop to find the ideal tree size from candidate_max_leaf_nodes
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
# store the best value of max_leaf_nodes
best_tree_size = min(scores, key=scores.get)
# fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)
# fit the final model and uncomment the next two lines
final_model.fit(X,y)


# Random Forests
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))