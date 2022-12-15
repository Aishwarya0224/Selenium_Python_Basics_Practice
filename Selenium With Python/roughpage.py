message = "Please email us at mentor.com with below template to receive response"

var = message.split("at")[1].strip().split(" ")[0]
print(var)