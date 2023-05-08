import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from Form1 import *
from Form2 import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._btnGeneral = System.Windows.Forms.Button()
		self._btnStudent = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._btnStudent)
		self._groupBox2.Controls.Add(self._btnGeneral)
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._label1)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(12, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(416, 186)
		self._groupBox2.TabIndex = 2
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Select the Type of Ticket Sales"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(284, 50)
		self._label1.TabIndex = 0
		self._label1.Text = "Select General Sales for all ticket sales to the general public"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 119)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(235, 52)
		self._label2.TabIndex = 1
		self._label2.Text = "Select Student Sales for all student ticket sales"
		# 
		# btnGeneral
		# 
		self._btnGeneral.Location = System.Drawing.Point(297, 29)
		self._btnGeneral.Name = "btnGeneral"
		self._btnGeneral.Size = System.Drawing.Size(94, 59)
		self._btnGeneral.TabIndex = 2
		self._btnGeneral.Text = "General Sales"
		self._btnGeneral.UseVisualStyleBackColor = True
		self._btnGeneral.Click += self.BtnGeneralClick
		# 
		# btnStudent
		# 
		self._btnStudent.Location = System.Drawing.Point(297, 119)
		self._btnStudent.Name = "btnStudent"
		self._btnStudent.Size = System.Drawing.Size(94, 59)
		self._btnStudent.TabIndex = 3
		self._btnStudent.Text = "Student Sales"
		self._btnStudent.UseVisualStyleBackColor = True
		self._btnStudent.Click += self.BtnStudentClick
		# 
		# btnExit
		# 
		self._btnExit.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnExit.Location = System.Drawing.Point(309, 204)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(93, 34)
		self._btnExit.TabIndex = 3
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(439, 251)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._groupBox2)
		self.Name = "MainForm"
		self.Text = "Pg435ticketsales"
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnGeneralClick(self, sender, e):
		Form1.Show()
		self.Hide()

	def BtnStudentClick(self, sender, e):
		pass