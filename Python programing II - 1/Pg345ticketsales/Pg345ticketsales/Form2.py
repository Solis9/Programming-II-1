
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._lblTotal = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTickets = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._txtNumTickets)
		self._groupBox2.Controls.Add(self._label1)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(12, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(288, 143)
		self._groupBox2.TabIndex = 2
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "How Many Tickets?"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(171, 36)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(100, 29)
		self._txtNumTickets.TabIndex = 4
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(159, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Number of tickets"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 82)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(265, 52)
		self._label2.TabIndex = 5
		self._label2.Text = "Student tickets are for seating in the student section only."
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._lblTickets)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label5)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(338, 12)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(213, 143)
		self._groupBox3.TabIndex = 6
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Cost"
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblTotal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblTotal.Location = System.Drawing.Point(89, 111)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(100, 23)
		self._lblTotal.TabIndex = 8
		# 
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblTax.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblTax.Location = System.Drawing.Point(89, 70)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(100, 23)
		self._lblTax.TabIndex = 7
		# 
		# lblTickets
		# 
		self._lblTickets.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblTickets.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblTickets.Location = System.Drawing.Point(89, 29)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(100, 23)
		self._lblTickets.TabIndex = 6
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(6, 111)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(58, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "Total:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(6, 70)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(48, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Tax:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(6, 25)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(76, 23)
		self._label5.TabIndex = 3
		self._label5.Text = "Tickets:"
		# 
		# btnCalculate
		# 
		self._btnCalculate.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnCalculate.Location = System.Drawing.Point(338, 161)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(97, 31)
		self._btnCalculate.TabIndex = 7
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClose.Location = System.Drawing.Point(454, 161)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(97, 31)
		self._btnClose.TabIndex = 8
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(565, 204)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Name = "Form2"
		self.Text = "Form2"
		self._groupBox2.ResumeLayout(False)
		self._groupBox2.PerformLayout()
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnCalculateClick(self, sender, e):
		intNumTickets = 0
		decTicketCost = 0.0
		decSalesTax = 0.0
		decTotal = 0.0
		
		intNumTickets = int(self.txtNumTickets.Text)
		decTicketCost = intNumTickets * decSTUDENT_PRICE
		decSalesTax = CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalesTax
		
		self._lblTickets.Text = str(round(decTicketCost), 2)
		self._lblTax.Text = str(round(decSalesTax), 2)
		self._lblTotal.Text = str(round(decTotal), 2)
		
		decTAXRATE = 0.06
		def CalcTax(cost):
			return cost * decTAXRATE