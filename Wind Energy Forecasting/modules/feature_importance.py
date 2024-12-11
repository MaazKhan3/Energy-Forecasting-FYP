import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    """Plot the feature importances of the trained model."""
    importances = model.feature_importances_
    indices = range(len(importances))
    
    plt.figure(figsize=(12, 8))
    plt.barh(indices, importances, align='center')
    plt.yticks(indices, feature_names)
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature')
    plt.title('Feature Importance from Random Forest')
    plt.show()
