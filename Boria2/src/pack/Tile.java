package pack;

public class Tile {
	private Bot bots[];
	private int x,y;
	private int g;
	
	public Tile(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	
	public void update() {
		for (int i = 0;i<Boria.bots.size();i++) {
			System.out.println("Test");
		}
	}
	public Bot[] getBots() {
		return bots;
	}

	public void setBots(Bot bots[]) {
		this.bots = bots;
	}

	public int getG() {
		return g;
	}

	public void setG(int g) {
		this.g = g;
	}

}
