import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;



public class CreateHtml {

    public static void create(String code[],int col[], int stpf[][], String results[], String file_name)
    {
        // Create file 
        FileWriter fstream;
        try {
            String html_file=file_name+"_report.html";
            fstream = new FileWriter(html_file);
            System.out.println("Fle created");

            BufferedWriter out = new BufferedWriter(fstream);
            out.write("<html><head><title>DATA</title></head>");
            out.write("<body>");
            out.write("<h1><u>uroborus</u><h1><pre>");


            String str=null;
            String shade=null;

            String sentence=null;
            for( int i=1;i<code.length;i++)
            {

                if(stpf[i][0]==0 && stpf[i][1]==0)
                {
                    sentence="<FONT size=\"5\" STYLE=\"background-color:white\" >";
                    sentence+="<span class=\"dropt\" title=\""+results[i]+"\">"+code[i];
                    sentence+=" <span style=\"width:500px;\"></span>";
                    sentence+="</span></FONT><br>";
                }
                else
                {	

                    shade=RangeColor.htmlColor(col[i]);             
                    sentence="<FONT size=\"5\" STYLE=\"background-color:"+shade+"\" >"; 

                    sentence+="<span class=\"dropt\" title=\""+results[i]+"\">"+code[i];
                    sentence+=" <span style=\"width:500px;\"></span>";
                    sentence+="</span></FONT><br>";
                }        

                out.write(sentence); 
            }	

            out.write("</pre></body></html>");

            //Close the output stream
            out.close();
        } catch (IOException ex) {
            Logger.getLogger(CreateHtml.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
