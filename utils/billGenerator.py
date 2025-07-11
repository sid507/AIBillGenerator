from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
import io
import asyncio
import os
from datetime import datetime

# Define the Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))


class BillGenerator:
    def __init__(self):
        self.name = "Bill Generator Tool"
        self.description = "Generates a bill in PNG format from the provided data."
        self.output_dir = "generated_tickets"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_png(self, date: str,
            items: list[dict[str, int | str]],
            grandTotal: int) -> str:
        data = {
            "date": date,
            "items": items,
            "grandTotal": grandTotal
        }
        print(f"Generating PNG with data: {data}")
        # Render Jinja2 template
        template = env.get_template("bill.html")
        html_content = template.render(data)
        print(html_content)

        # Generate a unique filename
        filename = f"ticket_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        file_path = os.path.join(self.output_dir, filename)

        # Use sync Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html_content, wait_until="networkidle")
            page.screenshot(path=file_path, full_page=True)
            browser.close()

        return file_path  # Return the path to the generated PNG
