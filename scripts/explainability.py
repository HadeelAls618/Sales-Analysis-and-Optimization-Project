

from lime.lime_tabular import LimeTabularExplainer

def explain_model(X_train, model, X_test, instance_index=3, num_features=7):
    """
    Use LIME to explain the model's predictions.
    """
    explainer = LimeTabularExplainer(X_train.values, feature_names=X_train.columns, mode='regression')
    X_observation = X_test.iloc[[instance_index], :]
    
    exp = explainer.explain_instance(X_observation.values[0], model.predict, num_features=num_features)
    
    # Show the explanation in the notebook (if supported)
    exp.show_in_notebook(show_table=True, show_all=False)
    
    # Return the explanation as a list
    return exp.as_list()
     