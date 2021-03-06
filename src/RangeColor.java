import java.util.Scanner;

public abstract class RangeColor
{

    private RangeColor(){}

    /**
     * Computes the html color corresponding to the color values given.
     *
     * @param color      an integer between <code>0</code> and <code>120</code> (inclusive) that 
     *                   represents the hue between red (0) and green (120).
     * @param brightness a double representing full brightness, <code>1.0</code> to 
     *                   null brightness, <code>0.0</code>.
     *
     * @return           an html string <code>"#XXXXXX"</code> according to the appropriate color. Note: 
     *                   in the case of invalid input, Blue is returned.
     */
    public static String htmlColor(int color, double brightness)
    {

        //Adjust lower
        // brightness *= .75;

        //On invalid input, return bright blue (a color not otherwise used).
        if(color < 0 || color > 120 || brightness < 0 || brightness > 100) {
            return "#0000ff"; 
        }

        String html = "#";

        //Compute red value and append
        int red = (int) (Math.min( -255.0 * color * brightness / 60 + 255.0 + 255.0 * brightness, 255.0 ));
        String red_hex = Integer.toHexString(red);
        if(red_hex.length() == 1) {
            red_hex = "0" + red_hex;
        }
        html += red_hex;

        //Compute green and append
        int green = (int) (Math.min( 255.0 * color * brightness / 60 + 255 * (1 - brightness), 255.0));
        String green_hex = Integer.toHexString(green);
        if(green_hex.length() == 1) {
            green_hex = "0" + green_hex;
        }
        html += green_hex;

        //Compute blue and append
        int blue = (int) ((1-brightness) * 255.0);
        String blue_hex = Integer.toHexString(blue);
        if(blue_hex.length() == 1) {
            blue_hex = "0" + blue_hex;
        }
        html += blue_hex;

       
        return html;
    }


    /**
     * Computes color as htmlColor assuming brightness of 1.0.
     *
     * @param color  an integer between <code>0</code> and <code>120</code> (inclusive) that 
     *               represents the hue between red (0) and green (120).
     *
     * @return       an html string <code>"#XXXXXX"</code> according to the appropriate color.
     */
    public static String htmlColor(int color)
    {
        return htmlColor(color, 1);
    }


    /**
     * For testing purposes.
     *
     * Prints a file to standard out which represents of range of colors as a color test.
     */

    public static void main(String[] args)
    {
        java.util.Random random = new java.util.Random();
        System.out.println("<html><title>RangeColor Demo</title>");
        System.out.println("<script language=\"javascript\">");
        System.out.println("    function changeColors()");
        System.out.println("    {");
        System.out.println("        document.getElementByID('1').style.");
        System.out.println("    }");
        System.out.println("</script>");


        for(int i=0; i<=120; i++) {
            System.out.print("<div id=\"" + (i) + "\"");
            int color = random.nextInt(120);
            System.out.print(" name=\"" + color + "\" style=\"background-color:" + htmlColor(color) + "\">");
            System.out.print("Statement number: " + i);
            System.out.println("</div><br>");
        }
        System.out.println("</html>");
    }
}
