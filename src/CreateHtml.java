package abc;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 *

 */
public class CreateHtml{
	
	static int threshold_value=0;
	static String code1[];
	static int col1[];
	static int stpf1[][];
	static String results1[];
	static String file_name1;
	
	public static void takeInput(String threshold)
	{
	
		System.out.println("Its working");
		System.out.println("Threshold value="+threshold);
		threshold_value=Integer.parseInt(threshold);
		create(code1,col1,stpf1,results1,file_name1, threshold_value);
		
	
	}
 
    public static void create(String code[],int col[], int stpf[][], String results[], String file_name, int threshold_value)
    {
    	code1=code;
    	col1=col;
    	stpf1=stpf;
    	results1=results;
    	file_name1=file_name;
  // Create file 
  FileWriter fstream;
        try {
        	String html_file=file_name+"_report.html";
            fstream = new FileWriter(html_file);
            System.out.println("Output file created!");
        
  BufferedWriter out = new BufferedWriter(fstream);
  out.write("<html><head><title>Fault localization</title>");
  out.newLine();
  out.write("<script language=\"javascript\" type=\"text/javascript\">");
  out.write(" function validate(){ ");  
  out.write("var b=form1.threshold.value;");
  
  out.write("var numbers = /^[0-9]+$/;  ");
 out.write(" if(b.match(numbers))  ");
   
   out.write("{ var c=parseInt(b);");
   out.write("if(c<0 || c>100)");
   out.write("   {alert(\"Please enter a number in the range [0,100]\"); }");
   out.write("passValue();");
   out.write("}"); 
     out.write("else {alert(\"Please enter a valid number!\");}");
     
     out.write("}");
     
     out.write("function passValue()");
     out.write("{takeInput(form1.threshold.value);}");
    // out.write("{theApplet = document.getElementById(\"app\");");
    // out.write("document.getElementById(\"display\").innerHTML = theApplet.takeInput(form1.threshold.value);");
     out.write("</script></head>");
     out.newLine();
  out.write("<body>");
 // out.write("<applet id=\"app\" width=0 height=0 code=\"CreateHTML.class\"></applet>");
  out.write("<h1><u>uroborus</u></h1><pre>");
  out.write("<form name=\"form1\" action=\"java CreateHTML\">");
  out.write("<div align=\"center\">Threshold value: <input type=\"text\" name=\"threshold\"><br>");
  out.write("<br><input type=\"submit\" onclick=\"validate()\" value=\"Change\" /><br></div>");
 // out.write("</form><div id=\"display\"></div>");
  out.newLine();
  
 
  
 
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
            	sentence+="<span id=\""+i+"\" name=\""+shade+"\" class=\"dropt\" title=\""+results[i]+"\">"+code[i];
            	sentence+=" <span style=\"width:500px;\"></span>";
            	sentence+="</span></FONT><br>";
            
            }
            else
            {	
            	
            shade=RangeColor.htmlColor(col[i]); //, threshold_value);
           
            sentence="<FONT size=\"5\" STYLE=\"background-color:"+shade+"\" >"; 
   
           
            
            sentence+="<span id=\""+i+"\" name=\""+shade+"\" class=\"dropt\" title=\""+results[i]+"\">"+code[i];
        	sentence+=" <span style=\"width:500px;\"></span>";
        	sentence+="</span></FONT><br>";
            
            }        
            
            out.write(sentence); 
            out.newLine();
    		
        }	
    
  
    
   out.write("</pre></body></html>");
   out.newLine();
  
  //Close the output stream
  out.close();
  } catch (IOException ex) {
            Logger.getLogger(CreateHtml.class.getName()).log(Level.SEVERE, null, ex);
        }
  }
 
  }

