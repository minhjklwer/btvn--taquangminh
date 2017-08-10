using System;

namespace BTVNsession63
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			while (true)
			{
			Console.Write ("Colums ? ");

			int Colums = Convert.ToInt32 (Console.ReadLine ()); 

			Console.Write ("Rows ? ");
			int Rows = Convert.ToInt32 (Console.ReadLine ());

				for (int o = 0; o < Rows; o++) {
					for(int m = 0; m < Colums; m++)
					{
							Console.Write ("X*");
					}

					Console.WriteLine ();
				}
			}
		}
	}
}

