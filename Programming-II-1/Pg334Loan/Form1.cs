using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg334Loan
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int intCount = 0;
            int intMonths = 0;
            double dblLoan = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dblPrincipal = 0.0;

            try {
                intMonths = int.Parse(txtMonth.Text);
                dblLoan = double.Parse(txtCost.Text) -
                          double.Parse(txtDownPayment.Text);
            }
            catch (Exception ex) {
                MessageBox.Show("Please enter numeric values");
                return;
            }

        }

        const int intMIN_MONTHS = 6;
        const int intMAX_MONTHS = 48;
        const float sngMONTHS_YEAR = 12.0f;

        const double dblNEW_RATE = 0.089;
        const double dblUSED_RATE = 0.095;

        double dblAnnualRate = dblNEW_RATE;

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
