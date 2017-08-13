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


			
			int convertnumber;
			int number;

				while (true) 
				{
					convertnumber = (nums % 2);

					number = (nums / 2);

					Console.Write (convertnumber);

					nums = number;

					if (number == 0) 
					{
						break;
					}
				}
			}
		}
	}
}




