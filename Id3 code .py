import math
from collections import Counter


#the function of entropy calculation is below 

def entropy(data):
    """Calculate the entropy of a dataset."""
    labels = [instance['class'] for instance in data]
    label_counts = Counter(labels)
    total_instances = len(data)
    entropy = 0.0
    for label in label_counts:
        probability = label_counts[label] / total_instances
        entropy -= probability * math.log2(probability)
    return entropy
    
    
#the function of Information Gain calculation is below

def information_gain(data, attribute):
    """Calculate the Information Gain for a specific attribute."""
    total_entropy = entropy(data)
    attribute_values = set([instance[attribute] for instance in data])
    weighted_entropy = 0.0
    for value in attribute_values:
        subset = [instance for instance in data if instance[attribute] == value]
        subset_entropy = entropy(subset)
        probability = len(subset) / len(data)
        weighted_entropy += probability * subset_entropy
    return total_entropy - weighted_entropy

def most_common_class(data):
    """Return the most common class label in the dataset."""
    labels = [instance['class'] for instance in data]
    label_counts = Counter(labels)
    return label_counts.most_common(1)[0][0]

def id3(data, attributes):
    """ID3 Decision Tree Algorithm."""
    # If all instances have the same class label, return a leaf node with that label
    if len(set(instance['class'] for instance in data)) == 1:
        return data[0]['class']

    # If there are no attributes left, return the most common class label
    if len(attributes) == 0:
        return most_common_class(data)

    # Select the best attribute to split on based on Information Gain
    best_attribute = max(attributes, key=lambda attr: information_gain(data, attr))

    # Create a decision tree with the best attribute as the root
    tree = {best_attribute: {}}
    attributes.remove(best_attribute)

    # Recursively build the subtree for each value of the best attribute
    for value in set(instance[best_attribute] for instance in data):
        subset = [instance for instance in data if instance[best_attribute] == value]
        subtree = id3(subset, attributes.copy())
        tree[best_attribute][value] = subtree

    return tree

# All The Data That We Gonna Be Using 
data = [
    {'Travel': 'No', 'Education': 'High_School', 'Emplyment_Status': 'Self_Employed', 'Gender': 'Male', 'class': 'Yes'},
    {'Travel': 'Yes', 'Education': 'Bachelors', 'Emplyment_Status': 'Self_Employed', 'Gender': 'Female', 'class': 'No'},
    {'Travel': 'Yes', 'Education': 'High_School', 'Emplyment_Status': 'Unemployed', 'Gender': 'Female', 'class': 'No'},
    {'Travel': 'Yes', 'Education': 'High_School', 'Emplyment_Status': 'Employed', 'Gender': 'Male', 'class': 'Yes'},
    {'Travel': 'No', 'Education': 'Masters', 'Emplyment_Status': 'Employed', 'Gender': 'Female', 'class': 'Yes'},
    {'Travel': 'Yes', 'Education': 'Bachelors', 'Emplyment_Status': 'Employed', 'Gender': 'Male', 'class': 'Yes'},
    {'Travel': 'Yes', 'Education': 'Bachelors', 'Emplyment_Status': 'Self_Employed', 'Gender': 'Male', 'class': 'Yes'},
    {'Travel': 'No', 'Education': 'Masters', 'Emplyment_Status': 'Employed', 'Gender': 'Female', 'class': 'No'},
    {'Travel': 'Yes', 'Education': 'High_School', 'Emplyment_Status': 'Employed', 'Gender': 'Male', 'class': Yes'},
    {'Travel': 'No', 'Education': 'Bachelors', 'Emplyment_Status': 'Employed', 'Gender': 'Male', 'class': 'Yes'},
    {'Travel': 'No', 'Education': 'Masters', 'Emplyment_Status': 'Unemployed', 'Gender': 'Female', 'class': 'No'},
    {'Travel': 'Yes', 'Education': 'Bachelors', 'Emplyment_Status': 'Unemployed', 'Gender': 'Female', 'class': 'No'},
    {'Travel': 'No', 'Education': 'Bachelors', 'Emplyment_Status': 'Employed', 'Gender': 'Female', 'class': 'Yes'},
    {'Travel': 'No', 'Education': 'High_School', 'Emplyment_Status': 'Employed', 'Gender': 'Male', 'class': 'No'},
]

attributes = ['Travel', 'Education', 'Emplyment_Status', 'Gender']

decision_tree = id3(data, attributes)
print(decision_tree)
