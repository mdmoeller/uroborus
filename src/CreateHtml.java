// package abc;

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
            System.out.println("HTML file created!");
        
  BufferedWriter out = new BufferedWriter(fstream);
  out.write("<html><head><title>DATA</title></head>");
  out.write("<body>");
  out.write("<h1><u>uroborus</u><h1><pre>");
  //out.write("<form>");
  //out.write("<center>");
  
 
  String str=null;
String shade=null;
//String red="red";
String sentence=null;
    for( int i=1;i<code.length;i++)
        {
        
    		/*for(int j=0;j<blank.length;j++)
    			if(i==blank[j])
    				i++;
    	
    		if(i<code.length)
    		{*/
    	
            //str=code[i]; //+(col[i]/120);
            
            if(stpf[i][0]==0 && stpf[i][1]==0)
            {
            	sentence="<FONT size=\"5\" STYLE=\"background-color:white\" >";
            	sentence+="<span class=\"dropt\" title=\""+results[i]+"\">"+code[i];
            	sentence+=" <span style=\"width:500px;\"></span>";
            	sentence+="</span></FONT><br>";
            
            	//
            	//sentence="<INPUT TYPE='text' SIZE='"+30+"' ALT=\"0\" value='"+str+" '  readonly><br/>";
            	//sentence="<A onMouseOver=\"document.bgColor=\'white\'\">"+str+"</a><br>";
            }
            else
            {	
            	//System.out.println("Color value= "+col[i]);	//Brightness value= "+bright[i]);
            shade=RangeColor.htmlColor(col[i]); //, bright[i]);
            //out.write("<font color='"+shade+"'>"+str+"</font><br/>");
            sentence="<FONT size=\"5\" STYLE=\"background-color:"+shade+"\" >"; 
   
            //sentence="<A onMouseOver=\"document.bgColor=\'"+shade+"\'\">"+str+"</a><br>";
            
            sentence+="<span class=\"dropt\" title=\""+results[i]+"\">"+code[i];
        	sentence+=" <span style=\"width:500px;\"></span>";
        	sentence+="</span></FONT><br>";
            
            }        
            //System.out.println(str);
            out.write(sentence); 
            //str.length()+
    		
        }	
    
  
    /*out.write("<script language="JavaScript" type="text/javascript">");
	out.write("var gDomain="www.qsstats.com";");
	out.write("var gDcsId="dcs37pv2c00000oun93vypyva_4k6d";");
	out.write("var gFpc="WT_FPC";");
	out.write("var gConvert=true;");
	out.write("var gFpcDom = "htmlgoodies.com";");
	out.write("if ((typeof(gConvert) != "undefined") && gConvert && (document.cookie.indexOf(gFpc + "=") == -1) && (document.cookie.indexOf("WTLOPTOUT=")==-1)) {");
	out.write("    document.write("<SCR"+"IPT TYPE='text/javascript' SRC='http"+(window.location.protocol.indexOf('https:')==0?'s':'')+"://"+gDomain+"/"+gDcsId+"/wtid.js"+"'><\/SCR"+"IPT>");");
	out.write("}");
	out.write("function dcsAdditionalParameters() {}");
   out.write(" </script>");*/
    
   out.write("</pre></body></html>");
  
  //Close the output stream
  out.close();
  } catch (IOException ex) {
            Logger.getLogger(CreateHtml.class.getName()).log(Level.SEVERE, null, ex);
        }
  }
 
  }

