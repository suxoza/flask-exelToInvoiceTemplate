from flask import request, render_template
from flask_paginate import Pagination, get_page_parameter
from . import DB, tableKeys


class User:
	def __init__(self):
		self.db = DB.DB()

	def addslashes(self, s):
		l = ["\\", '"', "'", "\0", ]
		for i in l:
			if i in s:
				s = s.replace(i, '\\'+i)
		return s

	def getProducts(self):
		self.page = request.args.get('page', default = 1, type = int)
		

		transactionNum = 10
		
		start = (self.page - 1) * transactionNum
		sql = "select * from invoice "
		itemsCount = self.db.rowCount(sql)

		sql = '''
			select
				t.*,
				sum(t1.quantity) as quantity,
				sum(t1.sellingPrice) as sellingPrice
			from invoice t 
			left join products t1 on t1.invoiceID = t.id
			group by t.id
			order by t.id desc limit {},{}
		'''.format(start, transactionNum)
		select = self.db.bigSelect(sql)
		itemKeys = tableKeys.keys['invoice'] + ['quantity','sellingPrice']
		#print([len(select)])
		return [itemsCount, itemKeys, select]

	def blank(self):
		ID = request.args.get('id', default = 0, type = int)
		if not ID: raise LinkError()
		sql = '''
			select
				t.*,
				date_format(insert_date, "%M %d, %Y") as insert_date,
				sum(t1.quantity) as quantity,
				sum(t1.sellingPrice) as sellingPrice
			from invoice t 
			join products t1 on t1.invoiceID = t.id
			where t.id = {}
		'''.format(ID)
		invoice = self.db.select(sql)
		#print(invoice)
		sql = '''
			select 
				*, 
				substring(Description, 1, 30) as Description 
			from products 
			where invoiceID = {}
			'''.format(invoice['id'])
		select = self.db.bigSelect(sql)
		#print(select)
		if not select:raise LinkError()
		
		return render_template('blank.html', invoice = invoice, keys = tableKeys.keys['products'], values = select)

	def index(self):
		itemsCount, itemKeys, itemValues = self.getProducts()
		pagination = Pagination(page=self.page, total=itemsCount, record_name='users', css_framework = 'bootstrap')
		return render_template('home.html', count = itemsCount, keys = itemKeys, values = itemValues, pagination = pagination)