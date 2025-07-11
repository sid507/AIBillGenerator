from langchain.tools import tool
from utils.billGenerator import BillGenerator

@tool
def extractData(
    date: str,
    items: list[dict[str, int | str]],
    grandTotal: int,
    theme
) -> any:
    """fetches date, items, and grand total from given prompt"""
    print(f"Generating pop ticket PNG for date: {date}, items: {items}, grandTotal: {grandTotal}, theme: {theme}")
    # bill_generator = BillGenerator()
    # bill_generator.generate_png(date=date, items=items, grandTotal=grandTotal)
    return {"date": date, "items": items, "grandTotal": grandTotal, "theme": theme}

# If you need a class, do NOT instantiate it multiple times!
class BillDataExtractorTool:
    def __init__(self):
        self.name = "Extract Data Tool"
        self.description = "Extracts date, items, and grand total from the provided prompt "
        self.bill_generator_tool = [extractData]