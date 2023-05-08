
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Options(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(384, 146)
		self._groupBox1.TabIndex = 1
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Conference"
		# 
		# groupBox2
		# 
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(402, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(363, 146)
		self._groupBox2.TabIndex = 2
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Preconference Workshops"
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(7, 43)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(283, 29)
		self._checkBox1.TabIndex = 3
		self._checkBox1.Text = "Conference Registration: $895"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(7, 88)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(366, 30)
		self._checkBox2.TabIndex = 4
		self._checkBox2.Text = "Opening Night Dinner and Keynote: $30"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# Options
		# 
		self.ClientSize = System.Drawing.Size(805, 356)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Options"
		self.Text = "Options"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

