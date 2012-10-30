package abc;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 *

 */
public class CreateHtml {
 
    public static void create(String code[],int col[])
    {
  // Create file 
  FileWriter fstream;
        try {
            fstream = new FileWriter("Data.html");
        
  BufferedWriter out = new BufferedWriter(fstream);
  out.write("<html><head><title>DATA</title></head>");
  out.write("<body>");
  out.write("<h1>CODE<h1>");
  out.write("<form>");
  
 
  String str=null;
String shade=null;
//String red="red";
String sentence=null;
    for( int i=1;i<code.length;i++)
        {
            
            str=code[i];
            shade=RangeColor.htmlColor(col[i]);
            //out.write("<font color='"+shade+"'>"+str+"</font><br/>");
 sentence="<INPUT TYPE='text' SIZE='"+30+"' STYLE='background-color:"+shade+"' value='"+str+" '  readonly><br/>"; 
           out.write(sentence); 
            //str.length()+
        }
    
  
   out.write("</body></html>");
  
  //Close the output stream
  out.close();
  } catch (IOException ex) {
            Logger.getLogger(CreateHtml.class.getName()).log(Level.SEVERE, null, ex);
        }
  }
 
  }

