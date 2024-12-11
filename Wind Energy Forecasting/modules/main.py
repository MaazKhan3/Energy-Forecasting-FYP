from data_processing import load_data, preprocess_data, split_data
from model_training import train_model, evaluate_model
from feature_importance import plot_feature_importance
from data_visualization import plot_predictions, plot_confusion_matrix

def main():
    # Load and preprocess data
    filepath = 'data/your_dataset.csv'
    df = load_data(filepath)
    X, y = preprocess_data(df, target_column='target')
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    accuracy, report = evaluate_model(model, X_test, y_test)
    print(f'Accuracy: {accuracy}')
    print(f'Classification Report:\n{report}')

    # Feature importance
    feature_names = df.drop(columns=['target']).columns
    plot_feature_importance(model, feature_names)

    # Plot predictions and confusion matrix
    y_pred = model.predict(X_test)
    plot_predictions(y_test, y_pred)
    plot_confusion_matrix(y_test, y_pred, classes=model.classes_)

if __name__ == '__main__':
    main()
