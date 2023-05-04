using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang85c
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int output = num1 * 5; //+ 6 * 4 + 9 * 5 + num2;
            int output2 = output + 6;
            int output3 = output2 * 4;
            int output4 = output3 + 9;
            int output5 = output4 * 5;
            int output6 = output5 + num2;
            int output7 = output6 - 165;
            double output8 = (double)output7 / 100;
            label4.Text = output6.ToString();
            label5.Text = output8.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            label4.Text = "";
            label5.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
