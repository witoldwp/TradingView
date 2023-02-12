class HomePage:
    def __init__(self, page):
        self.logo = page.get_by_role("button", name="Open user menu")
        # self.user_icon =
        # self.user_sign_in =
