class SignInWithEmailPage:
    def __init__(self, page):
        self.user_email = page.locator()
        self.user_password = page.locator()