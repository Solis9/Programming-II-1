
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radSectionA = System.Windows.Forms.RadioButton()
		self._radSectionB = System.Windows.Forms.RadioButton()
		self._radSectionC = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(346, 75)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How Many Tickets?"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(75, 40)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(159, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of tickets"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(240, 40)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(100, 29)
		self._txtNumTickets.TabIndex = 1
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radSectionC)
		self._groupBox2.Controls.Add(self._radSectionB)
		self._groupBox2.Controls.Add(self._radSectionA)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(12, 93)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(127, 166)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Section"
		# 
		# radSectionA
		# 
		self._radSectionA.Location = System.Drawing.Point(7, 29)
		self._radSectionA.Name = "radSectionA"
		self._radSectionA.Size = System.Drawing.Size(109, 24)
		self._radSectionA.TabIndex = 0
		self._radSectionA.TabStop = True
		self._radSectionA.Text = "Section A"
		self._radSectionA.UseVisualStyleBackColor = True
		# 
		# radSectionB
		# 
		self._radSectionB.Location = System.Drawing.Point(7, 75)
		self._radSectionB.Name = "radSectionB"
		self._radSectionB.Size = System.Drawing.Size(109, 24)
		self._radSectionB.TabIndex = 1
		self._radSectionB.TabStop = True
		self._radSectionB.Text = "Section B"
		self._radSectionB.UseVisualStyleBackColor = True
		# 
		# radSectionC
		# 
		self._radSectionC.Location = System.Drawing.Point(7, 120)
		self._radSectionC.Name = "radSectionC"
		self._radSectionC.Size = System.Drawing.Size(109, 24)
		self._radSectionC.TabIndex = 2
		self._radSectionC.TabStop = True
		self._radSectionC.Text = "Section C"
		self._radSectionC.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._lblTickets)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label2)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(145, 93)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(213, 166)
		self._groupBox3.TabIndex = 3
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Cost"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 25)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(76, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Tickets:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(6, 75)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(48, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Tax:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(6, 120)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(58, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "Total:"
		# 
		# btnCalculate
		# 
		self._btnCalculate.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnCalculate.Location = System.Drawing.Point(63, 265)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(97, 30)
		self._btnCalculate.TabIndex = 4
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClose.Location = System.Drawing.Point(180, 265)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(97, 30)
		self._btnClose.TabIndex = 5
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
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
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblTax.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblTax.Location = System.Drawing.Point(89, 75)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(100, 23)
		self._lblTax.TabIndex = 7
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblTotal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblTotal.Location = System.Drawing.Point(89, 120)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(100, 23)
		self._lblTotal.TabIndex = 8
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(372, 310)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	#def TextBox4TextChanged(self, sender, e):
		#pass

	def BtnCalculateClick(self, sender, e):
		intNumTickets = 0
		decTicketCost = 0.0
		decSalesTax = 0.0
		decTotal = 0.0
		
		intNumTickets = int(self.txtNumTickets.Text)
		decTicketCost = intNumTickets * PriceEachTicket()
		decSalesTax = CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalesTax
		
		self._lblTickets.Text = str(round(decTicketCost), 2)
		self._lblTax.Text = str(round(decSalesTax), 2)
		self._lblTotal.Text = str(round(decTotal), 2)
		
		decTAXRATE = 0.06
		def CalcTax(cost):
			return cost * decTAXRATE