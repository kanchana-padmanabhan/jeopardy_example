import sys
import tkinter as tk
from tkinter import ttk
import pandas as pd


class AnswerQuestion:
    def check_answer(self):
        sys.stdout = self.print_obj
        #  print(self.question)
        #  print(self.question_answer_jeopardy_style[self.question])
        #  print(self.answer)
        correct_answer = self.question_answer_jeopardy_style.get(self.question, "Answer not found")
        user_answer = self.answer.get()
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}. The answer you gave was: {user_answer}")
        
        print("--------------------------------------------------------------------------------")
        print("\n")
        self.answer_window.destroy()


    
    # def open_answer_portal(self, question):
    #     self.question = question
    #     tk.Label(self.root, text="Answer").grid(row=0, column=0)
    #     self.answer = tk.Entry(self.root)
    #     self.answer.grid(row=0, column=1)
    #     tk.Button(self.root, text='Check', command=self.check_answer).grid(row=3, 
    #                                                    column=1, 
    #                                                    sticky=tk.W, 
    #                                                    pady=4)
    def open_answer_portal(self, question):
        self.question = question
        self.answer_window = tk.Toplevel(self.root)
        tk.Label(self.answer_window, text="Answer").grid(row=0, column=0)
        self.answer = tk.Entry(self.answer_window)
        self.answer.grid(row=0, column=1)
        tk.Button(self.answer_window, text='Check', command=self.check_answer).grid(row=3, column=1, sticky=tk.W, pady=4)


    def __init__(self, root, print_obj):
        self.question_answer_jeopardy_style = {
                "In 1492, Christopher Columbus embarked on a famous voyage across the Atlantic Ocean. Which country sponsored his journey?": "What is Spain?",
                "The Battle of Gettysburg, a turning point in the American Civil War, took place in which U.S. state?": "What is Pennsylvania?",
                "What ancient wonder was located in the city of Babylon and is considered one of the Seven Wonders of the Ancient World?": "What are the Hanging Gardens of Babylon?",
                "Who was the leader of the Soviet Union during the Cuban Missile Crisis in 1962?": "Who is Nikita Khrushchev?",
                "The Treaty of Versailles, signed in 1919, officially ended which major conflict?": "What is World War I?",
                "What is the result of multiplying 8 by 7?": "What is 56?",
                "If a triangle has angles measuring 90, 45, and 45 degrees, what type of triangle is it?": "What is a right-angled isosceles triangle?",
                "What is the square root of 144?": "What is 12?",
                "If a rectangle has a length of 10 units and a width of 5 units, what is its area?": "What is 50 square units?",
                "Solve for x: 2x + 5 = 15.": "What is 5?",
                "The Amazon River, known for its vast biodiversity, is primarily located in which continent?": "What is South America?",
                "What European capital is situated on the banks of the River Thames and is known for landmarks such as Big Ben and the Tower Bridge?": "What is London, United Kingdom?",
                "Mount Everest, the world's highest peak, is part of which mountain range?": "What are the Himalayas?",
                "The Great Barrier Reef, one of the world's most extensive coral reef systems, is located off the northeast coast of which country?": "What is Australia?",
                "What is the largest desert in the world by area, and it is not a cold icy desert but a subtropical one?": "What is the Sahara Desert?"
        }
        self.print_obj = print_obj
        self.root = root
    


class PrintToT1:
    def __init__(self, root):
        self.root = root
        self.t1 = tk.Text(self.root) 
        self.t1.pack() 

    def write(self, s): 
        self.t1.insert(tk.END, s) 
    
    def flush(self):
        pass

class DataFrameViewerApp:
    def __init__(self, root, print_obj, answer_obj):
        self.root = root
        self.print_obj = print_obj
        self.answer_obj = answer_obj
        self.root.title("Sanjay's Jeopardy Board")

        # Create a sample DataFrame
        data = {'History': ['$200', '$400', '$600', '$800', '$1000'],
                'Geography': ['$200', '$400', '$600', '$800', '$1000'],
                'Math': ['$200', '$400', '$600', '$800', '$1000']}
        self.df = pd.DataFrame(data)

        self.category_dollar_question = {
                'History': {
                    '$200': "In 1492, Christopher Columbus embarked on a famous voyage across the Atlantic Ocean. Which country sponsored his journey?",
                    '$400': "The Battle of Gettysburg, a turning point in the American Civil War, took place in which U.S. state?",
                    '$600': "What ancient wonder was located in the city of Babylon and is considered one of the Seven Wonders of the Ancient World?",
                    '$800': "Who was the leader of the Soviet Union during the Cuban Missile Crisis in 1962?",
                    '$1000': "The Treaty of Versailles, signed in 1919, officially ended which major conflict?"
                },
                'Math': {
                    '$200': "What is the result of multiplying 8 by 7?",
                    '$400': "If a triangle has angles measuring 90, 45, and 45 degrees, what type of triangle is it?",
                    '$600': "What is the square root of 144?",
                    '$800': "If a rectangle has a length of 10 units and a width of 5 units, what is its area?",
                    '$1000': "Solve for x: 2x + 5 = 15."
                },
                'Geography': {
                    '$200': "The Amazon River, known for its vast biodiversity, is primarily located in which continent?",
                    '$400': "What European capital is situated on the banks of the River Thames and is known for landmarks such as Big Ben and the Tower Bridge?",
                    '$600': "Mount Everest, the world's highest peak, is part of which mountain range?",
                    '$800': "The Great Barrier Reef, one of the world's most extensive coral reef systems, is located off the northeast coast of which country?",
                    '$1000': "What is the largest desert in the world by area, and it is not a cold icy desert but a subtropical one?"
                }
            }


        # Create Treeview widget
        self.tree = ttk.Treeview(root, columns=self.df.columns, show='headings')

        # Add columns to Treeview
        for i, col in enumerate(self.df.columns):
            self.tree.heading(i, text=col)
            self.tree.column(i, width=100)  # Adjust width as needed

        # Insert data into Treeview
        for i, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Bind click event to the Treeview
        self.tree.bind("<ButtonRelease-1>", self.select_item)

        # Pack Treeview widget
        self.tree.pack(pady=10)

    # def select_item(self, a):
    #     curItem = self.tree.focus()
    #     print(self.tree.item(curItem))


    def select_item(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        # print ('curItem = ', curItem)
        # print ('col = ', col)
        col_int = int(col.replace("#", "")) - 1
        category = self.df.columns[col_int]
        # print(category)

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        # print ('cell_value = ', cell_value)
        

        sys.stdout = self.print_obj

        print(self.category_dollar_question[category][cell_value])
        question = self.category_dollar_question[category][cell_value]
        self.answer_obj.open_answer_portal(question)
       
        


if __name__ == "__main__":
    root = tk.Tk()
    print_obj = PrintToT1(root) 
    answer_obj = AnswerQuestion(root, print_obj)
    app = DataFrameViewerApp(root, print_obj, answer_obj)
    
    root.mainloop()
