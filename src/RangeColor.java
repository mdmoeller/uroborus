import java.util.Scanner;

public class RangeColor
{

    /**
     * Computes the html color corresponding to the color values given.
     * @param color an integer between 0 and 120 (inclusive) that represents the hue between red (0) and green (120).
     * @param brightness a double representing full brightness (1.0) to null brightness (0.0).
     */
    public static String htmlColor(int color, double brightness)
    {

        //Adjust lower
        brightness *= .75;

        //On invalid input, return bright blue (a color not otherwise used).
        if(color < 0 || color > 120 || brightness < 0 || brightness > 1) {
            return "#0000ff"; 
        }

        String html = "#";

        //Compute red value and append
        int red = (int) (Math.min( -255.0 * color / 60 + 510, 255.0 ) * brightness);
        String red_hex = Integer.toHexString(red);
        if(red_hex.length() == 1) {
            red_hex = "0" + red_hex;
        }
        html += red_hex;

        //Compute green and append
        int green = (int) (Math.min( 255.0 * color / 60, 255.0 ) * brightness);
        String green_hex = Integer.toHexString(green);
        if(green_hex.length() == 1) {
            green_hex = "0" + green_hex;
        }
        html += green_hex;

        //Never need any blue:
        html += "00";
       
        return html;
    }

    /**
     * Computes color as htmlColor assuming brightness of 1.0.
     */
    public static String htmlColor(int color)
    {
        return htmlColor(color, 1);
    }

    public static void main(String[] args)
    {
        // Scanner sc = new Scanner(System.in);

        // while(sc.hasNext()) {
            // System.out.println( htmlColor(sc.nextInt(), sc.nextDouble()) );
        // }
        //
        System.out.println("<html>");

        for(int i=0; i<=120; i++) {
            System.out.print("<font color=\"" + htmlColor(i) + "\"> This is color #" + i + ".</font>    ");
            System.out.print("<font color=\"" + htmlColor(i, .75) + "\"> This is color #" + i + ".</font>   ");
            System.out.print("<font color=\"" + htmlColor(i, .5) + "\"> This is color #" + i + ".</font>    ");
            System.out.println("<font color=\"" + htmlColor(i, 0) + "\"> This is color #" + i + ".</font><br>");
        }
        System.out.println("</html>");
    }
}
