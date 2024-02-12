package pack;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Boria extends JPanel implements ActionListener {
    private Timer timer;
    public static List<Bot> bots;
    private final int DELAY = 65; // Milliseconds between update/render calls
    public static Universe u = new Universe();
    public Boria() {
        setPreferredSize(new Dimension(1300, 800));
        setBackground(Color.BLACK);
        initGame();
    }

    private void initGame() {
        bots = new ArrayList<>();
        // Populate the bots list
        for (int i = 0; i < 2250; i++) { // Example: creating 100 bots
            bots.add(new Bot(650, 400, new Color(255,0,0))); // Starting all bots at the center for simplicity
        }
        
        timer = new Timer(DELAY, this);
        timer.start();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        doDrawing(g);
    }

    private void doDrawing(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        for (Bot bot : bots) {
            bot.draw(g2d);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        updateGame();
        repaint();
    }

    private void updateGame() {
        for (Bot bot : bots) {
            bot.update();
        }
    }

    public static void main(String[] args) {
    	SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Bots of Boria");
            Boria simulation = new Boria();
            
            frame.add(simulation);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);

            frame.addKeyListener(new KeyAdapter() {
                @Override
                public void keyPressed(KeyEvent e) {
                    if (e.getKeyCode() == KeyEvent.VK_R) { // If 'R' key is pressed
                        u.reset();; // Call the static resetGame method
                        simulation.repaint(); // Repaint the simulation panel to reflect changes
                    }
                }
            });
            try {
				Thread.sleep(100);
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}

            frame.setFocusable(true);
            frame.requestFocusInWindow();
        });
        
        
    }
}

