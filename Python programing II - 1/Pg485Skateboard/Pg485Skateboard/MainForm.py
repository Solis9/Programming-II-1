import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(261, 166)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Decks:"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(7, 29)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(241, 31)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "The Master Thrasher $60"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 78)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(241, 31)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "The Dictator of Grind $45"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 130)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(195, 31)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "The Street King $50"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(292, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(177, 166)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Truck assemblies:"
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(6, 129)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(139, 31)
		self._radioButton4.TabIndex = 5
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "8.5 axle $45"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(6, 77)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(139, 31)
		self._radioButton5.TabIndex = 4
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "8 axle $40"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(6, 28)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(139, 31)
		self._radioButton6.TabIndex = 3
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "7.75 axle $35"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton7)
		self._groupBox3.Controls.Add(self._radioButton8)
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(13, 185)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(261, 246)
		self._groupBox3.TabIndex = 3
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Miscellaneous:"
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(7, 103)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(241, 31)
		self._radioButton7.TabIndex = 2
		self._radioButton7.TabStop = True
		self._radioButton7.Text = ":"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(7, 66)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(241, 31)
		self._radioButton8.TabIndex = 1
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "Bearings $30"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(7, 29)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(241, 31)
		self._radioButton9.TabIndex = 0
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "Grip Tape $10"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(7, 177)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(241, 31)
		self._radioButton10.TabIndex = 4
		self._radioButton10.TabStop = True
		self._radioButton10.Text = ":"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(7, 140)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(241, 31)
		self._radioButton11.TabIndex = 3
		self._radioButton11.TabStop = True
		self._radioButton11.Text = ":"
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(547, 455)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg485Skateboard"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)

