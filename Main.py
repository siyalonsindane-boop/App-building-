import flet as ft

def main(page: ft.Page):
    page.title = "Neo App"
    page.add(
        ft.Text("Hello from Neo's first APK 🚀", size=30)
    )

ft.app(target=main)
