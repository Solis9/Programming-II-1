﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg498Payroll
{
    public partial class Form1 : Form
    {
        const decimal decHOURLY_PAY_RATE = 6;
        const int intMAX_EMPLYEES = 6;
        // "const" prevents

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int[] intHours = new int[intMAX_EMPLYEES];
            int intCount = 0;
            int intEmpHours = 0;
            decimal decEmpPay = 0.0m;

            for (intCount = 0; intCount < intMAX_EMPLYEES; intCount++) {
                while (int.TryParse(
                    Interaction.InputBox("Enter the number of hours worked by employee #" +
                    (intCount+1).ToString(), "Need Hours Worked"),
                    out intEmpHours) == false) {
                        MessageBox.Show("Please enter an integer for hours worked");

                }
                intHours[intCount] = intEmpHours;
            }
            listBox1.Items.Clear();
            for (intCount = 0; intCount < intMAX_EMPLYEES; intCount++) {
                decEmpPay = intHours[intCount] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (intCount + 1).ToString() +
                    " earned " + decEmpPay.ToString("$.00"));
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
