package abc;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;



public class CreateHtml {
 
    public static void create(String code[],int col[], int stpf[][], double bright[])
    {
  // Create file 
 	 FileWriter fstream;
        try {
            fstream = new FileWriter("Data.html");
        
 	 BufferedWriter out = new BufferedWriter(fstream);
  	out.write("<html><head><title>DATA</title></head>");
  	out.write("<body>");
  	out.write("<h1>uroborus<h1>");
  
  
 
  	String str=null;
	String shade=null;

	String sentence=null;
    	for( int i=1;i<code.length;i++)
        {
        
    		
    	
           str=code[i]; 
            
           if(stpf[i][0]==0 && stpf[i][1]==0)
         	sentence="<FONT size=\"5\" STYLE=\"background-color:white\" >"+str+"</FONT><br>";
            	         else
            	{	
            	System.out.println("Color value= "+col[i]+"	Brightness value= "+bright[i]);
            	shade=RangeColor.htmlColor(col[i], bright[i]); 
            
            	sentence="<FONT size=\"5\" STYLE=\"background-color:"+shade+"\" >"+str+" </FONT><br/>"; 
   
              	}        
            
            	out.write(sentence); 
           
    		
        }	
    
  
    
    
   	out.write("</body></html>");
  
  	//Close the output stream
  	out.close();
  	} 
	catch (IOException ex) {
            Logger.getLogger(CreateHtml.class.getName()).log(Level.SEVERE, null, ex);
        }
  }
 
 }

