import tkinter as tk
from tkinter import messagebox
import pandas as pd


class InsuranceChargePredictorApp:
    def __init__(self, master):
        self.master = master
        master.title("Insurance Charge Predictor")

        self.age_label = tk.Label(master, text="Age:")
        self.age_label.grid(row=0, column=0)
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=0, column=1)

        self.bmi_label = tk.Label(master, text="BMI:")
        self.bmi_label.grid(row=1, column=0)
        self.bmi_entry = tk.Entry(master)
        self.bmi_entry.grid(row=1, column=1)

        self.children_label = tk.Label(master, text="Number of Children:")
        self.children_label.grid(row=2, column=0)
        self.children_entry = tk.Entry(master)
        self.children_entry.grid(row=2, column=1)

        self.smoker_label = tk.Label(master, text="Smoker (1 for Yes, 0 for No):")
        self.smoker_label.grid(row=3, column=0)
        self.smoker_entry = tk.Entry(master)
        self.smoker_entry.grid(row=3, column=1)

        self.predict_button = tk.Button(master, text="Predict", command=self.predict_charge)
        self.predict_button.grid(row=4, column=0, columnspan=2)

    def predict_charge(self):
        age = float(self.age_entry.get())
        bmi = float(self.bmi_entry.get())
        children = int(self.children_entry.get())
        smoker = int(self.smoker_entry.get())


        data = pd.read_csv("https://raw.githubusercontent.com/Ktokkerz01/SoftwareTechCapstoneProject/main/Dataset11.csv")  # Example dataset
        X = data[['age', 'bmi', 'children', 'smoker']]
        y = data['charges']
        model = LinearRegression()
        model.fit(X, y)

        charge_prediction = model.predict([[age, bmi, children, smoker]])

        messagebox.showinfo("Prediction Result", f"The predicted average price of charges is: ${charge_prediction[0]:.2f}")

root = tk.Tk()
root.mainloop()
