import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._label7 = System.Windows.Forms.Label()
		self._textBox8 = System.Windows.Forms.TextBox()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox8)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._textBox7)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._textBox6)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._textBox5)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._textBox4)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(637, 216)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Registration"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 45)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(108, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Name:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(150, 45)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(137, 29)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(150, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(137, 29)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 90)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(108, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Company:"
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(150, 134)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(137, 29)
		self._textBox3.TabIndex = 5
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(6, 134)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(108, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Address:"
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(150, 178)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(137, 29)
		self._textBox4.TabIndex = 7
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(6, 178)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(108, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "City:"
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(484, 51)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(137, 29)
		self._textBox5.TabIndex = 9
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(340, 51)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(108, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Phone:"
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(484, 96)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(137, 29)
		self._textBox6.TabIndex = 11
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(340, 96)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(108, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "Email:"
		# 
		# textBox7
		# 
		self._textBox7.Location = System.Drawing.Point(415, 140)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(44, 29)
		self._textBox7.TabIndex = 13
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(340, 140)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(64, 23)
		self._label7.TabIndex = 12
		self._label7.Text = "State:"
		# 
		# textBox8
		# 
		self._textBox8.Location = System.Drawing.Point(531, 140)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(90, 29)
		self._textBox8.TabIndex = 15
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(468, 140)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(45, 23)
		self._label8.TabIndex = 14
		self._label8.Text = "Zip:"
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(415, 231)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 1
		self._label9.Text = "Total Cost:"
		# 
		# label10
		# 
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(533, 231)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 2
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 231)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(182, 57)
		self._button1.TabIndex = 3
		self._button1.Text = "Select Conference Options"
		self._button1.TextAlign = System.Drawing.ContentAlignment.TopLeft
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(205, 231)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 33)
		self._button2.TabIndex = 4
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(317, 231)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 33)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(665, 301)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg479Conference"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)

