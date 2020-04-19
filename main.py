import pandas as pd
from flask import Flask, request, session, redirect, url_for, escape, render_template, send_file
import xlrd, os, uuid, pdfkit
from openpyxl.workbook import Workbook


from lib.errors import *
from lib.User import User
from lib.tableKeys import keys as tableKeys

app = Flask(__name__, 
			static_url_path='', 
            static_folder='templates/',
            template_folder='templates/')
app.secret_key = "some"



user = User();

@app.route('/', methods = ['GET'])
def home():
	if 'user' in session:
		return user.index()
	else:
		return redirect(url_for('login'))

@app.route('/blank', methods = ['GET'])
def blank():
	try:
		return user.blank()
	except LinkError:
		return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			session['user'] = 'admin'
			return redirect('/')
	return render_template('login.html', error=error)

@app.route('/logout', methods=['GET'])
def logout():
	if'user' in session:
		session.pop('user', None)
	return redirect(url_for('login'))


@app.route('/toPDF', methods=['GET'])
def toPDF():
	if not 'user' in session:
		return redirect(url_for('login'))
	ID = request.args.get('id', default = 1, type = int)
	pdfkit.from_url('http://'+request.host+'/blank?pdf=1&id='+str(ID), 'out.pdf')
	return send_file('out.pdf', as_attachment=True)


@app.route('/importFile', methods=['POST'])
def importFile():
	if not 'user' in session:
		return redirect(url_for('login'))

	sql = ("insert into invoice (")+(", ".join(tableKeys['invoice'])+") values (")+(", ".join([("'"+user.addslashes(request.form.get(i))+"'" if type(request.form.get(i)) == str else str(request.form.get(i))) for i in tableKeys['invoice']]))+");"
	invoiceID = user.db.insert(sql)
	file = request.files['uploadFile']

	products = tableKeys['products']

	df = pd.read_excel(file.stream, sheet_name=0)
	df.to_excel('temporary.xlsx', index=False)


	book = xlrd.open_workbook('temporary.xlsx')
	sheet = book.sheet_by_name("Sheet1")
	
	dt = []
	for c in range(1, sheet.nrows):
		key = c - 1
		kk = {'invoiceID': invoiceID}
		for r in range(0, sheet.ncols):
			kk[products[r]] = sheet.cell(c, r).value
		dt.append(kk)
	keys = list(filter(lambda x: x != 'id', products))
	keys.append('invoiceID')
	sql = ("insert into products (")+(", ".join(keys)+") values ")+(", ".join([("("+",".join([("'"+user.addslashes(i[k])+"'" if type(i[k]) == str else str(i[k])) for k in keys if k in i])+")") for i in dt]))
	
	insertID = user.db.insert(sql)
	return redirect('/blank?id={}'.format(invoiceID))
	

if __name__ == '__main__':
	app.config.from_object(__name__)
	app.run('0.0.0.0')
 