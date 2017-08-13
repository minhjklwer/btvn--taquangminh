using System;

namespace btvnsession7
{
	class MainClass
	{
		public static void Main (string[] args)
		{ 
			while(true){
				
			Random rnd = new Random ();
			int nums = rnd.Next(1 ,100);
			int convert;
			int number;
			while (true) 
			{
				convert = (nums % 2);

				number = (nums / 2);

				Console.Write (convert);

				nums = number;
				if (number == 0) 
 -				{
 -					break;
 -				}

				}
			}
		}
	}
}




