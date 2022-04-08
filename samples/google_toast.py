# Create an instance
from exclude.creds import PASS_WORD, USER_NAME
from notus.google import GoogleToaster

ga = GoogleToaster(USER_NAME, PASS_WORD)
ga.set_log_level("debug")
ga.authenticate()
print(len(ga.list()))
ga.create("Google", {"delivery": "mail"})
