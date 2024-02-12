package pack;

import java.awt.Color;
import java.awt.Graphics2D;
import java.util.Random;

class Bot {
    private double x, y;
    private static final int SIZE = 12;
    private static final Random random = new Random();
    private Color color = new Color(255,0,0);
    Color co1 = new Color(255,0,0);
    Color co2 = new Color(0,255,0);
    Color co3 = new Color(0,0,255);
    Color co4 = new Color(255, 165, 0);
    Color co5 = new Color(0,255,255);
    Color co6 = new Color(200,55,187);
    Color co7 = new Color (215, 134, 18);
    public Bot(int x, int y, Color color) {
        this.x = x;
        this.y = y;
        this.color = color;
    }

    public void update() {

    	double mX = 0; 
        double mY = 0;
        double g = 0; 
        for(int i = 0;i<Boria.bots.size();i++) {
        	
        	if (Boria.bots.get(i) != this) {
	            double oX = Boria.bots.get(i).x;
	            double oY = Boria.bots.get(i).y;
	
	            double dX = this.x - oX;
	            double dY = this.y - oY;
	
	            double dist = (dX*dX)+(dY*dY);
	            dist = Math.sqrt(dist);
	            if (dist <50) {
		        	if (Boria.bots.get(i).color.getRed() == 255 && Boria.bots.get(i).color.getGreen() == 0  && Boria.bots.get(i).color.getBlue() ==0) {
		        		
		        		//Contagion logic
		        		if (dist < Universe.d1 && Universe.c1 == 1 && (Universe.c11.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc1+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c11);

		        			}
		        		}
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			g = Universe.g1;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g2;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g3;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g4;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g5;
		
		        		}else if (this.color.getRed() == 200 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g6;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g7;
		
		        		}
		        	}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        		
		        		if (dist < Universe.d2 && Universe.c2 == 1 && (Universe.c12.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc2+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c12);

		        			}
		        		}
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			
		        			g = Universe.g8;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g9;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g10;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g11;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g12;
		
		        		}else if (this.color.getRed() == 200 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g13;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g14;
		
		        		}
		        	}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        		
		        		if (dist < Universe.d3 && Universe.c3 == 1 && (Universe.c13.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc3+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c13);

		        			}
		        		}
		        		
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			
		        			g = Universe.g15;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g16;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g17;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g18;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g19;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g20;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g21;
		
		        		}
		        		//255, 165, 0
		        	}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        		if (dist < Universe.d4 && Universe.c4 == 1 && (Universe.c14.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc4+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c14);

		        			}
		        		}
		        		
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			
		        			g = Universe.g1;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g22;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g23;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g24;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g25;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g26;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g27;
		
		        		}
		        	}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        		if (dist < Universe.d5 && Universe.c5 == 5 && (Universe.c15.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc5+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c15);

		        			}
		        		}
		        		
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			
		        			g = Universe.g28;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g29;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g30;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g31;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g32;
		
		        		}else if (this.color.getRed() == 200 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g33;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g34;
		
		        		}
		        		//200,55,187
		        	}else if (this.color.getRed() == 200 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        		if (dist < Universe.d6 && Universe.c6 == 1 && (Universe.c16.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc6+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c16);

		        			}
		        		}
		        		
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			
		        			g = Universe.g35;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g36;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g37;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g38;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g39;
		
		        		}else if (this.color.getRed() == 200 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g40;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g41;
		
		        		}
		        		//215, 134, 18
		        	}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        		if (dist < Universe.d7 && Universe.c7 == 1 && (Universe.c17.getRGB() != this.getColor().getRGB())) {
		        			int cChance = random.nextInt(Universe.cc7+1);
		        			if (cChance == 1) {
		        				Boria.bots.get(i).setColor(Universe.c17);
		        			}
		        		}
		        		
		        		
		        		if (this.color.getRed() == 255 && this.color.getGreen() == 0 && this.color.getBlue() == 0) {
		        			
		        			g = Universe.g42;
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 0) {
		        			g = Universe.g43;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 0 && this.color.getBlue() == 255) {
		        			g = Universe.g44;
		
		        		}else if (this.color.getRed() == 255 && this.color.getGreen() == 165 && this.color.getBlue() == 0) {
		        			g = Universe.g45;
		
		        		}else if (this.color.getRed() == 0 && this.color.getGreen() == 255 && this.color.getBlue() == 255) {
		        			g = Universe.g46;
		
		        		}else if (this.color.getRed() == 200 && this.color.getGreen() == 55 && this.color.getBlue() == 187) {
		        			g = Universe.g47;
		
		        		}else if (this.color.getRed() == 215 && this.color.getGreen() == 134 && this.color.getBlue() == 18) {
		        			g = Universe.g48;
		        		}
		        	}
		        	if (dist > 0) {
		                double F = g/((dist*Universe.grav)*10);
		                mX += (F*dX);
		                mY += (F*dY);
		        	}
	            
	            }
		        if (this.x < 10) {
		        	mX = mX*-1;
		        }
		        if (this.x > 1290) {
		        	mX = mX*-1;
		        }
		        if (this.y > 790) {
		        	mY = mY*-1;
		        }
		        if (this.y < 10) {
		        	mY = mY*-1;
		        }
		        
	        	this.setX((this.x + (mX)));
	        	this.setY((this.y + (mY)));
	        	
	        	if (this.x < 10) {
	        		this.setX(10);
	        	}
	        	if (this.x > 1290) {
	        		this.setX(1290);
	        	}
	        	if (this.y > 790) {
	        		this.setY(790);
	        	}
	        	if (this.y < 10) {
	        		this.setY(10);
	        	}
        
	
	        }
        }
    }

    public void draw(Graphics2D g2d) {
        g2d.setColor(this.color); // Example bot color
        g2d.fillOval((int) Math.round(x), (int) Math.round(y), SIZE, SIZE);
    }

	public Color getColor() {
		return color;
	}

	public void setColor(Color color) {
		this.color = color;
	}
	
	public void setX(double d) {
		this.x = d;
	}
	
	public void setY(double y) {
		this.y = y;
	}
}