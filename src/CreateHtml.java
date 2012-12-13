package abc;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;


public class CreateHtml
{
	
	
    public static void create(String code[],int col[], int stpf[][], String results[], String file_name) //, int threshold_value)
    {
    	
    	// Create file 
    	FileWriter fstream;
        try 
        {
        	String html_file=file_name+"_report.html";
            fstream = new FileWriter(html_file);
            System.out.println("Output file created!");
            System.out.println();
            BufferedWriter out = new BufferedWriter(fstream);
            out.write("<html><head><title>Fault localization</title>");
            out.newLine();
            out.write("<script language=\"javascript\" type=\"text/javascript\">");
            out.newLine();
           
     
            out.newLine();
            out.write("function changeColors()");
            out.newLine();
            out.write("{	var thresh_temp = document.getElementById(\"threshold\").value;   var threshnum;");
            out.newLine();
            out.write("document.getElementById(\"thresh_value\").value=thresh_temp;");
            out.newLine();
            out.write("var thresh=parseInt(thresh_temp)*1.2;");
            out.newLine();
            out.write("var threshnum = parseInt(thresh);");
            out.newLine();
            out.write("for(var i=1; i < "+code.length+"; i++){");
            out.newLine();
            out.write("var elt = document.getElementById(i.toString());");
            out.newLine();
            out.write("var old_color = parseInt(elt.dataset.name);");
            out.newLine();
            out.write("if(old_color!=-1){");
            out.write("elt.style.backgroundColor = htmlColor(old_color, threshnum);}}");
    
            out.newLine();
            out.write("}");
            out.newLine();
            out.write("function htmlColor(color, threshold){");
    
     
            out.newLine();
            out.write("if(color < 0 || color > 120)");
            out.newLine();
            out.write("{   return \"#0000ff\";    }");
            out.newLine();
            out.write("midpoint = threshold / 2;");
            out.newLine();
            out.write("html = \"#\";");
    
            out.newLine();
            out.write("var redpart;");
            out.newLine();
            out.write("if( color <= midpoint ) {   redpart = 255;   } else {    var slope = -255 / midpoint;   var intercept = -slope * midpoint + 255;   redpart = Math.max(0, Math.floor(intercept + slope * color));   }");
            out.newLine();
            out.write("var red_hex = redpart.toString(16);");
            out.newLine();
            out.write("if(red_hex.length == 1) {   red_hex = \"0\" + red_hex;   }");
            out.newLine();
            out.write("html += red_hex;");
            out.write("//Compute green and append");
            out.newLine();
            out.write("var greenpart;");
            out.newLine();
            out.write("if( color >= midpoint ) {   greenpart = 255;   } else {    var slope = 255 / midpoint;   var intercept = 0;   greenpart = Math.max(0, Math.floor(intercept + slope * color));   }");
            out.newLine();
            out.write("var green_hex = greenpart.toString(16);");
            out.newLine();
            out.write("if(green_hex.length == 1) {   green_hex = \"0\" + green_hex;   }");
          
            out.newLine();
            out.write("html += green_hex;");
            out.newLine();
            out.write("// Blue is always 00");
            out.newLine();
            out.write("html += \"00\";      return html;	}");
            out.newLine();
    
    
            out.write("</script></head>");
            out.newLine();
            out.write("<body>");
 
            out.write("<br><br><h1><u>uroborus</u></h1><pre>");
 
            out.newLine();
  
            out.write("<center><div style=\"top:0;position:fixed;background-color:#ffffff;width:100%\">");
            out.newLine();
            out.write("Threshold:<input type=\"text\" id=\"thresh_value\" size=2 maxlength=3 value=\"100\">");
            out.write("<input id=\"threshold\" type=\"range\" style=\"width:80%\" min=\"0\" max=\"100\" value=\"100\" onchange=\"changeColors()\" />");
            out.newLine();
            out.write("</div></center><br>");
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
       
            	
            		sentence="<FONT size=\"5\"  >";
            		sentence+="<span id=\""+i+"\" data-name=\"-1\" STYLE=\"background-color:"+shade+"\" class=\"dropt\" title=\""+results[i]+"\">"+code[i];
            		sentence+=" <span style=\"width:500px;\"></span>";
            		sentence+="</span></FONT><br>";
            
            	}
            	else
            	{	
            	
            		shade=RangeColor.htmlColor(col[i]); //, threshold_value);
           
            		sentence="<FONT size=\"5\"  >"; 
   
           
            		sentence+="<span id=\""+i+"\" data-name=\""+col[i]+"\" STYLE=\"background-color:"+shade+"\" class=\"dropt\" title=\""+results[i]+"\">"+code[i];
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
        } 
        catch (IOException ex) 
        {
            Logger.getLogger(CreateHtml.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}

