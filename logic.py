from PyQt6.QtWidgets import QMainWindow
from gui import Ui_MainWindow
import os

class Logic(QMainWindow, Ui_MainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.calculate_button.clicked.connect(lambda: self.calculate_amount())

    def calculate_amount(self) -> None:
        """calculate amount and main logic"""
        total_amount = self.get_total_amount()
        amoun_error_msg = self.validate_total_amount(total_amount)
        if amoun_error_msg:
            self.update_message_label(amoun_error_msg, 'red')
            return
        
        people_count = self.get_people_count()
        people_count_error_msg = self.validate_people_count(people_count)
        if people_count_error_msg:
            self.update_message_label(people_count_error_msg, 'red')
            return
        
        tip_percentage = self.get_tip_percentage()
        total_with_tip = self.calculate_total_with_tip(tip_percentage, total_amount)
        total_per_person = self.calculate_amount_per_person(total_with_tip, people_count)
        self.update_message_label(f"Total: ${total_with_tip:.2f}.  Amount per person: ${total_per_person:.2f}", 'white')
        


    def get_total_amount(self) -> str:
        """Get amount from input and remove extra spaces"""
        return self.total_amount_input.text().strip()
    
    def validate_total_amount(self, total_amount: str) -> str | None:
        """Validate that amount is a positive number"""
        try:
            converted_amount = float(total_amount)
            if converted_amount <= 0:
                raise ValueError
        except ValueError:
            return "Enter a valid amount. Example: 150.25"
        
         
    def get_people_count(self) -> str:
        """Get number of people from input and remove extra spaces"""
        return self.people_count_input.text().strip()
    
    def validate_people_count(self, people_count: str) -> str | None:
        """Validate that number of people is a positive number"""
        try:
            converted_people_count = int(people_count)
            if converted_people_count <= 0:
                raise ValueError
        except ValueError:
            return "Enter a valid number of people"
        
    def get_tip_percentage(self) -> float:
        """Convert to decimal number the tip percentage"""
        tip_text = self.tip_combo_box.currentText()
        
        return float(tip_text.replace('%', '')) / 100
    
    def calculate_total_with_tip(self, tip_percentage: float, total_amount: str) -> float:
        """Calculate total amount plus tip"""
        total_amount_float = float(total_amount)
        tip = total_amount_float * tip_percentage
        return total_amount_float + tip
    
    def calculate_amount_per_person(self, total_with_tip: float, people_count: str) -> float:
        """Amount that each person should pay"""
        people_count_int = int(people_count)
        return total_with_tip / people_count_int
        
    def update_message_label(self, message: str, color: str) -> None:
        """Update display message with specific color"""
        self.message_label.setText(message)
        self.message_label.setStyleSheet(f"color: {color};")  

    

                 
        
        
