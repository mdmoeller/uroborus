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
 
    public static void create(String code[],int col[], int stpf[][], String results[], String file_name)
    {
  // Create file 
  FileWriter fstream;
        try {
        	String html_file=file_name+"_report.html";
            fstream = new FileWriter(html_file);
            System.out.println("Output file created!");
        
  BufferedWriter out = new BufferedWriter(fstream);
  out.write("<html><head><title>Fault localization</title>");
  out.write("<script language=\"javascript\" type=\"text/javascript\">");
  out.write(" function validate(){ ");  
  out.write("var b=form1.threshold.value;");
  
  out.write("var numbers = /^[0-9]+$/;  ");
 out.write(" if(b.match(numbers))  ");
   
   out.write("{ var c=parseInt(b);");
   out.write("if(c<0 || c>120)");
    out.write("   {alert(\"Please enter a number in the range [0,120]!\"); }}"); 
        out.write("else {alert(\"Please enter a valid number!\");}}");
        out.write("</script></head>");
  out.write("<body>");
  out.write("<h1><u>uroborus</u></h1><pre>");
  out.write("<form name=\"form1\" action=\"#\">");
  out.write("<div align=\"center\">Threshold value: <input type=\"text\" name=\"threshold\"><br><input type=\"submit\" onclick=\"validate()\" value=\"Change\" /><br></div>");
  
  
 
  
 
  String str=null;
String shade=null;

String sentence=null;
    for( int i=1;i<code.length;i++)
        {
        
    		
    	
            
            if(stpf[i][0]==0 && stpf[i][1]==0)
            {
            	int index=0;
            	
            	
            	shade="#FFFFFF";
            	while(index<code[i].length())
            		if(code[i].charAt(index++)=='#')
            		{
            		
            			shade="#A4A4A4";
            			break;
            		}	
       
            	
            	sentence="<FONT size=\"5\" STYLE=\"background-color:"+shade+"\" >";
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

