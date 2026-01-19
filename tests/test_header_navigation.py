from pages.home_page import HomePage

def test_header_links_navigation(page):
    home = HomePage(page)

    home.open()
    home.header.go_to_services()

    home.open()
    page.goto("https://www.jalasoft.com/clients")

    home.open()
    home.header.go_to_about_us()

    home.open()
    home.header.go_to_careers()

    home.open()
    home.header.go_to_blog()
