from guizero import App, Text, TextBox, PushButton, Picture

app = App(title="Liam Newton", bg='white', width=1920, height=1080)

username = 'Liam'
password = 'password'

def check_input():
    if un_box.value == username and pw_box.value == password:
        message = Text(app, text='Correct')
        Picture(app, image="Kim.gif")
    else:
        message = Text(app, text='Virus Detected')
        Picture(app, image="giphy.gif")


text1 = Text(app, text="Username", size=100, font='algerian', color='aqua', align='')
un_box = TextBox(app, height=30, width=20)
text1 = Text(app, text="Password", size=100, font='algerian', color='aqua', align='')
pw_box = TextBox(app, height=30, width=20)
submit = PushButton(app, text='SUBMIT', command=check_input)


# text1 = Text(app, text="Hello GUI!!", size=100, font='algerian', color='aqua', align='')
#
# app.yesno(title="yes or no", text='Would you like to close this window?')
# app.warn(title='Virus Detected!', text="Virus")

app.display()
