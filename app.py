import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create and train a classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Function to perform prediction
def classify_iris():
    try:
        # Get the input values from the entry fields
        sepal_length = float(entry1.get())
        sepal_width = float(entry2.get())
        petal_length = float(entry3.get())
        petal_width = float(entry4.get())
        
        # Make a prediction using the trained model
        prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Map the predicted class to the corresponding Iris species
        species = iris.target_names[prediction[0]]
        
        # Show the predicted species in a message box
        messagebox.showinfo("Prediction", f"The predicted species is: {species}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values")

# Create the main window
root = tk.Tk()
root.title("Iris Classification")

# Set the size of the window
root.geometry("400x300")  # Width x Height

# Create labels and entry fields for user input
label1 = tk.Label(root, text="Sepal Length:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Sepal Width:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Petal Length:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Petal Width:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

# Create a button to trigger classification
classify_button = tk.Button(root, text="Classify Iris", command=classify_iris)
classify_button.pack()

# Start the main loop
root.mainloop()
