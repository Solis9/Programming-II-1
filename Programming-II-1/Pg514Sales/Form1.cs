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

namespace Pg514Sales
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool GetSalesData(ref decimal[] decSales)
        {
            decimal[] decSalesData;
            int intNumDays = 0;
            int intCount;
            bool blnSuccess;

            string strNumDays = Interaction.InputBox("For how many days " + "do you have sales?");

            if (!int.TryParse(strNumDays, out intNumDays)) {
                MessageBox.Show("You entered a non-numeric value", "Error");
                return false;
            }

            if (intNumDays > 0) {
                decSalesData = new decimal[intNumDays];
                for (intCount = 0; intCount < intNumDays; intCount++) {
                    bool blnValid = false;
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}