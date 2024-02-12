package pack;
import java.awt.Color;
import java.util.Random;

public class Universe {
	
	public static double grav = 0.0;
	static Random rand = new Random();
	public static double g1 = 0.0;
	public static double g2 = 0.0;
	public static double g3 = 0.0;
	public static double g4 = 0.0;
	public static double g5 = 0.0;
	public static double g6 = 0.0;
	public static double g7 = 0.0;
	public static double g8 = 0.0;
	public static double g9 = 0.0;
	public static double g10 = 0.0;
	public static double g11 = 0.0;
	public static double g12 = 0.0;
	public static double g13 = 0.0;
	public static double g14 = 0.0;
	public static double g15 = 0.0;
	public static double g16 = 0.0;
	public static double g17 = 0.0;
	public static double g18 = 0.0;
	public static double g19 = 0.0;
	public static double g20 = 0.0;
	public static double g21 = 0.0;
	public static double g22 = 0.0;
	public static double g23 = 0.0;
	public static double g24 = 0.0;
	public static double g25 = 0.0;
	public static double g26 = 0.0;
	public static double g27 = 0.0;
	public static double g28 = 0.0;
	public static double g29 = 0.0;
	public static double g30 = 0.0;
	public static double g31 = 0.0;
	public static double g32 = 0.0;
	public static double g33 = 0.0;
	public static double g34 = 0.0;
	public static double g35 = 0.0;
	public static double g36 = 0.0;
	public static double g37 = 0.0;
	public static double g38 = 0.0;
	public static double g39 = 0.0;
	public static double g40 = 0.0;
	public static double g41 = 0.0;
	public static double g42 = 0.0;
	public static double g43 = 0.0;
	public static double g44 = 0.0;
	public static double g45 = 0.0;
	public static double g46 = 0.0;
	public static double g47 = 0.0;
	public static double g48 = 0.0;
	
	public static int gDist  = rand.nextInt(650)+50;

	public static int c1  = rand.nextInt(2);
	public static int c2  = rand.nextInt(2);
	public static int c3  = rand.nextInt(2);
	public static int c4  = rand.nextInt(2);
	public static int c5  = rand.nextInt(2);
	public static int c6  = rand.nextInt(2);
	public static int c7  = rand.nextInt(2);


	public static int d1 =rand.nextInt(3);
	public static int d2 =rand.nextInt(3);
	public static int d3 =rand.nextInt(3);
	public static int d4 =rand.nextInt(3);
    public static int d5 =rand.nextInt(3);
    public static int d6 =rand.nextInt(3);
    public static int d7 =rand.nextInt(3);



	public static int cc1 =rand.nextInt(10);
	public static int cc2 =rand.nextInt(10);
	public static int cc3 =rand.nextInt(10);
	public static int cc4 =rand.nextInt(10);
	public static int cc5 =rand.nextInt(10);
	public static int cc6 =rand.nextInt(10);
	public static int cc7 =rand.nextInt(10);

	public static Color c11 = new Color(255,0,0);
	public static Color c12 = new Color(255,0,0);
	public static Color c13 = new Color(255,0,0);
	public static Color c14 = new Color(255,0,0);
	public static Color c15 = new Color(255,0,0);
	public static Color c16 = new Color(255,0,0);
	public static Color c17 = new Color(255,0,0);
	
	private static Color[] colors = {
	        new Color(255, 0, 0),
	        new Color(0, 255, 0),
	        new Color(0, 0, 255),
	        new Color(255, 165, 0),
	        new Color(0, 255, 255),
	        new Color(215, 134, 18),
	        new Color(200, 55, 187)
	    };
	
	public Universe() {
		
	}
	
	public void reset() {
		 gDist  = rand.nextInt(650)+50;
		 c11 = colors[rand.nextInt(colors.length)];
		 c12 = colors[rand.nextInt(colors.length)];
		 c13 = colors[rand.nextInt(colors.length)];
		 c14 = colors[rand.nextInt(colors.length)];
		 c15 = colors[rand.nextInt(colors.length)];
		 c16 = colors[rand.nextInt(colors.length)];
		 c17 = colors[rand.nextInt(colors.length)];

		 c1  = rand.nextInt(2);
		 c2  = rand.nextInt(2);
		 c3  = rand.nextInt(2);
		 c4  = rand.nextInt(2);
		 c5  = rand.nextInt(2);
		 c6  = rand.nextInt(2);
		 c7  = rand.nextInt(2);
		 
		 d1 = rand.nextInt(3);
		 d2 = rand.nextInt(3);
		 d3 = rand.nextInt(3);
		 d4 = rand.nextInt(3);
		 d5 = rand.nextInt(3);
		 d6 = rand.nextInt(3);
		 d7 = rand.nextInt(3);
		 
		 cc1 =rand.nextInt(100);
		 cc2 =rand.nextInt(100);
		 cc3 =rand.nextInt(100);
		 cc4 =rand.nextInt(100);
		 cc5 =rand.nextInt(100);
		 cc6 =rand.nextInt(100);
		 cc7 =rand.nextInt(100);

		 g1 = rand.nextDouble() * 1- 1; 
	     g2 = rand.nextDouble() * 1- 1; 
	     g3 = rand.nextDouble() * 1- 1;
	     g4 = rand.nextDouble() * 1- 1; 
	     g5 = rand.nextDouble() * 1- 1; 
	     g6 = rand.nextDouble() * 1- 1;
	     g7 = rand.nextDouble() * 1- 1; 
	     g8 = rand.nextDouble() * 1- 1; 
	     g9 = rand.nextDouble() * 1- 1;
	     g10 = rand.nextDouble() * 1- 1; 
	     g11 = rand.nextDouble() * 1- 1; 
	     g12 = rand.nextDouble() * 1- 1;
	     g13 = rand.nextDouble() * 1- 1; 
	     g14 = rand.nextDouble() * 1- 1; 
	     g15 = rand.nextDouble() * 1- 1;
	     g16 = rand.nextDouble() * 1- 1; 
	     g17 = rand.nextDouble() * 1- 1; 
	     g18 = rand.nextDouble() * 1- 1;
	     g19 = rand.nextDouble() * 1- 1; 
	     g20 = rand.nextDouble() * 1- 1; 
	     g21 = rand.nextDouble() * 1- 1;
	     g21 = rand.nextDouble() * 1- 1; 
	     g22 = rand.nextDouble() * 1- 1; 
	     g23 = rand.nextDouble() * 1- 1;
	     g24 = rand.nextDouble() * 1- 1; 
	     g25 = rand.nextDouble() * 1- 1; 
	     g26 = rand.nextDouble() * 1- 1;
	     g27 = rand.nextDouble() * 1- 1; 
	     g28 = rand.nextDouble() * 1- 1; 
	     g29 = rand.nextDouble() * 1- 1;
	     g30 = rand.nextDouble() * 1- 1; 
	     g31 = rand.nextDouble() * 1- 1; 
	     g32 = rand.nextDouble() * 1- 1;
	     g33 = rand.nextDouble() * 1- 1; 
	     g34 = rand.nextDouble() * 1- 1; 
	     g35 = rand.nextDouble() * 1- 1;
	     g36 = rand.nextDouble() * 1- 1; 
	     g37 = rand.nextDouble() * 1- 1; 
	     g38 = rand.nextDouble() * 1- 1;
	     g39 = rand.nextDouble() * 1- 1; 
	     g40 = rand.nextDouble() * 1- 1; 
	     g41 = rand.nextDouble() * 1- 1;
	     g42 = rand.nextDouble() * 1- 1; 
	     g43 = rand.nextDouble() * 1- 1; 
	     g44 = rand.nextDouble() * 1- 1; 
	     g45 = rand.nextDouble() * 1- 1;
	     g46 = rand.nextDouble() * 1- 1; 
	     g47 = rand.nextDouble() * 1- 1;
	     g48 = rand.nextDouble() * 1- 1; 
	     
	     grav = (rand.nextDouble()  * 10) + 180 ;
    	 int cg = rand.nextInt(2);

	     for (Bot bot : Boria.bots) {
	    	 int x = rand.nextInt(1300);
	    	 int y = rand.nextInt(800);
	    	 bot.setX(x);
	    	 bot.setY(y);
	    	 int c = rand.nextInt(7);
	    	if (cg == 0) {
		    	if (c == 0) {
			         bot.setColor(new Color (255,0,0));
		    	}else if (c == 1) {
		    		bot.setColor(new Color (0, 255, 0));
		        }else if (c == 2) {
		        	bot.setColor(new Color (0, 0, 255));
		        }else if (c == 3) {
		        	bot.setColor(new Color (255, 165, 0));
		        }else if (c == 4) {
		        	bot.setColor(new Color (0, 255, 255));
		        }else if (c == 5) {
		        	bot.setColor(new Color (215, 134, 18));
		        }else if (c == 6) {
		        	bot.setColor(new Color (200, 55, 187));
		        }
	    	}else if (cg == 1) {
		    	if (c == 0) {
			         bot.setColor(new Color (255,0,0));
		    	}else {
		    		bot.setColor(new Color (0, 255, 0));
		    	}
	    	}else {
	    		if (c == 0 || c== 1 || c== 2) {
			         bot.setColor(new Color (255,0,0));
		    	}else if (c == 3 || c == 4 || c== 5) {
		    		bot.setColor(new Color (0, 255, 0));
		        }else
		        	bot.setColor(new Color (0, 0, 255));
		        
	    	}
	     }
	}

}
