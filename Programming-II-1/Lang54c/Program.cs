using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lang54c
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Radius: ");
            int rad = int.Parse(Console.ReadLine());
            double cir = (double) rad * rad;
            double area = (double) rad * 3.14;

            Console.WriteLine("Radius: " + rad);
            Console.WriteLine("Circumference: " + cir);
            Console.WriteLine("Area: " + area);
            Console.ReadLine();
        }
    }
}
