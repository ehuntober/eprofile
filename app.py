import gspread
from flask import  Flask , render_template


gc = gspread.service_account(filename='eprofile.json')
sh = gc.open('eprofile')



shProfile = sh.get_worksheet(0)
values_list = shProfile.row_values(1)
print(shProfile)
print(values_list)
shContacts = sh.get_worksheet(1)
# shContacts.append_row(['B1', 'Bingo!'])
shContacts.update('A1:B2', [[1, 2], [3, 4]])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)