using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273Book
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           int pts = 0;
           int books = int(textBox1.Text);

            if (books) = 0;{
                pts = 0;
            } else if (books) = 1 {
                pts = 5;
            } else if (books) = 2 {
                pts = 15;
            } else if (books) = 3 {
                pts = 30;
            } else if (books) >= 4 {
                pts = 60;
            }

        }
    }
}
