import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(19, 212)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(97, 30)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(122, 212)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(97, 30)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(225, 212)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(97, 30)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._button3)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._button2)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(352, 248)
		self._groupBox1.TabIndex = 3
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Phone Call Rate"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(7, 29)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(286, 30)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Daytime 6:00 a.m. -  5:59 p.m."
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 65)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(286, 30)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening 6:00 p.m. - 11:59 p.m."
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 101)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(286, 30)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off-Peak 12:00 a.m. - 5:59 a.m."
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 138)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(281, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Number of Minutes Used:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(7, 165)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(119, 29)
		self._textBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(378, 273)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg272LongDistance"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)



	def Button1Click(self, sender, e):
		rate = 0.0
		day = 
		evening = 
		peak =