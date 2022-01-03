# Create an instance
from notus.google import GoogleToaster
from exclude.creds import PASS_WORD, USER_NAME

ga = GoogleToaster(USER_NAME, PASS_WORD)
ga.set_log_level("debug")
ga.authenticate()
print(len(ga.list()))
ga.create("Google", {"delivery": "mail"})
